class MYError(Exception):
    pass

def AND(x , y ):

    
    if x and y == 1:
        return 1
    else:
        return 0 
def OR(x,y):

    if x or y == 1 :
        return 1 
    else:
        return 0 
def XOR(x , y):
    if x != y :
        return 1 
    else:
        return 0 
def NOT(x):
    if x == 0 :
        return 1 
    else:
        return 0
def NAND(x,y):
    if x and y == 1 :
        return 0 
    else:
        return 1 
def NOR(x,y):
    if x and y == 0:
        return 1 
    else:
        return 0 
    
def half_adder(x,y):
    sum = XOR(x,y)
    carry = AND(x,y)
    return sum ,carry
def adder(x,y,carry):
    sum1 = XOR(x,y)
    sum_bit = XOR(sum1 , carry)
    carry1 = AND(x, y)
    carry2 = AND(sum1, carry)
    carry_out = OR(carry1, carry2)
    return sum_bit, carry_out

class ALU:
    def __init__(self):
        # Add flags dictionary
        self.flags = {
            'Z': 0,  # Zero flag
            'C': 0,  # Carry flag
            'N': 0,  # Negative flag
            'O': 0   # Overflow flag
        }

    def _update_flags(self, result, carry=None, overflow=None):
        # Set Zero flag
        self.flags['Z'] = bin(int(result == 0))[2:]
        # Set Negative flag (for 8-bit signed)
        self.flags['N'] = bin(int((result & 0x80) != 0))[2:]
        # Set Carry flag if provided
        if carry is not None:
            self.flags['C'] = bin(int(carry))[2:]
        else:
            self.flags['C'] = "0"
        # Set Overflow flag if provided
        if overflow is not None:
            self.flags['O'] = bin(int(overflow))[2:]
        else:
            self.flags['O'] = "0"

    def operate(self, op_code, operand1, operand2):
        # Ensure the operation code is 6 bits
        # Notes: The operation code must always be a 6-bit binary string. If it is not exactly 6 bits, the function will raise an error.
        if len(op_code) != 6:
            print(f'opcode = {op_code}')
            raise MYError("Operation code must be 6 bits")
        if len(operand1) != 8 or len(operand2) != 8:
            print(f'op 1 = {operand1}')
            print(f'op 2 = {operand2}')
            raise MYError("Each operand must be 8 bits")

        # Convert binary string inputs to integers
        operand1 = int(operand1, 2)
        operand2 = int(operand2, 2)

        # Perform the operation
        if op_code == "000000":  # AND
            result = AND(operand1, operand2)
            self._update_flags(result)
        elif op_code == "000001":  # OR
            result = OR(operand1, operand2)
            self._update_flags(result)
        elif op_code == "000010":  # XOR
            result = XOR(operand1, operand2)
            self._update_flags(result)
        elif op_code == "000011":  # NOT (unary)
            result = NOT(operand1)
            self._update_flags(result)
        elif op_code == "000100":  # NAND
            result = NAND(operand1, operand2)
            self._update_flags(result)
        elif op_code == "000101":  # NOR
            result = NOR(operand1, operand2)
            self._update_flags(result)
        elif op_code == "000110":  # HALF_ADDER
            sum_bit, carry = half_adder(operand1, operand2)
            self._update_flags(sum_bit, carry=carry)
            return bin(sum_bit)[2:].zfill(8), bin(carry)[2:].zfill(1)
        elif op_code == "000111":  # ADDER
            sum_bit, carry_out = adder(operand1, operand2, 0)
            self._update_flags(sum_bit, carry=carry_out)
            return bin(sum_bit)[2:].zfill(8), bin(carry_out)[2:].zfill(1)
        elif op_code == "001000":  # ADD
            result = operand1 + operand2
            carry = int(result > 0xFF)
            overflow = int(((operand1 ^ result) & (operand2 ^ result) & 0x80) != 0)
            result &= 0xFF
            print('ADD has been done')
            self._update_flags(result, carry=carry, overflow=overflow)
        elif op_code == "001001":  # SUB
            result = operand1 - operand2
            carry = int(operand1 >= operand2)
            overflow = int(((operand1 ^ operand2) & (operand1 ^ result) & 0x80) != 0)
            result &= 0xFF
            self._update_flags(result, carry=carry, overflow=overflow)
        elif op_code == "001010":  # MUL
            result = operand1 * operand2
            carry = int(result > 0xFF)
            result &= 0xFF
            self._update_flags(result, carry=carry)
        elif op_code == "001011":  # DIV
            if operand2 == 0:
                raise MYError("Division by zero")
            result = operand1 // operand2
            self._update_flags(result)
        elif op_code == "001100":  # MOD
            if operand2 == 0:
                raise MYError("Modulo by zero")
            result = operand1 % operand2
            self._update_flags(result)
        elif op_code == "001101":  # POW
            result = operand1 ** operand2
            carry = int(result > 0xFF)
            result &= 0xFF
            self._update_flags(result, carry=carry)
        elif op_code == "001110":  # INC (unary)
            result = operand1 + 1
            carry = int(result > 0xFF)
            result &= 0xFF
            self._update_flags(result, carry=carry)
        elif op_code == "001111":  # DEC (unary)
            result = operand1 - 1
            carry = int(result < 0)
            result &= 0xFF
            self._update_flags(result, carry=carry)
        elif op_code == "010000":  # SHL
            result = operand1 << operand2
            carry = int((result & 0x100) != 0)
            result &= 0xFF
            self._update_flags(result, carry=carry)
        elif op_code == "010001":  # SHR
            carry = int((operand1 >> (operand2 - 1)) & 1 if operand2 > 0 else 0)
            result = operand1 >> operand2
            self._update_flags(result, carry=carry)
        elif op_code == "010010":  # BIT_AND
            result = operand1 & operand2
            self._update_flags(result)
        elif op_code == "010011":  # BIT_OR
            result = operand1 | operand2
            self._update_flags(result)
        elif op_code == "010100":  # BIT_XOR
            result = operand1 ^ operand2
            self._update_flags(result)
        elif op_code == "010101":  # BIT_NOT (unary)
            result = ~operand1 & 0xFF
            self._update_flags(result)
        elif op_code == "010110":  # EQ
            result = int(operand1 == operand2)
            self._update_flags(result)
        elif op_code == "010111":  # NEQ
            result = int(operand1 != operand2)
            self._update_flags(result)
        elif op_code == "011000":  # GT
            result = int(operand1 > operand2)
            self._update_flags(result)
        elif op_code == "011001":  # LT
            result = int(operand1 < operand2)
            self._update_flags(result)
        elif op_code == "011010":  # GTE
            result = int(operand1 >= operand2)
            self._update_flags(result)
        elif op_code == "011011":  # LTE
            result = int(operand1 <= operand2)
            self._update_flags(result)
        elif op_code == "011100":  # MIN
            result = min(operand1, operand2)
            self._update_flags(result)
        elif op_code == "011101":  # MAX
            result = max(operand1, operand2)
            self._update_flags(result)
        elif op_code == "011110":  # ABS (unary)
            result = abs(operand1)
            self._update_flags(result)
        elif op_code == "011111":  # NEG (unary)
            result = (-operand1) & 0xFF
            self._update_flags(result)
        else:
            raise MYError("Unknown ALU operation")

        # Convert the result back to a binary string
        return bin(result)[2:].zfill(8)

        # Binary operation table:
        # 1.000000: AND - Logical AND operation
        # 2.000001: OR - Logical OR operation
        # 3.000010: XOR - Logical XOR operation
        # 4.000011: NOT - Logical NOT operation (unary)
        # 5.000100: NAND - Logical NAND operation
        # 000101: NOR - Logical NOR operation
        # 000110: HALF_ADDER - Computes sum and carry using half-adder
        # 000111: ADDER - Computes sum and carry-out using full adder
        # 001000: ADD - Adds two binary inputs
        # 001001: SUB - Subtracts second binary input from the first
        # 001010: MUL - Multiplies two binary inputs
        # 001011: DIV - Divides first binary input by the second
        # 001100: MOD - Computes modulo of first input by the second
        # 001101: POW - Raises first binary input to the power of the second
        # 001110: INC - Increments a single binary input (unary)
        # 001111: DEC - Decrements a single binary input (unary)
        # 010000: SHL - Bitwise shift left operation
        # 010001: SHR - Bitwise shift right operation
        # 010010: BIT_AND - Bitwise AND operation
        # 010011: BIT_OR - Bitwise OR operation
        # 010100: BIT_XOR - Bitwise XOR operation
        # 010101: BIT_NOT - Bitwise NOT operation (unary)
        # 010110: EQ - Checks if two inputs are equal
        # 010111: NEQ - Checks if two inputs are not equal
        # 011000: GT - Checks if first input is greater than the second
        # 011001: LT - Checks if first input is less than the second
        # 011010: GTE - Checks if first input is greater than or equal to the second
        # 011011: LTE - Checks if first input is less than or equal to the second
        # 011100: MIN - Returns the smaller of two inputs
        # 011101: MAX - Returns the larger of two inputs
        # 011110: ABS - Returns the absolute value of a single input (unary)
        # 011111: NEG - Negates a single input (unary)