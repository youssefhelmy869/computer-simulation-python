import processing_unit as c
import assembler as a


cpu = c.CPU()
assembler = a.Assembler()

os = ['JUMP 169' , # operatins system call will only be from hd[0] - hd[49] applictions will start from hd[50] and mode_bit will start at 0 
      # func to from the operating system to write the harddrive the aplliction must first write to address to the address the heap 5 or 7 or 9 and the info 
      #6 or 8 or 10 
      # (HEAP ADDRESS) FIRST ADDRESS THEN INFO
      
      
      
      'MOVE_H_HD 5 6' , # SYS_CALL 000000 address = 00000000000001
      'APP_CALL',
      'MOVE_H_HD 7 8' , # SYS_CALL 000001 address = 00000000000011
      'APP_CALL' , 
      'MOVE_H_HD 9 10', # SYS_CALL 000010 address = 00000000000101
      'APP_CALL',
      'HALT',           # SYS_CALL 000011 address = 00000000000111
      'APP_CALL',
      
      
      #     r  r h  first 2 are RAM address while the third is a heap address
      
      'SHOW 11 12 13' , # SYS_CALL 000100                 ||| address = 00000000001001
      'APP_CALL' , 
      'SHOW 14 15 16' , # SYS_CALL 000101                     address = 00000000001011
      'APP_CALL' , 
      'SHOW 17 18 19' , # SYS_CALL 000110                     address = 00000000001101
      'APP_CALL' ,
      'CREATE_FILE' , # SYS_CALL 000111                       address = 00000000001111
      'APP_CALL' , 
      # create new process ID  SYS_CALL 001001
      
      'SYS_CALL 010000', # INCREMENT THE PROCESS ID      ADDRESS = 00000000010001
      'WRITE_HEAP 7 00011001', #write to heap[7] address 25|  ADDRESS = 00000000010010
      'APP_CALL',                                            #ADDRESS = 00000000010011 
      # the appliction must write to heap[12] the allocated memory address space pointer
      # SYS_CALL 001100 (TO CREATE PROCCESS 1 )
      'WRITE_HEAP 8 00011001',  # copy from heap[25]          address = 00000000010100
      'WRITE_HEAP 9 00011110',  # to heap [30]                address = 00000000010101
      'COPY_H_H',               #                             address = 00000000010110
      'WRITE_HEAP 8 00001100',  # COPY FROM HEAP[12]          address = 00000000010111
      'WRITE_HEAP 9 00011111',  # TO HEAP[31]                 address = 00000000011000
      'COPY_H_H',               #                             address = 00000000011001
      'APP_CALL',               #                             address = 00000000011010
      # SYS_CALL 001101
      'WRITE_HEAP 8 00011001' , # copy heap[25](process id)   address = 00000000011011
      'WRITE_HEAP 9 00100000' , # to heap [32]                address = 00000000011100
      'COPY_H_H' ,              #                             address = 00000000011101
      'WRITE_HEAP 8 00001100',  # heap[12]                    address = 00000000011110
      'WRITE_HEAP 9 00100001',  # heap[33]                    address = 00000000011111
      'COPY_H_H',               #                             address = 00000000010000
      'APP_CALL',               #                             address = 00000000010001
      # SYS_CALL 001110
      'WRITE_HEAP 8 00011001', # copy heap[25](process id)   address = 00000000100010
      'WRITE_HEAP 9 00100010', # to heap [34]                address = 00000000100011
      'COPY_H_H',              #                             address = 00000000100100
      'WRITE_HEAP 8 00001100', # heap[12]                    address = 00000000100101
      'WRITE_HEAP 9 00100011', # heap[35]                    address = 00000000100110
      'COPY_H_H',              #                             address = 00000000100111
      'APP_CALL',              #                             address = 00000000101000     
      # sys_call 001111
      'WRITE_HEAP 8 00011001', # copy heap[25](process id)   address = 00000000101001
      'WRITE_HEAP 9 00100100', # to heap [36]                address = 00000000101010
      'COPY_H_H',              #                             address = 00000000101011
      'WRITE_HEAP 8 00001100', # heap[12]                    address = 00000000101100
      'WRITE_HEAP 9 00100101', # heap[37]                    address = 00000000101101
      'COPY_H_H',              #                             address = 00000000101110
      'APP_CALL',              #                             address = 00000000101111
      
      # ALLOCATE MEMORY FOR THE PROCESS(ALLOC)
      # ALLOC_1 from heap[70 - 99] to harddrive[200 - 229]
      'WRITE_HEAP 4 00000011001000',
      'MOVE_H_HD 4 70',
      'WRITE_HEAP 4 00000011001001',
      'MOVE_H_HD 4 71',
      'WRITE_HEAP 4 00000011001010',
      'MOVE_H_HD 4 72',
      'WRITE_HEAP 4 00000011001011',
      'MOVE_H_HD 4 73',
      'WRITE_HEAP 4 00000011001100',
      'MOVE_H_HD 4 74',
      'WRITE_HEAP 4 00000011001101',
      'MOVE_H_HD 4 75',
      'WRITE_HEAP 4 00000011001110',
      'MOVE_H_HD 4 76',
      'WRITE_HEAP 4 00000011001111',
      'MOVE_H_HD 4 77', 
      'WRITE_HEAP 4 00000011010000',
      'MOVE_H_HD 4 78',
      'WRITE_HEAP 4 00000011010001',
      'MOVE_H_HD 4 79', 
      'WRITE_HEAP 4 00000011010010',
      'MOVE_H_HD 4 80',
      'WRITE_HEAP 4 00000011010011',
      'MOVE_H_HD 4 81',
      'WRITE_HEAP 4 00000011010100',
      'MOVE_H_HD 4 82',
      'WRITE_HEAP 4 00000011010101',
      'MOVE_H_HD 4 83',
      'WRITE_HEAP 4 00000011010110',
      'MOVE_H_HD 4 84',
      'WRITE_HEAP 4 00000011010111',
      'MOVE_H_HD 4 85',
      'WRITE_HEAP 4 00000011011000',
      'MOVE_H_HD 4 86',
      'WRITE_HEAP 4 00000011011001',
      'MOVE_H_HD 4 87',
      'WRITE_HEAP 4 00000011011010',      
      'MOVE_H_HD 4 88',
      'WRITE_HEAP 4 00000011011011',
      'MOVE_H_HD 4 89',
      'WRITE_HEAP 4 00000011011100',      
      'MOVE_H_HD 4 90',
      'WRITE_HEAP 4 00000011011101',
      'MOVE_H_HD 4 91',
      'WRITE_HEAP 4 00000011011110',
      'MOVE_H_HD 4 92',
      'WRITE_HEAP 4 00000011011111',
      'MOVE_H_HD 4 93',
      'WRITE_HEAP 4 00000011100000',
      'MOVE_H_HD 4 94',
      'WRITE_HEAP 4 00000011100001',
      'MOVE_H_HD 4 95',
      'WRITE_HEAP 4 00000011100010',
      'MOVE_H_HD 4 00000011100011',
      'MOVE_H_HD 4 97', 
      'WRITE_HEAP 4 00000011100100',
      'MOVE_H_HD 4 98',
      'WRITE_HEAP 4 00000011100101',
      'MOVE_H_HD 4 99',
      'APP_CALL',
      
      # ALLOC_2 from heap[70 - 99] to harddrive[230 - 259]
      'WRITE_HEAP 4 00000011100110', # 230
      'MOVE_H_HD 4 70',
      'WRITE_HEAP 4 00000011100111', # 231
      'MOVE_H_HD 4 71',
      'WRITE_HEAP 4 00000011101000', # 232
      'MOVE_H_HD 4 72',
      'WRITE_HEAP 4 00000011101001', # 233
      'MOVE_H_HD 4 73',
      'WRITE_HEAP 4 00000011101010', # 234
      'MOVE_H_HD 4 74',
      'WRITE_HEAP 4 00000011101011', # 235
      'MOVE_H_HD 4 75',
      'WRITE_HEAP 4 00000011101100', # 236
      'MOVE_H_HD 4 76',
      'WRITE_HEAP 4 00000011101101', # 237
      'MOVE_H_HD 4 77',
      'WRITE_HEAP 4 00000011101110', # 238
      'MOVE_H_HD 4 78',
      'WRITE_HEAP 4 00000011101111', # 239
      'MOVE_H_HD 4 79',
      'WRITE_HEAP 4 00000011110000', # 240
      'MOVE_H_HD 4 80',
      'WRITE_HEAP 4 00000011110001', # 241
      'MOVE_H_HD 4 81',
      'WRITE_HEAP 4 00000011110010', # 242
      'MOVE_H_HD 4 82',
      'WRITE_HEAP 4 00000011110011', # 243
      'MOVE_H_HD 4 83',
      'WRITE_HEAP 4 00000011110100', # 244
      'MOVE_H_HD 4 84',
      'WRITE_HEAP 4 00000011110101', # 245
      'MOVE_H_HD 4 85',
      'WRITE_HEAP 4 00000011110110', # 246
      'MOVE_H_HD 4 86',
      'WRITE_HEAP 4 00000011110111', # 247
      'MOVE_H_HD 4 87',
      'WRITE_HEAP 4 00000011111000', # 248
      'MOVE_H_HD 4 88',
      'WRITE_HEAP 4 00000011111001', # 249
      'MOVE_H_HD 4 89',
      'WRITE_HEAP 4 00000011111010', # 250
      'MOVE_H_HD 4 90',
      'WRITE_HEAP 4 00000011111011', # 251
      'MOVE_H_HD 4 91',
      'WRITE_HEAP 4 00000011111100', # 252
      'MOVE_H_HD 4 92',
      'WRITE_HEAP 4 00000011111101', # 253
      'MOVE_H_HD 4 93',
      'WRITE_HEAP 4 00000011111110', # 254
      'MOVE_H_HD 4 94',
      'WRITE_HEAP 4 00000011111111', # 255
      'MOVE_H_HD 4 95',
      'WRITE_HEAP 4 00000100000000', # 256
      'MOVE_H_HD 4 96',
      'WRITE_HEAP 4 00000100000001', # 257
      'MOVE_H_HD 4 97',
      'WRITE_HEAP 4 00000100000010', # 258
      'MOVE_H_HD 4 98',
      'WRITE_HEAP 4 00000100000011', # 259
      'MOVE_H_HD 4 99',
      'APP_CALL',
      
      
      
      
       
      
      
      'WRITE_HEAP 25 00000000', # defualt process ID           
      'WRITE_HEAP 26 00000001', #  number to increment 
      'WRITE_HEAP 0 00011001',
      'WRITE_HEAP 1 00011010',
      'WRITE_HEAP 2 00011001' , 
      'WRITE_HEAP 3 001000',
      'SYS_CALL 010000',
      
      
      
      
      
      
              
      
      'WRITE_RAM 75 11111111' , # 0 - 75 OS RAM 76-189 IS APPLICTION RAM
      'WRITE_RAM 190 11111111', # 190 - 256 bit map the filesysetem
      'WRITE_HEAP 50 11111111111111' , # 0 - 50 os heap 
      'WRITE_HEAP 150 11111111111111' , # 51 - 150 HEAP
      # REST IS THE LOCATION OF WHERE FILE ARE STORED IN HARDDRIVE
      'WRITE_HEAP 5 00000111110100' , # first 500 spaces are for commands
      'WRITE_HEAP 6 11111111111111' , # rest is for files
      'SYS_CALL 000000',
      
      
     
      
      
      
      
      
      
 
      
        
      
      
      
      
      
      
      
      
       
    
      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
]

assembler.load_program_into_Assembler(program_code=os)
machine_code = assembler.assemble()
#print(machine_code)
cpu.harddrive.load_program(machine_code)

cpu.harddrive.visualize()
#cpu.run()
#cpu.RAM.visualize()
#cpu.Heap.visualize()
#cpu.harddrive.visualize()