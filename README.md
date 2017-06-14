# A Comparison of Image Steganography Techniques (LSB vs DCT)

This project was created for CIS*4110: Computer Security at the University of Guelph.

## Requirements

The main requirements are: OpenCV & Pillow. Comparing the results requires matplotlib and other dependencies.

- openCV==3.0.0
- cycler==0.10.0
- decorator==4.0.11
- matplotlib==2.0.0
- networkx==1.11
- numpy==1.12.1
- olefile==0.44
- Pillow==4.1.0
- pyparsing==2.2.0
- python-dateutil==2.6.0
- pytz==2017.2
- PyWavelets==0.5.2
- scikit-image==0.13.0
- scipy==0.19.0
- six==1.10.0

## Usage 
Standard usage is:

    stego.py [-h] [-d] [-a] -i FILE [-o FILE] [-s STRING] [-f FILE]

```
Stego: DCT and LSB Image Steganography

Optional arguments:
-h, --help  Show this help message and exit
-d          Set method to decode, default is encode
-a          Set encoding/decoding algorithm to LSB, default is DCT
-i FILE     Specify input file name
-o FILE     Specify output file name (optional)
-s STRING   Specify message to encrypt
-f FILE     Specify text file containing message
```

LSB encryption example:

    stego.py -i inputFile.jpg -a -s 'message to encrypt'

DCT encryption example:

    stego.py -i inputFile.jpg -s 'message to encrypt'

LSB decryption example:

    stego.py -i inputFile.jpg -a -d

DCT decryption example:

    stego.py -i inputFile.jpg -d

## Contributors
- [Neivin Mathew](https://github.com/neivin)
- [Robyn Rintjema](https://github.com/rrintjem)
- [Steven Kalapos](https://github.com/skalapos)

