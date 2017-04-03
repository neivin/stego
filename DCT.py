#!/usr/local/bin/python
from __future__ import print_function
import cv2, sys, numpy as np, itertools

from PIL import Image

quant = np.array([[16,11,10,16,24,40,51,61],
                    [12,12,14,19,26,58,60,55],
                    [14,13,16,24,40,57,69,56],
                    [14,17,22,29,51,87,80,62],
                    [18,22,37,56,68,109,103,77],
                    [24,35,55,64,81,104,113,92],
                    [49,64,78,87,103,121,120,101],
                    [72,92,95,98,112,100,103,99]])

class DCT():    
    def __init__(self, imPath):
        self.imPath = imPath
        self.message = None
        self.bitMess = None
        self.oriCol = 0
        self.oriRow = 0
        self.numBits = 0   
    
    def DCTEn(self, secret, outIm):
        #load image for processing
        img = self.loadImage()
        if img is None:
            print("Error: File not found!")
            return

        self.message = str(len(secret))+'*'+secret
        self.bitMess = self.toBits()
        print(self.bitMess)
        
        #get size of image in pixels
        row,col = img.shape[:2]
        self.oriRow, self.oriCol = row, col        
        
        #cv2.imshow('g',gray)
        #cv2.imshow('i', img2)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        #make divisible by 8x8
        img = self.addPadd(img, row, col)
        row,col = img.shape[:2]

        #split image into RGB channels
        bImg,gImg,rImg = cv2.split(img)

        #message to be hid in blue channel so converted to type float32 for dct function
        bImg = np.float32(bImg)
        #print(bImg[0:8,0:8])
    
        #break into 8x8 blocks
        imgBlocks = [bImg[j:j+8, i:i+8]-128 for (j,i) in itertools.product(xrange(0,row,8),
                                                                       xrange(0,col,8))]
        #print(imgBlocks[1][0])
        #Blocks are run through DCT function
        dctBlocks = [np.round(cv2.dct(img_Block)) for img_Block in imgBlocks]

        #blocks then run through quantization table
        quantizedDCT = [np.round(dct_Block/quant) for dct_Block in dctBlocks]
        
        #set LSB in DC value corresponding bit of message
        messIndex = 0
        letterIndex = 0
        

        for quantizedBlock in quantizedDCT:
            #find LSB in DC coeff and replace with message bit
            DC = quantizedBlock[0][0]
            DC = np.uint8(DC)
            DC = np.unpackbits(DC)
            #print(DC, end=' ')
            DC[7] = self.bitMess[messIndex][letterIndex]
            #print(DC,end= ' ')
            DC = np.packbits(DC)
            
            #print(DC)
            DC = np.float32(DC)
            DC= DC-255
            quantizedBlock[0][0] = DC

            letterIndex = letterIndex+1
            if letterIndex == 8:
                letterIndex = 0
                messIndex = messIndex + 1
                if messIndex == len(self.message):
                    break
        
        #print(quantizedDCT[1][0])

        #blocks run inversely through quantization table
        quantizedDCT = [quantizedBlock *quant for quantizedBlock in quantizedDCT]
        
        #blocks run through inverse DCT
        sImgBlocks = [cv2.idct(B)+128 for B in quantizedDCT]
        
        #print(sImgBlocks[1][0])
        sImg=[]
        for chunkRowBlocks in self.chunks(sImgBlocks, col/8):
            for rowBlockNum in xrange(8):
                for block in chunkRowBlocks:
                    sImg.extend(block[rowBlockNum])
        sImg = np.array(sImg).reshape(row, col)
        
        #converted from type float32
        sImg = np.uint8(sImg)
        
        sImg = cv2.merge((sImg,gImg,rImg))
        cv2.imwrite(outIm,sImg)
        return sImg

    def DCTDe(self):
        img = cv2.imread(self.imPath, cv2.IMREAD_UNCHANGED)

        row,col = img.shape[:2]

        messSize = None
        messageBits = []

        #split image into RGB channels
        bImg,gImg,rImg = cv2.split(img)
        #print(bImg[0:8,0:8])
        #message hid in blue channel so converted to type float32 for dct function
        bImg = np.float32(bImg)
        #print(bImg[0:8,0:8])
    
        #break into 8x8 blocks
        imgBlocks = [bImg[j:j+8, i:i+8] for (j,i) in itertools.product(xrange(0,row,8),
                                                                       xrange(0,col,8))]
        #print(imgBlocks[1][0])
        #Blocks are run through DCT function
        dctBlocks = [cv2.dct(img_Block) for img_Block in imgBlocks]
        
        #blocks then run through quantization table
        quantizedDCT = [dct_Block/ (quant) for dct_Block in dctBlocks]
        
        #print(quantizedDCT[1][0])
        i=0
        #message extracted from LSB of DC coeff
        for quantizedBlock in quantizedDCT:
            DC = quantizedBlock[0][0]
            DC = np.uint8(DC)
            DC = np.unpackbits(DC)
            print(DC[7], end = '')
            i=1+i
            if i == 100:
                break
            

        return messageBits

    def chunks(self,l, n):
        for i in xrange(0, len(l), n):
            yield l[i:i + n]

    def loadImage(self):
        #load image
        img = cv2.imread(self.imPath, cv2.IMREAD_UNCHANGED)
        
        if img is None:
            return None  

        return img

    #add 'Padding' making image dividable by 8x8 blocks
    def addPadd(self,img, row, col):
        img = cv2.resize(img,(col+(8-col%8),row+(8-row%8)))    
        return img

    def toBits(self):
        bits = []

        for char in self.message:
            binval = bin(ord(char))[2:].rjust(8,'0')
            
            #for bit in binval: 
            bits.append(binval)

        self.numBits = bin(len(bits))[2:].rjust(8,'0')
        return bits

#Test Script
testEn = DCT('lenna.png')
secret = testEn.DCTEn('Super SECRET!', 'secret.png')

print('Message encoded = '+ testEn.message)

testDe = DCT('secret.png')
decode = testDe.DCTDe()
print('Hidden Message extracted = '+decode)