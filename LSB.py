from PIL import Image
import sys


class LSB():
    def __init__(self, filename, message):
        self.filename = filename
        self.message = message
        self.cover = None

    def open_image(self):
        try:
            self.cover = Image.open(self.filename)
        except FileNotFoundError as e:
            print('Error: ' + self.filename + ' does not exist. Please specify an existing file')

    def get_bit_depth(self):
        mode_to_bd = {'1':1, 'L':8, 'P':8, 'RGB':24, 'RGBA':32, 'CMYK':32, 'YCbCr':24, 'I':32, 'F':32}

        if self.cover is not None:
            return mode_to_bd[cover.mode]

    """ Validates that the message can fit into the specified file
        Counts the number of bits in the secret message and 
        compares it to how much space exists in the cover image """
    def validate(self):
        pass

    def hide(self):
        pass

# Driver script for testing
x = LSB('jjj.png')
x.open_image()
