"""
rigid_transformation
====================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "result" category
"""

class rigid_transformation(Operator):
    """Extracts rigid body motions from a displacement in input.

      available inputs:
        - streams_container (StreamsContainer) (optional)
        - data_sources (DataSources)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.result.rigid_transformation()

      >>> # Make input connections
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.result.rigid_transformation(streams_container=my_streams_container,data_sources=my_data_sources)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, streams_container=None, data_sources=None, config=None, server=None):
        super().__init__(name="RigidTransformationProvider", config = config, server = server)
        self._inputs = InputsRigidTransformation(self)
        self._outputs = OutputsRigidTransformation(self)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Extracts rigid body motions from a displacement in input.""",
                             map_input_pin_spec={
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""streams (result file container) (optional)"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""if the stream is null then we need to get the file path from the data sources""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "RigidTransformationProvider")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsRigidTransformation 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsRigidTransformation 
        """
        return super().outputs


#internal name: RigidTransformationProvider
#scripting name: rigid_transformation
class InputsRigidTransformation(_Inputs):
    """Intermediate class used to connect user inputs to rigid_transformation operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.rigid_transformation()
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
    """
    def __init__(self, op: Operator):
        super().__init__(rigid_transformation._spec().inputs, op)
        self._streams_container = Input(rigid_transformation._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._streams_container)
        self._data_sources = Input(rigid_transformation._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._data_sources)

    @property
    def streams_container(self):
        """Allows to connect streams_container input to the operator

        - pindoc: streams (result file container) (optional)

        Parameters
        ----------
        my_streams_container : StreamsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.rigid_transformation()
        >>> op.inputs.streams_container.connect(my_streams_container)
        >>> #or
        >>> op.inputs.streams_container(my_streams_container)

        """
        return self._streams_container

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator

        - pindoc: if the stream is null then we need to get the file path from the data sources

        Parameters
        ----------
        my_data_sources : DataSources, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.rigid_transformation()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> #or
        >>> op.inputs.data_sources(my_data_sources)

        """
        return self._data_sources

class OutputsRigidTransformation(_Outputs):
    """Intermediate class used to get outputs from rigid_transformation operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.rigid_transformation()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(rigid_transformation._spec().outputs, op)
        self._fields_container = Output(rigid_transformation._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.result.rigid_transformation()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

