"""
mesh_cut
========
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from meshOperatorsCore plugin, from "mesh" category
"""

class mesh_cut(Operator):
    """Extracts a skin of the mesh in triangles (2D elements) in a new meshed region

      available inputs:
        - field (Field)
        - iso_value (float)
        - closed_surface (float)
        - slice_surfaces (bool)

      available outputs:
        - mesh (MeshedRegion)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.mesh.mesh_cut()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_iso_value = float()
      >>> op.inputs.iso_value.connect(my_iso_value)
      >>> my_closed_surface = float()
      >>> op.inputs.closed_surface.connect(my_closed_surface)
      >>> my_slice_surfaces = bool()
      >>> op.inputs.slice_surfaces.connect(my_slice_surfaces)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.mesh.mesh_cut(field=my_field,iso_value=my_iso_value,closed_surface=my_closed_surface,slice_surfaces=my_slice_surfaces)

      >>> # Get output data
      >>> result_mesh = op.outputs.mesh()"""
    def __init__(self, field=None, iso_value=None, closed_surface=None, slice_surfaces=None, config=None, server=None):
        super().__init__(name="mesh_cut", config = config, server = server)
        self._inputs = InputsMeshCut(self)
        self._outputs = OutputsMeshCut(self)
        if field !=None:
            self.inputs.field.connect(field)
        if iso_value !=None:
            self.inputs.iso_value.connect(iso_value)
        if closed_surface !=None:
            self.inputs.closed_surface.connect(closed_surface)
        if slice_surfaces !=None:
            self.inputs.slice_surfaces.connect(slice_surfaces)

    @staticmethod
    def _spec():
        spec = Specification(description="""Extracts a skin of the mesh in triangles (2D elements) in a new meshed region""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "iso_value", type_names=["double"], optional=False, document="""iso value"""), 
                                 3 : PinSpecification(name = "closed_surface", type_names=["double"], optional=False, document="""1: closed surface, 0:iso surface"""), 
                                 4 : PinSpecification(name = "slice_surfaces", type_names=["bool"], optional=False, document="""true: slicing will also take into account shell and 2D elements, false: sliicing will ignore shell and 2D elements. default is true""")},
                             map_output_pin_spec={
                                 2 : PinSpecification(name = "mesh", type_names=["meshed_region"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mesh_cut")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMeshCut 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMeshCut 
        """
        return super().outputs


#internal name: mesh_cut
#scripting name: mesh_cut
class InputsMeshCut(_Inputs):
    """Intermediate class used to connect user inputs to mesh_cut operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mesh.mesh_cut()
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_iso_value = float()
      >>> op.inputs.iso_value.connect(my_iso_value)
      >>> my_closed_surface = float()
      >>> op.inputs.closed_surface.connect(my_closed_surface)
      >>> my_slice_surfaces = bool()
      >>> op.inputs.slice_surfaces.connect(my_slice_surfaces)
    """
    def __init__(self, op: Operator):
        super().__init__(mesh_cut._spec().inputs, op)
        self._field = Input(mesh_cut._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._field)
        self._iso_value = Input(mesh_cut._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._iso_value)
        self._closed_surface = Input(mesh_cut._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._closed_surface)
        self._slice_surfaces = Input(mesh_cut._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._slice_surfaces)

    @property
    def field(self):
        """Allows to connect field input to the operator

        Parameters
        ----------
        my_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.mesh_cut()
        >>> op.inputs.field.connect(my_field)
        >>> #or
        >>> op.inputs.field(my_field)

        """
        return self._field

    @property
    def iso_value(self):
        """Allows to connect iso_value input to the operator

        - pindoc: iso value

        Parameters
        ----------
        my_iso_value : float, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.mesh_cut()
        >>> op.inputs.iso_value.connect(my_iso_value)
        >>> #or
        >>> op.inputs.iso_value(my_iso_value)

        """
        return self._iso_value

    @property
    def closed_surface(self):
        """Allows to connect closed_surface input to the operator

        - pindoc: 1: closed surface, 0:iso surface

        Parameters
        ----------
        my_closed_surface : float, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.mesh_cut()
        >>> op.inputs.closed_surface.connect(my_closed_surface)
        >>> #or
        >>> op.inputs.closed_surface(my_closed_surface)

        """
        return self._closed_surface

    @property
    def slice_surfaces(self):
        """Allows to connect slice_surfaces input to the operator

        - pindoc: true: slicing will also take into account shell and 2D elements, false: sliicing will ignore shell and 2D elements. default is true

        Parameters
        ----------
        my_slice_surfaces : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.mesh_cut()
        >>> op.inputs.slice_surfaces.connect(my_slice_surfaces)
        >>> #or
        >>> op.inputs.slice_surfaces(my_slice_surfaces)

        """
        return self._slice_surfaces

class OutputsMeshCut(_Outputs):
    """Intermediate class used to get outputs from mesh_cut operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mesh.mesh_cut()
      >>> # Connect inputs : op.inputs. ...
      >>> result_mesh = op.outputs.mesh()
    """
    def __init__(self, op: Operator):
        super().__init__(mesh_cut._spec().outputs, op)
        self._mesh = Output(mesh_cut._spec().output_pin(2), 2, op) 
        self._outputs.append(self._mesh)

    @property
    def mesh(self):
        """Allows to get mesh output of the operator


        Returns
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.mesh_cut()
        >>> # Connect inputs : op.inputs. ...
        >>> result_mesh = op.outputs.mesh() 
        """
        return self._mesh

