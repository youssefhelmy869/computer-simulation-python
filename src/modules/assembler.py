import processing_unit as c
import sys 


class ModeError(Exception):
    pass
class UnKnownCommand(Exception):
    pass
class Assembler():
    def __init__(self):
        self.mode_bit = '0'
        self.assembly_code = []
        self.machine_code =[]
        self.lines_done =0 
        
    def load_program_into_Assembler(self , program_code):
        print('loading instructin into assembler')
        for instrusction in program_code:
            self.assembly_code.append(instrusction)
            print(f'command {instrusction} has been loaded into assembler')
    def assemble(self):
        for inst in self.assembly_code:
            commands = inst.split()
            binary_command = ''
            
            if commands[0] == 'ARTH':
                binary_command = binary_command + '1000'
                binary_command = binary_command + commands[1]
                RAM_address1 = format(int(commands[2]) , '08b')
                RAM_address2 = format(int(commands[3]) , '08b')
                RAM_address3 = format(int(commands[4]) , '08b')
                binary_command = binary_command + RAM_address1
                binary_command = binary_command + RAM_address2
                binary_command = binary_command + RAM_address3
                
            elif commands[0] == 'SYS_CALL':
                self.mode_bit = '1'
                print('kernal mode actvited')
                binary_command = '1010'
                binary_command = binary_command + commands[1]
                
            elif commands[0] == 'APP_CALL':
                self.mode_bit = '0'
                print('user mode actvited')
                binary_command = '1011'
                
                
            elif commands[0] == 'WRITE_HD':
                if self.mode_bit == '0':
                    raise ModeError('WRITE_HD instruction has been has envoked while in user mode')
                    sys.exit()
                    
                else:
                    hd_address = format(int(commands[1]) , '014b')
                    binary_command = binary_command + '0100'
                    binary_command = binary_command + hd_address
                    binary_command = binary_command = commands[2]
                    
            elif commands[0] == 'RET':
                binary_command = '0111'
                
            elif commands[0] == 'CALL':
                binary_command = '0110'
                binary_command = binary_command + format(int(commands[1]), '014b')
                
            elif commands[0] == 'JUMP_IF':
                binary_command = '0101'
                binary_command = binary_command + commands[1] # opcode
                hd_address = format(int(commands[2]) , '014b')
                RAM_address1 = format(int(commands[3]) , '08b')
                RAM_address2 = format(int(commands[4]), '08b')
                print(f'hd address = {hd_address}')
                print(f'RAM address 1  = {RAM_address1}')
                print(f'RAM address 2 = {RAM_address2}')
                binary_command = binary_command + hd_address
                binary_command = binary_command + RAM_address1
                binary_command = binary_command + RAM_address2 
            
            elif commands[0] == 'JUMP':
                binary_command = '0011'
                binary_command = binary_command + format(int(commands[1]) , '014b')
            
            elif commands[0] == 'WRITE_RAM':
                binary_command = '0001'
                binary_command = binary_command + format(int(commands[1]) , '08b')
                binary_command = binary_command + commands[2]
                
            elif commands[0] == 'SHOW':
                    binary_command = '0010'
                    binary_command = binary_command + format(int(commands[1]) ,'08b')
                    binary_command = binary_command + format(int(commands[2]) ,'08b')
                    binary_command = binary_command + format(int(commands[3])  ,'08b')
                    
            elif commands[0] == 'HALT':
                print('HALT has been envoked')
                
                binary_command = '11111111'   
            elif commands[0] == 'WRITE_HEAP':
                binary_command = '1100'
                binary_command = binary_command + format(int(commands[1]) , '08b')
                binary_command = binary_command + commands[2]
                
            elif commands[0] == 'MOVE_H_HD':
                binary_command = '1101'
                binary_command = binary_command + format(int(commands[1]) , '08b')
                binary_command = binary_command + format(int(commands[2]) , '08b')
                
            elif commands[0] == 'CREATE_FILE':
                binary_command = '1010001000'
                
            elif commands[0] == 'COPY_R_R':   # copy from RAM to RAM
                binary_command = '1010001010'
            
            elif commands[0] == 'COPY_H_H':
                binary_command = '1010001011'
                
            else:
                count = 0 
                for command in commands:
                    count += 1 
                    print(f'command {count} = {command}')
                raise UnKnownCommand('SYNTAX ERROR false commands')
                
            self.lines_done += 1
            print(f'lines assembled = {self.lines_done}')        
            self.machine_code.append(binary_command)
            print(binary_command)
            print('Done')
            
            
        return self.machine_code
    def Empty(self):
        self.assembly_code =[]
        self.machine_code = []          



