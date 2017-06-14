#!/usr/bin/python3

import os
import sys
import time
from LSB import LSB
from DCT import DCT
from argparse import ArgumentParser

def parser():
   
   #set the command line arguments
    parser = ArgumentParser(description="Stego: DCT and LSB Image Steganography")

    parser.add_argument('-d', dest='encrypt', action='store_false',
                        help="Set method to decode, default is encode",
                        default=True)

    parser.add_argument('-a', dest='algorithm', action='store_const',
                        help="Set encoding/decoding algorithm to LSB, default is DCT",
                        const="LSB", default="DCT")

    parser.add_argument("-i", dest="inputfile", required=True,
                        help="Specify input file name", metavar="FILE")

    parser.add_argument("-o", dest="outputfile", required=False,
                        help="Specify output file name (optional)", metavar="FILE")

    parser.add_argument("-s", dest="string", required=False,
                        help="Specify message to encrypt")

    parser.add_argument("-f", dest="file", required=False,
                        help="Specify text file containing message", metavar="FILE")

    args = parser.parse_args()
    return args

def main():
    args = parser()
    
    algo = args.algorithm
    inFile = args.inputfile
    message = args.string
    outFile = args.outputfile
    msgFile = args.file


    #encryption input check
    if args.encrypt is True and args.string is None and args.file is None:
        raise ValueError("Encryption requires an input string")

    # read file msg
    if args.file is not None:
        with open(msgFile, 'r') as textFile:
            message = textFile.read().replace('\n', '')
        
    #encryption
    if args.encrypt:

        #set output file if not specified
        if not args.outputfile:
            rawName = os.path.basename(os.path.normpath(inFile))
            dirName = os.path.dirname(os.path.normpath(inFile))

            outFile = dirName + '/' + algo + rawName

        #LSB implementation
        if algo == "LSB":
            start = time.time()
            x = LSB(inFile)
            encoded = x.hide(message, outFile)
            end = time.time()-start
            print ('time: ')
            print (end)
            #print ('Message encoded = ' + x.message)
        else: 
        #DCT implementation
            start = time.time()
            x = DCT(inFile)
            secret = x.DCTEn(message, outFile)
            end = time.time()-start
            print ('time: ')
            print (end)
            #print('Message encoded = '+ x.message)

    #decryption
    else:
        #LSB implementation
        if algo == 'LSB':
            start = time.time()
            y = LSB(inFile)
            secret = y.extract()
            end = time.time()-start
            print('Hidden Message:\n' + secret)
            print ('time: ')
            print (end)
        else: 
        #DCT implementation
            start = time.time()
            y = DCT(inFile)
            decode = y.DCTDe()
            end = time.time()-start
            print('Hidden Message:\n'+ decode)
            print ('time: ')
            print (end)
            
  

if __name__ == "__main__":
    main()
