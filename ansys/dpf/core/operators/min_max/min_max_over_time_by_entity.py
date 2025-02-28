"""
min_max_over_time_by_entity
===========================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "min_max" category
"""

class min_max_over_time_by_entity(Operator):
    """Evaluates minimum, maximum over time/frequency and returns those min max as well as the time/freq where they occured

      available inputs:
        - fields_container (FieldsContainer)
        - compute_amplitude (bool) (optional)

      available outputs:
        - min (FieldsContainer)
        - max (FieldsContainer)
        - time_freq_of_min (FieldsContainer)
        - time_freq_of_max (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.min_max.min_max_over_time_by_entity()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_compute_amplitude = bool()
      >>> op.inputs.compute_amplitude.connect(my_compute_amplitude)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.min_max.min_max_over_time_by_entity(fields_container=my_fields_container,compute_amplitude=my_compute_amplitude)

      >>> # Get output data
      >>> result_min = op.outputs.min()
      >>> result_max = op.outputs.max()
      >>> result_time_freq_of_min = op.outputs.time_freq_of_min()
      >>> result_time_freq_of_max = op.outputs.time_freq_of_max()"""
    def __init__(self, fields_container=None, compute_amplitude=None, config=None, server=None):
        super().__init__(name="min_max_over_time_by_entity", config = config, server = server)
        self._inputs = InputsMinMaxOverTimeByEntity(self)
        self._outputs = OutputsMinMaxOverTimeByEntity(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if compute_amplitude !=None:
            self.inputs.compute_amplitude.connect(compute_amplitude)

    @staticmethod
    def _spec():
        spec = Specification(description="""Evaluates minimum, maximum over time/frequency and returns those min max as well as the time/freq where they occured""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 4 : PinSpecification(name = "compute_amplitude", type_names=["bool"], optional=True, document="""Do calculate amplitude.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "min", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "max", type_names=["fields_container"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "time_freq_of_min", type_names=["fields_container"], optional=False, document=""""""), 
                                 3 : PinSpecification(name = "time_freq_of_max", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "min_max_over_time_by_entity")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMinMaxOverTimeByEntity 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMinMaxOverTimeByEntity 
        """
        return super().outputs


#internal name: min_max_over_time_by_entity
#scripting name: min_max_over_time_by_entity
class InputsMinMaxOverTimeByEntity(_Inputs):
    """Intermediate class used to connect user inputs to min_max_over_time_by_entity operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.min_max.min_max_over_time_by_entity()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_compute_amplitude = bool()
      >>> op.inputs.compute_amplitude.connect(my_compute_amplitude)
    """
    def __init__(self, op: Operator):
        super().__init__(min_max_over_time_by_entity._spec().inputs, op)
        self._fields_container = Input(min_max_over_time_by_entity._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._compute_amplitude = Input(min_max_over_time_by_entity._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._compute_amplitude)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.min_max.min_max_over_time_by_entity()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def compute_amplitude(self):
        """Allows to connect compute_amplitude input to the operator

        - pindoc: Do calculate amplitude.

        Parameters
        ----------
        my_compute_amplitude : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.min_max.min_max_over_time_by_entity()
        >>> op.inputs.compute_amplitude.connect(my_compute_amplitude)
        >>> #or
        >>> op.inputs.compute_amplitude(my_compute_amplitude)

        """
        return self._compute_amplitude

class OutputsMinMaxOverTimeByEntity(_Outputs):
    """Intermediate class used to get outputs from min_max_over_time_by_entity operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.min_max.min_max_over_time_by_entity()
      >>> # Connect inputs : op.inputs. ...
      >>> result_min = op.outputs.min()
      >>> result_max = op.outputs.max()
      >>> result_time_freq_of_min = op.outputs.time_freq_of_min()
      >>> result_time_freq_of_max = op.outputs.time_freq_of_max()
    """
    def __init__(self, op: Operator):
        super().__init__(min_max_over_time_by_entity._spec().outputs, op)
        self._min = Output(min_max_over_time_by_entity._spec().output_pin(0), 0, op) 
        self._outputs.append(self._min)
        self._max = Output(min_max_over_time_by_entity._spec().output_pin(1), 1, op) 
        self._outputs.append(self._max)
        self._time_freq_of_min = Output(min_max_over_time_by_entity._spec().output_pin(2), 2, op) 
        self._outputs.append(self._time_freq_of_min)
        self._time_freq_of_max = Output(min_max_over_time_by_entity._spec().output_pin(3), 3, op) 
        self._outputs.append(self._time_freq_of_max)

    @property
    def min(self):
        """Allows to get min output of the operator


        Returns
        ----------
        my_min : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.min_max.min_max_over_time_by_entity()
        >>> # Connect inputs : op.inputs. ...
        >>> result_min = op.outputs.min() 
        """
        return self._min

    @property
    def max(self):
        """Allows to get max output of the operator


        Returns
        ----------
        my_max : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.min_max.min_max_over_time_by_entity()
        >>> # Connect inputs : op.inputs. ...
        >>> result_max = op.outputs.max() 
        """
        return self._max

    @property
    def time_freq_of_min(self):
        """Allows to get time_freq_of_min output of the operator


        Returns
        ----------
        my_time_freq_of_min : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.min_max.min_max_over_time_by_entity()
        >>> # Connect inputs : op.inputs. ...
        >>> result_time_freq_of_min = op.outputs.time_freq_of_min() 
        """
        return self._time_freq_of_min

    @property
    def time_freq_of_max(self):
        """Allows to get time_freq_of_max output of the operator


        Returns
        ----------
        my_time_freq_of_max : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.min_max.min_max_over_time_by_entity()
        >>> # Connect inputs : op.inputs. ...
        >>> result_time_freq_of_max = op.outputs.time_freq_of_max() 
        """
        return self._time_freq_of_max

