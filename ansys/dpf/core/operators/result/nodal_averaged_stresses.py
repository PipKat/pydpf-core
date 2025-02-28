"""
nodal_averaged_stresses
=======================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from mapdlOperatorsCore plugin, from "result" category
"""

class nodal_averaged_stresses(Operator):
    """Read nodal averaged stresses as averaged nodal result from rst file.

      available inputs:
        - time_scoping (Scoping, list) (optional)
        - mesh_scoping (ScopingsContainer, Scoping, list) (optional)
        - fields_container (FieldsContainer) (optional)
        - streams_container (StreamsContainer, Stream) (optional)
        - data_sources (DataSources)
        - mesh (MeshedRegion) (optional)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.result.nodal_averaged_stresses()

      >>> # Make input connections
      >>> my_time_scoping = dpf.Scoping()
      >>> op.inputs.time_scoping.connect(my_time_scoping)
      >>> my_mesh_scoping = dpf.ScopingsContainer()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.result.nodal_averaged_stresses(time_scoping=my_time_scoping,mesh_scoping=my_mesh_scoping,fields_container=my_fields_container,streams_container=my_streams_container,data_sources=my_data_sources,mesh=my_mesh)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, time_scoping=None, mesh_scoping=None, fields_container=None, streams_container=None, data_sources=None, mesh=None, config=None, server=None):
        super().__init__(name="mapdl::rst::NS", config = config, server = server)
        self._inputs = InputsNodalAveragedStresses(self)
        self._outputs = OutputsNodalAveragedStresses(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read nodal averaged stresses as averaged nodal result from rst file.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","vector<int32>"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping","vector<int32>"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container","stream"], optional=True, document="""Streams containing the result file."""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""data sources containing the result file."""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""FieldsContainer filled in""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapdl::rst::NS")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsNodalAveragedStresses 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsNodalAveragedStresses 
        """
        return super().outputs


#internal name: mapdl::rst::NS
#scripting name: nodal_averaged_stresses
class InputsNodalAveragedStresses(_Inputs):
    """Intermediate class used to connect user inputs to nodal_averaged_stresses operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.nodal_averaged_stresses()
      >>> my_time_scoping = dpf.Scoping()
      >>> op.inputs.time_scoping.connect(my_time_scoping)
      >>> my_mesh_scoping = dpf.ScopingsContainer()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
    """
    def __init__(self, op: Operator):
        super().__init__(nodal_averaged_stresses._spec().inputs, op)
        self._time_scoping = Input(nodal_averaged_stresses._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._time_scoping)
        self._mesh_scoping = Input(nodal_averaged_stresses._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh_scoping)
        self._fields_container = Input(nodal_averaged_stresses._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._fields_container)
        self._streams_container = Input(nodal_averaged_stresses._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._streams_container)
        self._data_sources = Input(nodal_averaged_stresses._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._data_sources)
        self._mesh = Input(nodal_averaged_stresses._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self._mesh)

    @property
    def time_scoping(self):
        """Allows to connect time_scoping input to the operator

        Parameters
        ----------
        my_time_scoping : Scoping, list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.nodal_averaged_stresses()
        >>> op.inputs.time_scoping.connect(my_time_scoping)
        >>> #or
        >>> op.inputs.time_scoping(my_time_scoping)

        """
        return self._time_scoping

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator

        Parameters
        ----------
        my_mesh_scoping : ScopingsContainer, Scoping, list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.nodal_averaged_stresses()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> #or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)

        """
        return self._mesh_scoping

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        - pindoc: FieldsContainer already allocated modified inplace

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.nodal_averaged_stresses()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def streams_container(self):
        """Allows to connect streams_container input to the operator

        - pindoc: Streams containing the result file.

        Parameters
        ----------
        my_streams_container : StreamsContainer, Stream, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.nodal_averaged_stresses()
        >>> op.inputs.streams_container.connect(my_streams_container)
        >>> #or
        >>> op.inputs.streams_container(my_streams_container)

        """
        return self._streams_container

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator

        - pindoc: data sources containing the result file.

        Parameters
        ----------
        my_data_sources : DataSources, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.nodal_averaged_stresses()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> #or
        >>> op.inputs.data_sources(my_data_sources)

        """
        return self._data_sources

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        Parameters
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.nodal_averaged_stresses()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

class OutputsNodalAveragedStresses(_Outputs):
    """Intermediate class used to get outputs from nodal_averaged_stresses operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.nodal_averaged_stresses()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(nodal_averaged_stresses._spec().outputs, op)
        self._fields_container = Output(nodal_averaged_stresses._spec().output_pin(0), 0, op) 
        self._outputs.append(self._fields_container)

    @property
    def fields_container(self):
        """Allows to get fields_container output of the operator


        - pindoc: FieldsContainer filled in

        Returns
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.nodal_averaged_stresses()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

