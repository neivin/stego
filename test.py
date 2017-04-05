import sys
import os
from LSB import LSB
from DCT import DCT
from argparse import ArgumentParser

def parser():
   
   #set the command line arguments
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


    #encryption input check
    if args.encrypt is True and args.string is None:
        raise ValueError("Encryption requires an input string")

    #encryption
    if args.encrypt:

        #set output file if not specified
        if not args.outputfile:
            outFile = "ENCRYPTED"+inFile

        #LSB implementation
        if algo == "LSB":
            x = LSB(inFile)
            encoded = x.hide(message, outFile)
            #print ('Message encoded = ' + x.message)
        else: 
        #DCT implementation
            x = DCT(inFile)
            secret = x.DCTEn(message, outFile)
            #print('Message encoded = '+ x.message)

    #decryption
    else:
        #LSB implementation
        if algo == 'LSB':
            y = LSB(inFile)
            secret = y.extract()
            print('Hidden Message found = ' + secret)
        else: 
        #DCT implementation
            y = DCT(inFile)
            decode = y.DCTDe()
            print('Hidden Message found= '+ decode)
            
  

if __name__ == "__main__":
    main()
