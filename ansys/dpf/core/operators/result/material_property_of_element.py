"""
material_property_of_element
============================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "result" category
"""

class material_property_of_element(Operator):
    """ Load the appropriate operator based on the data sources and get material properties

      available inputs:
        - streams_container (StreamsContainer) (optional)
        - data_sources (DataSources)

      available outputs:
        - material_properties (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.result.material_property_of_element()

      >>> # Make input connections
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.result.material_property_of_element(streams_container=my_streams_container,data_sources=my_data_sources)

      >>> # Get output data
      >>> result_material_properties = op.outputs.material_properties()"""
    def __init__(self, streams_container=None, data_sources=None, config=None, server=None):
        super().__init__(name="MaterialPropertyOfElement", config = config, server = server)
        self._inputs = InputsMaterialPropertyOfElement(self)
        self._outputs = OutputsMaterialPropertyOfElement(self)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description=""" Load the appropriate operator based on the data sources and get material properties""",
                             map_input_pin_spec={
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document=""""""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "material_properties", type_names=["field"], optional=False, document="""material properties""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "MaterialPropertyOfElement")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMaterialPropertyOfElement 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMaterialPropertyOfElement 
        """
        return super().outputs


#internal name: MaterialPropertyOfElement
#scripting name: material_property_of_element
class InputsMaterialPropertyOfElement(_Inputs):
    """Intermediate class used to connect user inputs to material_property_of_element operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.material_property_of_element()
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
    """
    def __init__(self, op: Operator):
        super().__init__(material_property_of_element._spec().inputs, op)
        self._streams_container = Input(material_property_of_element._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._streams_container)
        self._data_sources = Input(material_property_of_element._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._data_sources)

    @property
    def streams_container(self):
        """Allows to connect streams_container input to the operator

        Parameters
        ----------
        my_streams_container : StreamsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.material_property_of_element()
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

        >>> op = dpf.operators.result.material_property_of_element()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> #or
        >>> op.inputs.data_sources(my_data_sources)

        """
        return self._data_sources

class OutputsMaterialPropertyOfElement(_Outputs):
    """Intermediate class used to get outputs from material_property_of_element operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.material_property_of_element()
      >>> # Connect inputs : op.inputs. ...
      >>> result_material_properties = op.outputs.material_properties()
    """
    def __init__(self, op: Operator):
        super().__init__(material_property_of_element._spec().outputs, op)
        self._material_properties = Output(material_property_of_element._spec().output_pin(0), 0, op) 
        self._outputs.append(self._material_properties)

    @property
    def material_properties(self):
        """Allows to get material_properties output of the operator


        - pindoc: material properties

        Returns
        ----------
        my_material_properties : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.material_property_of_element()
        >>> # Connect inputs : op.inputs. ...
        >>> result_material_properties = op.outputs.material_properties() 
        """
        return self._material_properties

