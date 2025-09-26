"""
RAM Module

This module defines a `RAM` class that simulates a Random Access Memory (RAM) module. The RAM has 256 addresses, each capable of storing an 8-bit binary value. The module provides methods to read, write, and visualize the contents of the RAM.

Classes:
    RAM: A class to simulate a RAM module with 256 8-bit addresses.

Example:
    # Create a RAM instance
    ram = RAM()

    # Write a value to an address
    ram.write('00001101', '11111101')

    # Read a value from an address
    value = ram.read('00001101')

    # Visualize the RAM contents
    ram.visualize()
"""

class RAM():

    def __init__(self):
      
        self.storage = {}
        for i in range(256):
            # Each address is an 8-bit binary string, value is 8-bit binary string (initialized to '0'*8)
            address = format(i, '08b')
            self.storage[address] = '00000000'

    def read(self, address):

        return self.storage.get(address, None)

    def write(self, address, new_value):
       
        # Always store 8 bits, pad or trim as needed
        if len(new_value) < 8:
            new_value = new_value.zfill(8)
        elif len(new_value) > 8:
            new_value = new_value[-8:]
        self.storage[address] = new_value
        return self.storage[address]

    def visualize(self):
        print(' RAM ')

        print("Address    Value")
        print("----------------")
        for address, value in self.storage.items():
            print(f"{address}    {value}")
            
