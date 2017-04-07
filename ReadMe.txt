Read Me

Execution instructions 
======================

python test.py (flags)

Available flags are: 
-h : help flag, provides instructions on how to run 
-a: change the algorithm, adding the -a flag allows you to test the LSB implementation, negating the -a flag runs the DCT implementation
-d: decrypts the image, negating the -d flag runs the encryption 
-i inputFile: required flag, submits the desired input file
-o outputFile: not required, names the output file
-s 'message': required for encryption, string to be encrypted
-f FILE: text file to be encrypted

LSB encryption example:
	python test.py -i inputFile.jpg -a -s 'message to encrypt'

DCT encryption example:
	python test.py -i inputFile.jpg -s 'message to encrypt'

LSB decryption example:
	python test.py -i inputFile.jpg -a -d

DCT decryption example:
	python test.py -i inputFile.jpg -d