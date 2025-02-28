"""
nodal_rotation_by_euler_nodes
=============================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from mapdlOperatorsCore plugin, from "result" category
"""

class nodal_rotation_by_euler_nodes(Operator):
    """read Euler angles on nodes from the rst file and rotate the fields in the fieldsContainer.

      available inputs:
        - fields_container (FieldsContainer) (optional)
        - streams_container (StreamsContainer, Stream) (optional)
        - data_sources (DataSources)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.result.nodal_rotation_by_euler_nodes()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.result.nodal_rotation_by_euler_nodes(fields_container=my_fields_container,streams_container=my_streams_container,data_sources=my_data_sources)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, streams_container=None, data_sources=None, config=None, server=None):
        super().__init__(name="mapdl::rst::RotateNodalFCByEulerNodes", config = config, server = server)
        self._inputs = InputsNodalRotationByEulerNodes(self)
        self._outputs = OutputsNodalRotationByEulerNodes(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""read Euler angles on nodes from the rst file and rotate the fields in the fieldsContainer.""",
                             map_input_pin_spec={
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document=""""""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container","stream"], optional=True, document=""""""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapdl::rst::RotateNodalFCByEulerNodes")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsNodalRotationByEulerNodes 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsNodalRotationByEulerNodes 
        """
        return super().outputs


#internal name: mapdl::rst::RotateNodalFCByEulerNodes
#scripting name: nodal_rotation_by_euler_nodes
class InputsNodalRotationByEulerNodes(_Inputs):
    """Intermediate class used to connect user inputs to nodal_rotation_by_euler_nodes operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.nodal_rotation_by_euler_nodes()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
    """
    def __init__(self, op: Operator):
        super().__init__(nodal_rotation_by_euler_nodes._spec().inputs, op)
        self._fields_container = Input(nodal_rotation_by_euler_nodes._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._fields_container)
        self._streams_container = Input(nodal_rotation_by_euler_nodes._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._streams_container)
        self._data_sources = Input(nodal_rotation_by_euler_nodes._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._data_sources)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.nodal_rotation_by_euler_nodes()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def streams_container(self):
        """Allows to connect streams_container input to the operator

        Parameters
        ----------
        my_streams_container : StreamsContainer, Stream, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.nodal_rotation_by_euler_nodes()
        >>> op.inputs.streams_container.connect(my_streams_container)
        >>> #or
        >>> op.inputs.streams_container(my_streams_container)

        """
        return self._streams_container

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator

        Parameters
        ----------
        my_data_sources : DataSources, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.nodal_rotation_by_euler_nodes()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> #or
        >>> op.inputs.data_sources(my_data_sources)

        """
        return self._data_sources

class OutputsNodalRotationByEulerNodes(_Outputs):
    """Intermediate class used to get outputs from nodal_rotation_by_euler_nodes operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.nodal_rotation_by_euler_nodes()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(nodal_rotation_by_euler_nodes._spec().outputs, op)
        self._fields_container = Output(nodal_rotation_by_euler_nodes._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.result.nodal_rotation_by_euler_nodes()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

