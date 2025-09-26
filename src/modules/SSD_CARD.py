class SSD_CARD():

    def __init__(self):
      
        self.storage = {}
        for i in range(65,536):
            
            address = format(i, '016b')
            self.storage[address] = '0'* 84

    def read(self, address):

        return self.storage.get(address,'0' * 84)

    def write(self, address, new_value):
        self.storage[address] = new_value
        return self.storage[address]

    def visualize(self):
        print(' harddrive ')

        print("Address    Value")
        print("----------------")
        for address, value in self.storage.items():
            print(f"{address}    {value}")
x = SSD_CARD()
x.visualize()
