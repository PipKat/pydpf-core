"""
to_elemental_fc
===============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "averaging" category
"""

class to_elemental_fc(Operator):
    """Transform input fields into Elemental fields using an averaging process, result is computed on a given elements scoping.

      available inputs:
        - fields_container (FieldsContainer)
        - mesh (MeshedRegion) (optional)
        - mesh_scoping (Scoping) (optional)
        - smoothen_values (bool) (optional)
        - collapse_shell_layers (bool) (optional)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.to_elemental_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_smoothen_values = bool()
      >>> op.inputs.smoothen_values.connect(my_smoothen_values)
      >>> my_collapse_shell_layers = bool()
      >>> op.inputs.collapse_shell_layers.connect(my_collapse_shell_layers)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.averaging.to_elemental_fc(fields_container=my_fields_container,mesh=my_mesh,mesh_scoping=my_mesh_scoping,smoothen_values=my_smoothen_values,collapse_shell_layers=my_collapse_shell_layers)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, mesh=None, mesh_scoping=None, smoothen_values=None, collapse_shell_layers=None, config=None, server=None):
        super().__init__(name="to_elemental_fc", config = config, server = server)
        self._inputs = InputsToElementalFc(self)
        self._outputs = OutputsToElementalFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if smoothen_values !=None:
            self.inputs.smoothen_values.connect(smoothen_values)
        if collapse_shell_layers !=None:
            self.inputs.collapse_shell_layers.connect(collapse_shell_layers)

    @staticmethod
    def _spec():
        spec = Specification(description="""Transform input fields into Elemental fields using an averaging process, result is computed on a given elements scoping.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document=""""""), 
                                 3 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=True, document=""""""), 
                                 7 : PinSpecification(name = "smoothen_values", type_names=["bool"], optional=True, document="""if it is set to true, elemental nodal fields are first averaged on nodes and then averaged on elements (default is false)"""), 
                                 10 : PinSpecification(name = "collapse_shell_layers", type_names=["bool"], optional=True, document="""if true shell layers are averaged as well (default is false)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "to_elemental_fc")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsToElementalFc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsToElementalFc 
        """
        return super().outputs


#internal name: to_elemental_fc
#scripting name: to_elemental_fc
class InputsToElementalFc(_Inputs):
    """Intermediate class used to connect user inputs to to_elemental_fc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.averaging.to_elemental_fc()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_smoothen_values = bool()
      >>> op.inputs.smoothen_values.connect(my_smoothen_values)
      >>> my_collapse_shell_layers = bool()
      >>> op.inputs.collapse_shell_layers.connect(my_collapse_shell_layers)
    """
    def __init__(self, op: Operator):
        super().__init__(to_elemental_fc._spec().inputs, op)
        self._fields_container = Input(to_elemental_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._mesh = Input(to_elemental_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh)
        self._mesh_scoping = Input(to_elemental_fc._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._mesh_scoping)
        self._smoothen_values = Input(to_elemental_fc._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self._smoothen_values)
        self._collapse_shell_layers = Input(to_elemental_fc._spec().input_pin(10), 10, op, -1) 
        self._inputs.append(self._collapse_shell_layers)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.to_elemental_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        Parameters
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.to_elemental_fc()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator

        Parameters
        ----------
        my_mesh_scoping : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.to_elemental_fc()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> #or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)

        """
        return self._mesh_scoping

    @property
    def smoothen_values(self):
        """Allows to connect smoothen_values input to the operator

        - pindoc: if it is set to true, elemental nodal fields are first averaged on nodes and then averaged on elements (default is false)

        Parameters
        ----------
        my_smoothen_values : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.to_elemental_fc()
        >>> op.inputs.smoothen_values.connect(my_smoothen_values)
        >>> #or
        >>> op.inputs.smoothen_values(my_smoothen_values)

        """
        return self._smoothen_values

    @property
    def collapse_shell_layers(self):
        """Allows to connect collapse_shell_layers input to the operator

        - pindoc: if true shell layers are averaged as well (default is false)

        Parameters
        ----------
        my_collapse_shell_layers : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.to_elemental_fc()
        >>> op.inputs.collapse_shell_layers.connect(my_collapse_shell_layers)
        >>> #or
        >>> op.inputs.collapse_shell_layers(my_collapse_shell_layers)

        """
        return self._collapse_shell_layers

class OutputsToElementalFc(_Outputs):
    """Intermediate class used to get outputs from to_elemental_fc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.averaging.to_elemental_fc()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(to_elemental_fc._spec().outputs, op)
        self._fields_container = Output(to_elemental_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self._fields_container)

    @property
    def fields_container(self):
        """Allows to get fields_container output of the operator


        Returns
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.to_elemental_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

