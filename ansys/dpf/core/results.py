"""
.. _ref_results:

Results
========
This module contains the Results and Result classes that are created by the model
to easily access results in result files."""
import functools


from ansys.dpf.core import Operator
from ansys.dpf.core import errors
from ansys.dpf.core.scoping import Scoping
from ansys.dpf.core.custom_fields_container import (
    ElShapeFieldsContainer,
    BodyFieldsContainer,
)


class Results:
    """Organizes the results from DPF into accessible methods.

    All the available results are dynamically created base on the model's class:'ResultInfo' class.

    Attributes
    ----------
    displacement : Result
        Result provider helper wrapping the regular displacement operator.
        With this wrapper, time and mesh scopings can easily
        be customized.

        Examples
        --------
        Create a displacement result from the model and choose its time and mesh scopings.

        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.msup_transient)
        >>> disp = model.results.displacement.on_last_time_freq.on_named_selection("_CONSTRAINEDNODES")
        >>> last_time_disp = disp.eval()

    stress : Result
        Result provider helper wrapping the regular stress operator.
        With this wrapper, time and mesh scopings, location, and more
        can easily be customized.

        Examples
        --------
        Create a stress result from the model and choose its time and mesh scopings.

        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.msup_transient)
        >>> stress = model.results.stress.on_last_time_freq.on_named_selection('_CONSTRAINEDNODES')
        >>> last_time_stress = stress.eval()

    .... all other results : Result
        Result provider helper wrapping all types of providers available for a
        given result file.

        Examples
        --------
        Create a stress result from the model and choose its time and mesh scopings.

        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.electric_therm)
        >>> v = model.results.electric_potential
        >>> rf = model.results.reaction_force
        >>> dissip = model.results.thermal_dissipation_energy

    Examples
    --------
    Extract the result object from a model.

    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> model = dpf.Model(examples.simple_bar)
    >>> results = model.results # printable object

    Access the displacement at all times.

    >>> from ansys.dpf.core import Model
    >>> from ansys.dpf.core import examples
    >>> transient = examples.download_transient_result()
    >>> model = Model(transient)
    >>> displacements = model.results.displacement.on_all_time_freqs.eval()

    """  # noqa: E501

    def __init__(self, model):
        self.__class__ = type(Results.__name__ + str(id(self)), (Results,), {})

        self._result_info = model.metadata.result_info
        self._model = model
        self._connect_operators()

    def __result__(self, result_type, *args):
        return Result(self._model, result_type)

    def _connect_operators(self):
        """Dynamically add operators for results.

        The new operator's subresults are connected to the model's
        streams.

        Examples
        --------
        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = Model(transient)
        >>> disp_operator = model.results.displacement()
        >>> stress_operator = model.results.stress()
        >>> disp_x = model.results.displacement().X()
        >>> disp_y = model.results.displacement().Y()
        >>> disp_z = model.results.displacement().Z()

        """
        if self._result_info is None:
            return
        # dynamically add function based on input type
        self._op_map_rev = {}
        for result_type in self._result_info:
            try:
                doc = Operator(
                    result_type.operator_name, server=self._model._server
                ).__str__()
                bound_method = self.__result__
                method2 = functools.partial(bound_method, result_type)
                setattr(self.__class__, result_type.name, property(method2, doc=doc))

                self._op_map_rev[result_type.name] = result_type.name
            except errors.DPFServerException:
                pass
            except Exception as e:
                print(result_type.name)
                raise e

    def __str__(self):
        return str(self._result_info)

    def __iter__(self):
        for key in self._op_map_rev:
            yield self.__class__.__dict__[key].fget()

    def __getitem__(self, val):
        n = 0
        for key in self._op_map_rev:
            if n == val:
                return self.__class__.__dict__[key].fget()
            n += 1

    def __len__(self):
        return len(self._op_map_rev)


