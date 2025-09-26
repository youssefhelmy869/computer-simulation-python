class FlowError(Exception):
    pass



class stack():
    def __init__(self):
        self.stack_pointer = '00000001'
        self.storge = {}
        for i in range(256):
            address = format(i,'08b')
            self.storge[address] = '0'*14
    
    def PUSH(self , hd_address):   # push harddrive address to the stack
        if self.stack_pointer == '11111111':
            raise FlowError('Stack overflow error')
        else:
            self.storge[self.stack_pointer] = hd_address
            print(f'address {hd_address} has been pushed to {self.stack_pointer}')
            self.stack_pointer = format(int(self.stack_pointer, 2 ) + 1 , f"0{len(self.stack_pointer)}b")
    
    def POP (self):
        if self.stack_pointer == '00000000':
            raise  FlowError('Stack underflow error')
        print(f'address {self.stack_pointer} has been POPED')
        self.stack_pointer = format(int(self.stack_pointer, 2 ) - 1 , f"0{len(self.stack_pointer)}b")
        
        return self.storge[self.stack_pointer]
    
    def visualize(self):
        """
        Prints the stack contents from bottom to top.
        """
        print("Stack visualization (bottom -> top):")
        for i in range(1, int(self.stack_pointer, 2)):
            addr = format(i, '08b')
            print(f"{addr}: {self.storge[addr]}")

