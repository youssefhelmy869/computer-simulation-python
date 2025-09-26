

class Screen():
    def __init__(self):
        pass

    def show(self, binary_data, size_w, size_l):
        """
        Displays a screen based on binary data.

        Args:
            binary_data (str): A binary string representing the screen pixels.
            size_w (str): The width of the screen as a binary string.
            size_l (str): The height of the screen as a binary string.

        Raises:
            ValueError: If the binary data length does not match the screen dimensions.
        """
        size_w = int(size_w, 2)  # Convert binary string to integer
        size_l = int(size_l, 2)

        if len(binary_data) != size_w * size_l:
            raise ValueError("Binary data length does not match screen dimensions.")

        for row in range(size_l):
            line = binary_data[row * size_w:(row + 1) * size_w]
            output = ''.join('#' if bit == '1' else ' ' for bit in line)
            print(output)
            
x = Screen()
x.show(binary_data='1111111111111111' , size_w='0100' , size_l='0100')
