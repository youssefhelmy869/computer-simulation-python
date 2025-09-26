class MYEXCEPTION(Exception):
    pass
class harddrive():

    def __init__(self):
      
        self.storage = {}
        for i in range(1000):
            
            address = format(i, '014b')
            self.storage[address] = '0'* 84

    def read(self, address):

        return self.storage.get(address,'0' * 84)

    def write(self, address, new_value):
        self.storage[address] = new_value
        return self.storage[address]

    def visualize(self):
        print(' harddrive ')

        print("Address        decimal_address        Value")
        print("-------------------------------------------")
        for address, value in self.storage.items():
            print(f"{address}  |  {int(address , 2 )}  |  {value}")
            
    def load_program(self,command_list):
        for command in command_list:
            for address , info in self.storage.items():
                if info == '0' * 84:
                    self.storage[address] = command
                    break
                
            
            
                    
        
        