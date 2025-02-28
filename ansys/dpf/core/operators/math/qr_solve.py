"""
qr_solve
========
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Math plugin, from "math" category
"""

class qr_solve(Operator):
    """computes the solution using QR factorization.

      available inputs:
        - fields_container (FieldsContainer)
        - rhs (FieldsContainer)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.qr_solve()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_rhs = dpf.FieldsContainer()
      >>> op.inputs.rhs.connect(my_rhs)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.qr_solve(fields_container=my_fields_container,rhs=my_rhs)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, rhs=None, config=None, server=None):
        super().__init__(name="qrsolveOp", config = config, server = server)
        self._inputs = InputsQrSolve(self)
        self._outputs = OutputsQrSolve(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if rhs !=None:
            self.inputs.rhs.connect(rhs)

    @staticmethod
    def _spec():
        spec = Specification(description="""computes the solution using QR factorization.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""fields_container"""), 
                                 1 : PinSpecification(name = "rhs", type_names=["fields_container"], optional=False, document="""fields_container""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "qrsolveOp")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsQrSolve 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsQrSolve 
        """
        return super().outputs


#internal name: qrsolveOp
#scripting name: qr_solve
class InputsQrSolve(_Inputs):
    """Intermediate class used to connect user inputs to qr_solve operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.qr_solve()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_rhs = dpf.FieldsContainer()
      >>> op.inputs.rhs.connect(my_rhs)
    """
    def __init__(self, op: Operator):
        super().__init__(qr_solve._spec().inputs, op)
        self._fields_container = Input(qr_solve._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._rhs = Input(qr_solve._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._rhs)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        - pindoc: fields_container

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.qr_solve()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def rhs(self):
        """Allows to connect rhs input to the operator

        - pindoc: fields_container

        Parameters
        ----------
        my_rhs : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.qr_solve()
        >>> op.inputs.rhs.connect(my_rhs)
        >>> #or
        >>> op.inputs.rhs(my_rhs)

        """
        return self._rhs

class OutputsQrSolve(_Outputs):
    """Intermediate class used to get outputs from qr_solve operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.qr_solve()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(qr_solve._spec().outputs, op)
        self._fields_container = Output(qr_solve._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.math.qr_solve()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

