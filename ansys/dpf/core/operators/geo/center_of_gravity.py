"""
center_of_gravity
=================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "geo" category
"""

class center_of_gravity(Operator):
    """Compute the center of gravity of a set of elements

      available inputs:
        - mesh (MeshedRegion) (optional)
        - mesh_scoping (Scoping) (optional)
        - field (Field) (optional)

      available outputs:
        - field (Field)
        - mesh (MeshedRegion)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.geo.center_of_gravity()

      >>> # Make input connections
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.geo.center_of_gravity(mesh=my_mesh,mesh_scoping=my_mesh_scoping,field=my_field)

      >>> # Get output data
      >>> result_field = op.outputs.field()
      >>> result_mesh = op.outputs.mesh()"""
    def __init__(self, mesh=None, mesh_scoping=None, field=None, config=None, server=None):
        super().__init__(name="topology::center_of_gravity", config = config, server = server)
        self._inputs = InputsCenterOfGravity(self)
        self._outputs = OutputsCenterOfGravity(self)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if field !=None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute the center of gravity of a set of elements""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=True, document="""Mesh scoping, if not set, all the elements of the mesh are considered."""), 
                                 2 : PinSpecification(name = "field", type_names=["field"], optional=True, document="""Elemental or nodal ponderation used in computation.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document="""Center of gravity as a mesh""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "topology::center_of_gravity")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsCenterOfGravity 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsCenterOfGravity 
        """
        return super().outputs


#internal name: topology::center_of_gravity
#scripting name: center_of_gravity
class InputsCenterOfGravity(_Inputs):
    """Intermediate class used to connect user inputs to center_of_gravity operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.geo.center_of_gravity()
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
    """
    def __init__(self, op: Operator):
        super().__init__(center_of_gravity._spec().inputs, op)
        self._mesh = Input(center_of_gravity._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._mesh)
        self._mesh_scoping = Input(center_of_gravity._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh_scoping)
        self._field = Input(center_of_gravity._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._field)

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        Parameters
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.geo.center_of_gravity()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator

        - pindoc: Mesh scoping, if not set, all the elements of the mesh are considered.

        Parameters
        ----------
        my_mesh_scoping : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.geo.center_of_gravity()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> #or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)

        """
        return self._mesh_scoping

    @property
    def field(self):
        """Allows to connect field input to the operator

        - pindoc: Elemental or nodal ponderation used in computation.

        Parameters
        ----------
        my_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.geo.center_of_gravity()
        >>> op.inputs.field.connect(my_field)
        >>> #or
        >>> op.inputs.field(my_field)

        """
        return self._field

class OutputsCenterOfGravity(_Outputs):
    """Intermediate class used to get outputs from center_of_gravity operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.geo.center_of_gravity()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
      >>> result_mesh = op.outputs.mesh()
    """
    def __init__(self, op: Operator):
        super().__init__(center_of_gravity._spec().outputs, op)
        self._field = Output(center_of_gravity._spec().output_pin(0), 0, op) 
        self._outputs.append(self._field)
        self._mesh = Output(center_of_gravity._spec().output_pin(1), 1, op) 
        self._outputs.append(self._mesh)

    @property
    def field(self):
        """Allows to get field output of the operator


        Returns
        ----------
        my_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.geo.center_of_gravity()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

    @property
    def mesh(self):
        """Allows to get mesh output of the operator


        - pindoc: Center of gravity as a mesh

        Returns
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.geo.center_of_gravity()
        >>> # Connect inputs : op.inputs. ...
        >>> result_mesh = op.outputs.mesh() 
        """
        return self._mesh

