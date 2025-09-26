class HEAP():
    def __init__(self):
        self.storage = {}
        for i in range(256):
            address = format(i,'08b')
            self.storage[address] = '0'*84
            
    def read(self, address):
        print(f'getting {self.storage.get(address , '0'*84)}')

        return self.storage.get(address,'0' * 84)
    
    def write(self, address, new_value):
        print(f'writting {new_value} to {address}')
        self.storage[address] = new_value
        return self.storage[address]
    
    def visualize(self):
        print(' The HEAP ')

        print("Address    Decmail_address   Value")
        print("----------------------------------")
        for address, value in self.storage.items():
            print(f"{address}    |    {int(address , 2 )}      |     {value}")
            
x = HEAP()
x.visualize()
            
            
