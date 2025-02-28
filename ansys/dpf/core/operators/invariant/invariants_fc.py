"""
invariants_fc
=============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "invariant" category
"""

class invariants_fc(Operator):
    """Computes the element-wise invariants of all the tensor fields of a fields container.

      available inputs:
        - fields_container (FieldsContainer)

      available outputs:
        - fields_int (FieldsContainer)
        - fields_eqv (FieldsContainer)
        - fields_max_shear (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.invariant.invariants_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.invariant.invariants_fc(fields_container=my_fields_container)

      >>> # Get output data
      >>> result_fields_int = op.outputs.fields_int()
      >>> result_fields_eqv = op.outputs.fields_eqv()
      >>> result_fields_max_shear = op.outputs.fields_max_shear()"""
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="invariants_deriv_fc", config = config, server = server)
        self._inputs = InputsInvariantsFc(self)
        self._outputs = OutputsInvariantsFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the element-wise invariants of all the tensor fields of a fields container.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_int", type_names=["fields_container"], optional=False, document="""stress intensity field"""), 
                                 1 : PinSpecification(name = "fields_eqv", type_names=["fields_container"], optional=False, document="""stress equivalent intensity"""), 
                                 2 : PinSpecification(name = "fields_max_shear", type_names=["fields_container"], optional=False, document="""max shear stress field""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "invariants_deriv_fc")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsInvariantsFc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsInvariantsFc 
        """
        return super().outputs


#internal name: invariants_deriv_fc
#scripting name: invariants_fc
class InputsInvariantsFc(_Inputs):
    """Intermediate class used to connect user inputs to invariants_fc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.invariant.invariants_fc()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
    """
    def __init__(self, op: Operator):
        super().__init__(invariants_fc._spec().inputs, op)
        self._fields_container = Input(invariants_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.invariant.invariants_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

class OutputsInvariantsFc(_Outputs):
    """Intermediate class used to get outputs from invariants_fc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.invariant.invariants_fc()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_int = op.outputs.fields_int()
      >>> result_fields_eqv = op.outputs.fields_eqv()
      >>> result_fields_max_shear = op.outputs.fields_max_shear()
    """
    def __init__(self, op: Operator):
        super().__init__(invariants_fc._spec().outputs, op)
        self._fields_int = Output(invariants_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self._fields_int)
        self._fields_eqv = Output(invariants_fc._spec().output_pin(1), 1, op) 
        self._outputs.append(self._fields_eqv)
        self._fields_max_shear = Output(invariants_fc._spec().output_pin(2), 2, op) 
        self._outputs.append(self._fields_max_shear)

    @property
    def fields_int(self):
        """Allows to get fields_int output of the operator


        - pindoc: stress intensity field

        Returns
        ----------
        my_fields_int : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.invariant.invariants_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_int = op.outputs.fields_int() 
        """
        return self._fields_int

    @property
    def fields_eqv(self):
        """Allows to get fields_eqv output of the operator


        - pindoc: stress equivalent intensity

        Returns
        ----------
        my_fields_eqv : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.invariant.invariants_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_eqv = op.outputs.fields_eqv() 
        """
        return self._fields_eqv

    @property
    def fields_max_shear(self):
        """Allows to get fields_max_shear output of the operator


        - pindoc: max shear stress field

        Returns
        ----------
        my_fields_max_shear : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.invariant.invariants_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_max_shear = op.outputs.fields_max_shear() 
        """
        return self._fields_max_shear

