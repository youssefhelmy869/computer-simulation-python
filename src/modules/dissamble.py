class ModeError(Exception):
    pass
class Disassembler:
    def __init__(self):
        self.mode_bit = '1'
        self.binary_code = []
        self.assembly_code = []

    def load_program(self, machine_code):
        print('Loading binary instructions into disassembler...')
        for instruction in machine_code:
            self.binary_code.append(instruction)
            print(f'Binary command {instruction} has been loaded.')

    def disassemble(self):
        for inst in self.binary_code:
            opcode = inst[:4]
            asm_command = ""

            if opcode == '1000':  # ARTH
                op = inst[4]
                addr1 = int(inst[5:13], 2)
                addr2 = int(inst[13:21], 2)
                addr3 = int(inst[21:29], 2)
                asm_command = f'ARTH {op} {addr1} {addr2} {addr3}'

            elif opcode == '1010':  # SYS_CALL
                self.mode_bit = '1'
                print('Kernel mode activated')
                syscall_code = inst[4:10]  # Use 6 bits for syscall code
                asm_command = f'SYS_CALL {syscall_code}'

            elif opcode == '1011':  # APP_CALL
                self.mode_bit = '0'
                print('User mode activated')
                asm_command = 'APP_CALL'

            elif opcode == '0100':  # WRITE_HD
                if self.mode_bit == '0':
                    raise ModeError('WRITE_HD instruction found in user mode')
                hd_addr = int(inst[4:18], 2)
                data = inst[18:]
                asm_command = f'WRITE_HD {hd_addr} {data}'

            elif opcode == '0111':  # RET
                asm_command = 'RET'

            elif opcode == '0110':  # CALL
                address = int(inst[4:18], 2)
                asm_command = f'CALL {address}'

            elif opcode == '0101':  # JUMP_IF
                condition = inst[4]
                hd_addr = int(inst[5:19], 2)
                addr1 = int(inst[19:27], 2)
                addr2 = int(inst[27:35], 2)
                asm_command = f'JUMP_IF {condition} {hd_addr} {addr1} {addr2}'

            elif opcode == '0011':  # JUMP
                address = int(inst[4:18], 2)
                asm_command = f'JUMP {address}'

            elif opcode == '0001':  # WRITE_RAM
                addr = int(inst[4:12], 2)
                data = inst[12:]
                asm_command = f'WRITE_RAM {addr} {data}'

            elif opcode == '0010':  # SHOW
                addr1 = int(inst[4:12], 2)
                addr2 = int(inst[12:20], 2)
                addr3 = int(inst[20:28], 2)
                asm_command = f'SHOW {addr1} {addr2} {addr3}'

            elif inst == '11111111':  # HALT
                asm_command = 'HALT'

            elif opcode == '1100':  # WRITE_HEAP
                addr = int(inst[4:12], 2)
                data = inst[12:]
                asm_command = f'WRITE_HEAP {addr} {data}'

            elif opcode == '1101':  # MOVE_H_HD
                addr1 = int(inst[4:12], 2)
                addr2 = int(inst[12:20], 2)
                asm_command = f'MOVE_H_HD {addr1} {addr2}'

            elif inst == '1010001000':  # CREATE_FILE
                asm_command = 'CREATE_FILE'

            elif inst == '1010001010':  # COPY_R_R
                asm_command = 'COPY_R_R'

            elif inst == '1010001011':  # COPY_H_H
                asm_command = 'COPY_H_H'

            else:
                asm_command = f'UNKNOWN_COMMAND {inst}'

            self.assembly_code.append(asm_command)
            print(asm_command)

        return self.assembly_code
    def Empty(self):
        self.assembly_code =[]
        self.binary_code = []
x = Disassembler()
machine_code = ['11000000110011111111', '1010001001', '1010001100']
x.load_program(machine_code=machine_code)
assembly = x.disassemble()
count = 0 
for asm in assembly:
    count += 1
    print(f'command {count} = {asm}')
    
