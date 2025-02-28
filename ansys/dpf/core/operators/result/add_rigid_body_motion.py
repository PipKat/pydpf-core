"""
add_rigid_body_motion
=====================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from mapdlOperatorsCore plugin, from "result" category
"""

class add_rigid_body_motion(Operator):
    """Adds a given rigid translation, center and rotation from a displacement field. The rotation is given in terms of rotations angles. Note that the displacement field has to be in the global coordinate sytem

      available inputs:
        - displacement_field (Field)
        - translation_field (Field)
        - rotation_field (Field)
        - center_field (Field)
        - mesh (MeshedRegion) (optional)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.result.add_rigid_body_motion()

      >>> # Make input connections
      >>> my_displacement_field = dpf.Field()
      >>> op.inputs.displacement_field.connect(my_displacement_field)
      >>> my_translation_field = dpf.Field()
      >>> op.inputs.translation_field.connect(my_translation_field)
      >>> my_rotation_field = dpf.Field()
      >>> op.inputs.rotation_field.connect(my_rotation_field)
      >>> my_center_field = dpf.Field()
      >>> op.inputs.center_field.connect(my_center_field)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.result.add_rigid_body_motion(displacement_field=my_displacement_field,translation_field=my_translation_field,rotation_field=my_rotation_field,center_field=my_center_field,mesh=my_mesh)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, displacement_field=None, translation_field=None, rotation_field=None, center_field=None, mesh=None, config=None, server=None):
        super().__init__(name="RigidBodyAddition", config = config, server = server)
        self._inputs = InputsAddRigidBodyMotion(self)
        self._outputs = OutputsAddRigidBodyMotion(self)
        if displacement_field !=None:
            self.inputs.displacement_field.connect(displacement_field)
        if translation_field !=None:
            self.inputs.translation_field.connect(translation_field)
        if rotation_field !=None:
            self.inputs.rotation_field.connect(rotation_field)
        if center_field !=None:
            self.inputs.center_field.connect(center_field)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Adds a given rigid translation, center and rotation from a displacement field. The rotation is given in terms of rotations angles. Note that the displacement field has to be in the global coordinate sytem""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "displacement_field", type_names=["field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "translation_field", type_names=["field"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "rotation_field", type_names=["field"], optional=False, document=""""""), 
                                 3 : PinSpecification(name = "center_field", type_names=["field"], optional=False, document=""""""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""default is the mesh in the support""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "RigidBodyAddition")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsAddRigidBodyMotion 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsAddRigidBodyMotion 
        """
        return super().outputs


#internal name: RigidBodyAddition
#scripting name: add_rigid_body_motion
class InputsAddRigidBodyMotion(_Inputs):
    """Intermediate class used to connect user inputs to add_rigid_body_motion operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.add_rigid_body_motion()
      >>> my_displacement_field = dpf.Field()
      >>> op.inputs.displacement_field.connect(my_displacement_field)
      >>> my_translation_field = dpf.Field()
      >>> op.inputs.translation_field.connect(my_translation_field)
      >>> my_rotation_field = dpf.Field()
      >>> op.inputs.rotation_field.connect(my_rotation_field)
      >>> my_center_field = dpf.Field()
      >>> op.inputs.center_field.connect(my_center_field)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
    """
    def __init__(self, op: Operator):
        super().__init__(add_rigid_body_motion._spec().inputs, op)
        self._displacement_field = Input(add_rigid_body_motion._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._displacement_field)
        self._translation_field = Input(add_rigid_body_motion._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._translation_field)
        self._rotation_field = Input(add_rigid_body_motion._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._rotation_field)
        self._center_field = Input(add_rigid_body_motion._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._center_field)
        self._mesh = Input(add_rigid_body_motion._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self._mesh)

    @property
    def displacement_field(self):
        """Allows to connect displacement_field input to the operator

        Parameters
        ----------
        my_displacement_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.add_rigid_body_motion()
        >>> op.inputs.displacement_field.connect(my_displacement_field)
        >>> #or
        >>> op.inputs.displacement_field(my_displacement_field)

        """
        return self._displacement_field

    @property
    def translation_field(self):
        """Allows to connect translation_field input to the operator

        Parameters
        ----------
        my_translation_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.add_rigid_body_motion()
        >>> op.inputs.translation_field.connect(my_translation_field)
        >>> #or
        >>> op.inputs.translation_field(my_translation_field)

        """
        return self._translation_field

    @property
    def rotation_field(self):
        """Allows to connect rotation_field input to the operator

        Parameters
        ----------
        my_rotation_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.add_rigid_body_motion()
        >>> op.inputs.rotation_field.connect(my_rotation_field)
        >>> #or
        >>> op.inputs.rotation_field(my_rotation_field)

        """
        return self._rotation_field

    @property
    def center_field(self):
        """Allows to connect center_field input to the operator

        Parameters
        ----------
        my_center_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.add_rigid_body_motion()
        >>> op.inputs.center_field.connect(my_center_field)
        >>> #or
        >>> op.inputs.center_field(my_center_field)

        """
        return self._center_field

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        - pindoc: default is the mesh in the support

        Parameters
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.add_rigid_body_motion()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

class OutputsAddRigidBodyMotion(_Outputs):
    """Intermediate class used to get outputs from add_rigid_body_motion operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.add_rigid_body_motion()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(add_rigid_body_motion._spec().outputs, op)
        self._field = Output(add_rigid_body_motion._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.result.add_rigid_body_motion()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

