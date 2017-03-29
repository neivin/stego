from PIL import Image
import sys


class LSB():
    def __init__(self, filename, message):
        self.filename = filename
        self.message = message
        self.cover = None
        self.bits = None

    def open_image(self):
        try:
            self.cover = Image.open(self.filename)
            return True
        except FileNotFoundError as e:
            print('Error: ' + self.filename + ' does not exist. Please specify an existing file')
            return False

    def get_bit_depth(self):
        mode_to_bd = {'1':1, 'L':8, 'P':8, 'RGB':24, 'RGBA':32, 'CMYK':32, 'YCbCr':24, 'I':32, 'F':32}

        if self.cover is not None:
            return mode_to_bd[self.cover.mode]


    def messageBits(self, string):
        bits = []
        
        # Convert each character into binary and pad with 0s
        for char in string:
            binval = bin(ord(char))[2:].rjust(8,'0')
            
            for bit in binval: 
                bits.append(bit)

        return bits

    """ Validates that the message can fit into the specified file
        Counts the number of bits in the secret message and 
        compares it to how much space exists in the cover image """
    def validate(self):
        img_opened = self.open_image()
        
        # Find the capacity of the image
        capacity = 0
        if img_opened:
            capacity = self.cover.width * self.cover.height * (self.get_bit_depth()/8)
            print ('Capacity of image:\t' + str(capacity))

        # Convert the string message into bits 
        self.bits = self.messageBits(self.message)
        print('Message bits:\t\t' + str(len(self.bits)))

        if len(self.bits) >= capacity:
            print('Error: The message is too long to be encoded into the image ' + self.filename)
            return False

        return True


        
    def hide(self):
        # Check that the message can fit inside the image
        if not self.validate():
            print ('Error: Validation failed. Cannot encode message into image')
            return


def a2bits_list(chars):
    return [bin(ord(x))[2:].rjust(8, '0') for x in chars]

# Driver script for testing
x = LSB('macaws.png', 'SECRET')
x.hide()

print(str(a2bits_list('SECRET')))