class Result:
    """Helps with using DPF's result providers.

    This class helps to connect common inputs to the operator and
    recover its fields container output. 'Result' is created by the model.

    Examples
    --------
    Create a displacement result from the model and choose its time and mesh scopings

    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> model = dpf.Model(examples.msup_transient)
    >>> disp = model.results.displacement.on_last_time_freq.on_named_selection('_CONSTRAINEDNODES')
    >>> last_time_disp = disp.eval()

    Create a stress result from the model and split the result by element shapes (solid,
    shell, and beam).

    >>> model = dpf.Model(examples.download_all_kinds_of_complexity())
    >>> stress = model.results.stress
    >>> stress_split = stress.split_by_shape.eval()
    >>> solid_stress = stress_split.solid_field()

    Create a strain result from the model on all time sets and recover the
    operator to connect it to other operators.

    >>> model = dpf.Model(examples.msup_transient)
    >>> strain = model.results.elastic_strain.on_all_time_freqs()
    >>> eqv = dpf.operators.invariant.von_mises_eqv_fc(strain)
    >>> strain_eqv = eqv.outputs.fields_container()

    """

    def __init__(self, model, result_info):
        self._model = model
        self._time_scoping = None
        self._mesh_scoping = None
        self._location = None
        self._result_info = result_info
        self._specific_fc_type = None
        from ansys.dpf.core import operators

        try:
            # create the operator to read its documentation
            # if the operator doesn't exist, the method will not be added
            doc = Operator(
                self._result_info.operator_name, server=self._model._server
            ).__str__()
            self.__doc__ = doc
            if hasattr(operators, "result") and hasattr(
                operators.result, self._result_info.name
            ):
                self._operator = getattr(operators.result, self._result_info.name)(
                    server=self._model._server
                )
            else:
                self._operator = Operator(
                    self._result_info.operator_name, server=self._model._server
                )
            self._operator._add_sub_res_operators(self._result_info.sub_results)
            self._model.__connect_op__(self._operator)
        except errors.DPFServerException:
            pass
        except Exception as e:
            print(self._result_info.name)
            raise e

    def __call__(self, time_scoping=None, mesh_scoping=None):
        op = self._operator
        if time_scoping:
            op.inputs.time_scoping(time_scoping)
        elif self._time_scoping:
            op.inputs.time_scoping(self._time_scoping)

        if mesh_scoping:
            op.inputs.mesh_scoping(mesh_scoping)
        elif self._mesh_scoping:
            op.inputs.mesh_scoping(self._mesh_scoping)

        if self._location:
            op.inputs.requested_location(self._location)

        return op

    def eval(self):
        """Evaluate the result provider with the previously specified
        inputs and return the result fields container.

        Returns
        -------
        fields_container : FieldsContainer, ElShapeFieldsContainer, BodyFieldsContainer
            If ``split_by_body`` is used, a ``BodyFieldsContainer`` is returned.
            if ``split_by_shape`` is used, an ``ElShapeFieldsContainer`` is returned.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.msup_transient)
        >>> disp = model.results.displacement
        >>> fc = disp.on_all_time_freqs.eval()

        """
        fc = self.__call__().outputs.fields_container()
        if self._specific_fc_type == "shape":
            fc = ElShapeFieldsContainer(fields_container=fc, server=fc._server)
        elif self._specific_fc_type == "body":
            fc = BodyFieldsContainer(fields_container=fc, server=fc._server)
        return fc

    @property
    def on_all_time_freqs(self):
        """Sets the time scoping to all the time frequencies available in the time frequency support.

        Returns
        -------
        self : Result

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.msup_transient)
        >>> disp = model.results.displacement
        >>> disp.on_all_time_freqs.eval().get_label_scoping("time").ids
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

        """
        self._time_scoping = list(
            range(1, len(self._model.metadata.time_freq_support.time_frequencies) + 1)
        )
        return self

    @property
    def on_first_time_freq(self):
        """Sets the time scoping to the first time frequency available in the time frequency support.

        Returns
        -------
        self : Result

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.msup_transient)
        >>> disp = model.results.displacement
        >>> disp.on_first_time_freq.eval().get_label_scoping("time").ids
        [1]

        """
        self._time_scoping = 1
        return self

    @property
    def on_last_time_freq(self):
        """Sets the time scoping to the last time frequency available in the time frequency support.

        Returns
        -------
        self : Result

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.msup_transient)
        >>> disp = model.results.displacement
        >>> disp.on_last_time_freq.eval().get_label_scoping("time").ids
        [20]

        """
        self._time_scoping = len(
            self._model.metadata.time_freq_support.time_frequencies
        )
        return self

    def on_time_scoping(self, time_scoping):
        """Sets the time scoping to a given one.

        Parameters
        ----------
        time_scoping :  float, list[float], int, list[int], Scoping
            One or more times or frequencies.

        Returns
        -------
        self : Result

        Examples
        --------
        Choose time sets.

        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.msup_transient)
        >>> stress = model.results.stress
        >>> fc = stress.on_time_scoping([1,2,3,19]).eval()
        >>> len(fc)
        4

        Choose times. If the times chosen are not in the time frequency support,
        results are extrapolated.

        >>> fc = stress.on_time_scoping([0.115,0.125]).eval()
        >>> len(fc)
        2
        >>> fc.time_freq_support.time_frequencies.data
        array([0.115, 0.125])

        """
        self._time_scoping = time_scoping
        return self

    def on_named_selection(self, named_selection):
        """Set the mesh scoping to a given named selection.

        Parameters
        ----------
        named_selection : str
            Name of the named selection or component in upper case.

        Returns
        -------
        self : Result

        Examples
        --------
        Add a requested location to the average result on the nodes.

        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.msup_transient)
        >>> stress = model.results.stress
        >>> fc = stress.on_first_time_freq.on_named_selection('_CONSTRAINEDNODES').eval()
        >>> len(fc[0].scoping)
        40

        """

        self._mesh_scoping = self._model.metadata.named_selection(named_selection)
        return self

    @property
    def split_by_body(self):
        """Set the mesh scoping to a scopings container where each scoping is a body.

        Returns
        -------
        self : Result

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.download_all_kinds_of_complexity())
        >>> disp = model.results.displacement
        >>> fc_disp = disp.split_by_body.eval()
        >>> len(fc_disp)
        11
        >>> fc_disp.get_mat_scoping().ids
        [1, 5, 6, 10, 2, 7, 8, 13, 4, 12, 15]
        >>> disp_mat_10 = fc_disp.get_field_by_mat_id(10)

        """
        self._specific_fc_type = "body"
        return self._add_split_on_property_type("mat")

    @property
    def split_by_shape(self):
        """Set the mesh scoping to a scopings container where each scoping is an element shape.
        The evaluated fields container will have one field on 'solid',
        one on 'shell', one on 'beam' and one on 'unknown_shape'.

        Returns
        -------
        self : Result

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.download_all_kinds_of_complexity())
        >>> disp = model.results.displacement
        >>> fc_disp = disp.split_by_shape.eval()
        >>> len(fc_disp)
        4

        >>> shell_disp = fc_disp.shell_field()
        >>> solid_disp = fc_disp.solid_field()

        """
        self._specific_fc_type = "shape"
        return self._add_split_on_property_type("elshape")

    def _add_split_on_property_type(self, prop):
        previous_mesh_scoping = self._mesh_scoping
        from ansys.dpf.core import operators

        if hasattr(operators, "scoping") and hasattr(
            operators.scoping, "split_on_property_type"
        ):
            self._mesh_scoping = operators.scoping.split_on_property_type()
        else:
            self._mesh_scoping = Operator("scoping::by_property")

        self._mesh_scoping.inputs.requested_location(
            self._result_info.native_scoping_location
        )
        self._mesh_scoping.inputs.mesh(self._model.metadata.mesh_provider)
        self._mesh_scoping.inputs.label1(prop)
        if previous_mesh_scoping:
            try:
                self._mesh_scoping.inputs.mesh_scoping(previous_mesh_scoping)
            except:
                pass
        return self

    def on_mesh_scoping(self, mesh_scoping):
        """Set the mesh scoping to a given mesh scoping.

        Parameters
        ----------
        mesh_scoping : Scoping, list[int]

        Returns
        -------
        self : Result

        Examples
        --------
        Use a list of nodes.

        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.complex_rst)
        >>> disp = model.results.displacement
        >>> fc = disp.on_mesh_scoping([1,2,3]).eval()
        >>> len(fc[0].scoping)
        3

        Use a scoping to specify a list of entity IDs with their locations.

        >>> stress = model.results.stress
        >>> scop = dpf.Scoping(ids=[3,4,5], location= dpf.locations.nodal)
        >>> fc = stress.on_mesh_scoping(scop).eval()
        >>> len(fc[0].scoping)
        3
        >>> fc[0].location
        'Nodal'

        """
        if isinstance(mesh_scoping, list):
            mesh_scoping = Scoping(
                ids=mesh_scoping,
                location=self._result_info.native_scoping_location,
                server=self._model._server,
            )

        self._mesh_scoping = mesh_scoping
        return self

    def on_location(self, location):
        """Set the requested location of the provider.

        Elemental nodal fields can be averaged to a nodal or elemental location.

        Parameters
        ----------
        location : str, locations

        Returns
        -------
        self : Result

        Examples
        --------
        Add a requested location to the average result on the nodes.

        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.complex_rst)
        >>> stress = model.results.stress
        >>> fc = stress.eval()
        >>> fc[0].location
        'ElementalNodal'

        >>> fc = stress.on_location(dpf.locations.nodal).eval()
        >>> fc[0].location
        'Nodal'

        """
        self._location = location
        return self
