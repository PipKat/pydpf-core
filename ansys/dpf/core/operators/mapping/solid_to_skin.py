"""
solid_to_skin
=============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "mapping" category
"""

class solid_to_skin(Operator):
    """Maps a field defined on solid elements to a field defined on skin elements.

      available inputs:
        - field (Field, FieldsContainer)
        - mesh_scoping (MeshedRegion) (optional)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.mapping.solid_to_skin()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_mesh_scoping = dpf.MeshedRegion()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.mapping.solid_to_skin(field=my_field,mesh_scoping=my_mesh_scoping)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, mesh_scoping=None, config=None, server=None):
        super().__init__(name="solid_to_skin", config = config, server = server)
        self._inputs = InputsSolidToSkin(self)
        self._outputs = OutputsSolidToSkin(self)
        if field !=None:
            self.inputs.field.connect(field)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)

    @staticmethod
    def _spec():
        spec = Specification(description="""Maps a field defined on solid elements to a field defined on skin elements.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["abstract_meshed_region"], optional=True, document="""skin mesh region expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "solid_to_skin")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsSolidToSkin 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsSolidToSkin 
        """
        return super().outputs


#internal name: solid_to_skin
#scripting name: solid_to_skin
class InputsSolidToSkin(_Inputs):
    """Intermediate class used to connect user inputs to solid_to_skin operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mapping.solid_to_skin()
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_mesh_scoping = dpf.MeshedRegion()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    """
    def __init__(self, op: Operator):
        super().__init__(solid_to_skin._spec().inputs, op)
        self._field = Input(solid_to_skin._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._field)
        self._mesh_scoping = Input(solid_to_skin._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh_scoping)

    @property
    def field(self):
        """Allows to connect field input to the operator

        - pindoc: field or fields container with only one field is expected

        Parameters
        ----------
        my_field : Field, FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.solid_to_skin()
        >>> op.inputs.field.connect(my_field)
        >>> #or
        >>> op.inputs.field(my_field)

        """
        return self._field

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator

        - pindoc: skin mesh region expected

        Parameters
        ----------
        my_mesh_scoping : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.solid_to_skin()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> #or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)

        """
        return self._mesh_scoping

class OutputsSolidToSkin(_Outputs):
    """Intermediate class used to get outputs from solid_to_skin operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mapping.solid_to_skin()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(solid_to_skin._spec().outputs, op)
        self._field = Output(solid_to_skin._spec().output_pin(0), 0, op) 
        self._outputs.append(self._field)

    @property
    def field(self):
        """Allows to get field output of the operator


        Returns
        ----------
        my_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.solid_to_skin()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

