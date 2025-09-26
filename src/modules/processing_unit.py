import sys
import arthmetic_logic_unit as alu
import random_accsess_memory as ram
import moniter as sd
import harddrive as hdd
import stack as sp
import HEAP as h 











class CPU:
    def __init__ (self):
        self.ALU = alu.ALU()
        self.program_counter = '00000000000000'
        self.RAM = ram.RAM()
        self.Screen = sd.Screen()
        self.harddrive = hdd.harddrive()
        self.stack = sp.stack()
        self.running = True
        self.mode_bit = '0'
        self.Heap = h.HEAP()
        self.file_ID = '00000000'
        
        
        
        
    def run(self):  
        print('')
        print('')
        print('CPU HAS STARTED OPERATION')
        print('')
        print('')
        def decode(command):
            
                print('decoding')
                self.program_counter = format(int(self.program_counter, 2) + 1 , f'0{len(self.program_counter)}b')
                print('program counter encrmented')
            
            
                if command[0:4] == '1000':
                    print('arthmetic')
                    result = self.ALU.operate(command[4:10] , self.RAM.read(command[10:18]) , self.RAM.read(command[18:26]))
                    self.RAM.write(command[26:34] , result)
                    
                    
                elif command[0:4] == '0001':
                    print('ram write')
                    print(f' address = {command[4:12]}')
                    print(f' new value = {command[12:20]}')
                    
                    self.RAM.write(address=command[4:12] , new_value=command[12:20])
                    
                    
                elif command[0:4] == '0010':
                    print('showing screen')
                    self.Screen.show(size_w = self.RAM.read(command[4:12]) , size_l = self.RAM.read(command[12:20]) , binary_data = self.Heap.read(command[20:28]))
                
                
                
                elif command[0:4] == '0100':
                    x = command[18:]
                    print(f' x = {x}')
                    self.harddrive.write(address=command[4:18] , new_value=x)
                    print('writing to hardrive')


                elif command[0:4] == '1111' and command[4:8] == '1111':
                    print('system shutdown')
                    self.running = False
                    
                    
    
            
                      
                elif command[0:4] == '0011':
                    self.program_counter = command[4:18]
                    print(f'JUMP to {self.program_counter} has been excucteded ')
                
                elif command[0:4] == '0101':
                    opcode = command[4:8]
                    hd_address = command[8:22]
                    number_1 = self.RAM.read(address=command[22:30])
                    number_2 = self.RAM.read(address=command[30:38])
        
                    
                    self.ALU.operate(op_code='001001',operand1=number_1 , operand2=number_2)
                    if opcode == '0000':
                        if self.ALU.flags['Z'] == '1':
                            self.program_counter = hd_address
                    elif opcode == '0001':
                        if self.ALU.flags['N'] =='1':
                            self.program_counter = hd_address
                    elif opcode == '0010':
                        if self.ALU.flags['C'] == '1':
                            self.program_counter = hd_address
                    elif opcode == '0011':
                        if self.ALU.flags['Z'] == '0':
                            self.program_counter = hd_address
                    elif opcode == '0100':
                        if self.ALU.flags['N'] == '1' or self.ALU.flags['Z'] == "1":
                            self.program_counter = hd_address
                    elif opcode == '0101':
                        if self.ALU.flags['C'] == '1'or self.ALU.flags['Z'] == '1':
                            self.program_counter = hd_address
                            
                elif command[0:4] == '0110':
                    self.stack.PUSH(hd_address=self.program_counter)
                    self.program_counter = command[4:18]
                    print(f'CALL: jumping to {command[4:18]} from {self.program_counter}')
                    
                    
                elif command[0:4] == '0111':
                    self.program_counter = self.stack.POP()
                    print(f'RET: returning to {self.program_counter}')
                
                
                # sys call
                elif command[0:4] == '1010':
                    self.mode_bit = '1'
                    print('kernal mode actvited')
                    print('operating system has taken over')
                    self.stack.PUSH(hd_address=self.program_counter)
                    
                    if command[4:10] == '000000':
                        self.program_counter = '00000000000001'
                    elif command[4:10] == '000001':
                        self.program_counter = '00000000000011'
                    elif command[4:10] == '000010':
                        self.program_counter = '00000000000101'
                    elif command[4:10] == '000011':
                        self.program_counter = '00000000000111'# halt
                    elif command[4:10] == '000100':
                        self.program_counter = '00000000001001'
                        
                    elif command[4:10] == '000101':
                        self.program_counter = '00000000001011'
                        
                    elif command[4:10] == '000110':
                        self.program_counter = '00000000001101'
                        
                    elif command[4:10] == '000111':
                        self.program_counter = '00000000001111' # create a file 
                        
                    elif command[4:10] == '001000': 
                        
                        
                    # creating the file
                        print('creating file')
                        # getting the file contents
                        file_content = []
                        file_content.append(self.Heap.read(address='01100100'))# heap 100
                        file_content.append(self.Heap.read(address='01100101'))# heap 101
                        file_content.append(self.Heap.read(address='01100110'))# heap 102
                        file_content.append(self.Heap.read(address='01100111'))# heap 103
                        file_content.append(self.Heap.read(address='01101000'))# heap 104 
                        print(f'the file contents are : {file_content}')
                        
                        
                        # file ID 
                        
                        print(f'file ID is {self.file_ID}')
                        
                        
                        
                        
                        free_heap_address = []
                        bit_count = 0 
                        
                        for adderss, content in self.Heap.storage.items():
                        
                            if 151 <= int(adderss , 2) < 256 and content == '0' * 84:
                                free_heap_address.append(adderss)
                                bit_count += 1 
                                if bit_count == 3:
                                    break
                        print(f'free heap address are : {free_heap_address}')
                        heap_address1 = free_heap_address[0]
                        heap_adderss2 = free_heap_address[1]
                        heap_address3 = free_heap_address[2]
                        
                        
                        # find hardive address
                        free_hd_addres_list = []
                        hd_count = 0 
                        for hd_address , hd_content in self.harddrive.storage.items():
                            if 500 <= int(hd_address , 2) < 1000 and hd_content == '0'*84:
                                free_hd_addres_list.append(hd_address)
                                hd_count += 1 
                                print(bit_count)
                                if hd_count == 5 :
                                    break
                                
                        print(f'free harddrive address = {free_hd_addres_list}')
                        free_hd_address1 = free_hd_addres_list[0]
                        free_hd_address2 = free_hd_addres_list[1]
                        free_hd_address3 = free_hd_addres_list[2]
                        free_hd_address4 = free_hd_addres_list[3]
                        free_hd_address5 = free_hd_addres_list[4]
                        
                        
                        
                        
                        
                        
                        
                        self.Heap.write(address=heap_address1 , new_value=self.file_ID)# write file code to heap
                        
                        self.file_ID = format(int(self.file_ID , 2 ) + 1  ,f'0{len(self.file_ID)}b' )# increment the file code for the next file 
                        print(f'new file code = {self.file_ID}')
                        
                        
                        
                        self.Heap.write(address=heap_adderss2 , new_value=free_hd_address1)
                        self.Heap.write(address=heap_address3 , new_value=free_hd_address5)
                        
                        file_content1 = file_content[0]
                        file_content2 = file_content[1]
                        file_content3 = file_content[2]
                        file_content4 = file_content[3]
                        file_content5 = file_content[4]
                        
                        self.harddrive.write(address=free_hd_address1  ,  new_value=file_content1)
                        self.harddrive.write(address=free_hd_address2  ,  new_value=file_content2)
                        self.harddrive.write(address=free_hd_address3  ,  new_value=file_content3)
                        self.harddrive.write(address=free_hd_address4  ,  new_value=file_content4)
                        self.harddrive.write(address=free_hd_address5  ,  new_value=file_content5)
                        
                        # update bitmap
                            
                        print('updating bitmap')
                        for address , content in self.RAM.storage.items():
                            
                            if 191 <= int(address , 2) < 256:# 191 - 256
                                print(f'address = {address}')
                                print(f'content = {content}')
                                bit_count = 0 
                                new_content = ''
                                for bit in content:
                                    print(f'bit = {bit}')
                                    
                                    if bit == '0' and bit_count < 3 :
                                        new_content = new_content + '1'
                                        bit_count += 1 
                                        print('new 1 bit has been')
                                        
                                    else: 
                                        new_content = new_content + bit
                                if len(new_content) == 8 :
                                    self.RAM.storage[address] = new_content
                                    break
                                print(f'new content = {new_content}')
                    
                    elif command[4:10] == '001001':  # create a new process id
                        self.program_counter = '00000000010001'
                        
                    elif command[4:10] == '001010': # copy address 1 to address 2 in ram 
                        RAM_address_1 = self.Heap.read(address='00001010') # the address to copy from is written to heap[10]
                        RAM_address_2 = self.Heap.read(address='00001011') # the address to copy to is written to heap[11]
                        
                        content_to_write = self.RAM.read(address=RAM_address_1)
                        self.RAM.write(address=RAM_address_2 , new_value=content_to_write)
                        
                    elif command[4:10] == '001011': # COPY_H_H
                        print('SYS_CALL 001011 has been called (COPY_H_H)')
                        heap_address1 = self.Heap.read(address='00001000')
                        heap_adderss2 = self.Heap.read(address='00001001')
                        
                        print(f'heap address1 = {heap_address1}')
                        print(f'heap address2 = {heap_adderss2}')

                        
                        content_to_write = self.Heap.read(address=heap_address1)
                        print(f'the content to write = {content_to_write}')
                        self.Heap.write(address=heap_adderss2 , new_value=content_to_write)
                    
                    elif command[4:10] == '001100':
                        self.program_counter = '00000000010100'
                    
                    elif command[4:10] == '001101':
                        self.program_counter = '00000000011011'
                    
                    elif command[4:10] == '001110':
                        self.program_counter = '00000000011011'
                        
                    elif command[4:10] == '001111':
                        self.program_counter = '00000000101001'
                    elif command[4:10] == '010000':
                        print('writing process id ')
                        heap_address1 = self.Heap.read(address='00000000')
                        heap_adderss2 = self.Heap.read(address='00000001')
                        heap_address3 = self.Heap.read(address='00000010')
                        opcode = self.Heap.read(address='00000011')  
                        oprand1 = self.Heap.read(address=heap_address1)   
                        oprand2 = self.Heap.read(address=heap_adderss2)
                        
                        result = self.ALU.operate(op_code=opcode , operand1=oprand1,operand2=oprand2)
                        self.Heap.write(address=heap_address3 , new_value=result)                   
                        
                                                
                            
                        
                        
                                            
                                        
                                
                                
                                 
                        
                        
                        
                                
                                 
                            
                                
                                
                                
                            
                        
                        
                    
                    
                    
                elif command[0:4] == '1011':
                    print('user mode actvited')
                    print('returning to application')
                    self.program_counter = self.stack.POP()
                
                elif command[0:4] == '1100':
                    print('writing to heap')
                    adderss = command[4:12]
                    new_value = command[12:]
                    self.Heap.write(adderss , new_value)   
                
                
                
                
                
                
                elif command[0:4] == '1101':
                    print('copying from meap to ram')
                    hd_address = self.Heap.read(address=command[4:12])
                    print(hd_address)
                    new_value = self.Heap.read(address=command[12:])
                    print(new_value)
                    self.harddrive.write(address=hd_address,new_value=new_value)
                
                
                
                
                
                
                
                
                
                        
                else:
                    print(f"Unknown instruction: {command[0:4]}")
                    self.running = False        
                
                    
                
        cycle_count = 0   
        while self.running == True:
            command = self.harddrive.read(address=self.program_counter)
            
            print(f'program couter equal = {self.program_counter}')
            print(f'decimal program counter = {int(self.program_counter , 2) }')
            print(f'stack pointer = {self.stack.stack_pointer}')
            print(f'command={command}')
            
            
            
            if len(self.program_counter) == 14:
                decode(command=command)
                
            else:
                self.program_counter ='1' * 14
                
            if self.program_counter == '00000111110011':
                self.running = False
            cycle_count +=1
            print(f'cycles excucted = {cycle_count}')
            print('')
            print('')
            print('')
            print('')
    def show_harddrive(self):
        print('showing harddrive')
        self.harddrive.visualize()
    def show_RAM(self):
        print('showing RAM')
        self.RAM.visualize()
    def show_heap(self):
        print('showing heap')
        self.Heap.visualize()
    def show_stack(self):
        print('showing stack')
        print(f'stack pointer = {self.stack.stack_pointer}')
        self.stack.visualize()