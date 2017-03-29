import sys
import os
from argparse import ArgumentParser

def parser():
   
    parser = ArgumentParser(description="image-steg")

    parser.add_argument('-d', dest='encrypt', action='store_false',
                        help="Sets method to decrypt, default is encrypt",
                        default=True)

    parser.add_argument('-a', dest='algorithm', action='store_const',
                        help="Sets algorithm to LSB, default is DCT",
                        const="LSB", default="DCT")

    parser.add_argument("-i", dest="inputfile", required=True,
                        help="input file name", metavar="FILE")

    parser.add_argument("-o", dest="outputfile", required=False,
                        help="output file name (optional)", metavar="FILE")

    parser.add_argument("-s", dest="string", required=False,
                        help="Message to encrypt")

    args = parser.parse_args()
    return args

def main():
    args = parser()

    algo = args.algorithm
    inFile = args.inputfile
    message = args.string
    outFile = args.outputfile

    if args.encrypt is True and args.string is None:
        raise ValueError("Encryption requires an input string")

    if args.encrypt:
        if not args.outputfile:
            outFile = "ENCRYPTED"+inFile
    else:
        if not args.outputfile:
            outFile = "DECRYPTED"+inFile

if __name__ == "__main__":
    main()
