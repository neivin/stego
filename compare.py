from skimage.measure import compare_ssim as structSim
import matplotlib.pyplot as plot
import numpy
import cv2


def meanSquareError(im1, im2):
	error = numpy.sum((im1.astype('float') - im2.astype('float')) ** 2)
	error /= float(im1.shape[0] * im1.shape[1]);

	return error

def compareImages(im1, im2, title):
	mse = meanSquareError(im1,im2)
	ss = structSim(im1,im2,multichannel=True)

	# make figure
	fig = plot.figure(title)
	plot.suptitle('MSE: %.2f, SSIM: %.2f' % (mse,ss))

	ax = fig.add_subplot(1,2,1)
	plot.imshow(im1, cmap = plot.cm.gray)
	plot.axis('off')

	ax = fig.add_subplot(1,2,2)
	plot.imshow(im2, cmap = plot.cm.gray)
	plot.axis('off')

	plot.show()

def main():
	original = cv2.imread('img/lenna.png')
	lsbEncoded = cv2.imread('img/LSBlenna.png')
	dctEncoded = cv2.imread('img/DCTlenna.png')

	original = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
	lsbEncoded = cv2.cvtColor(lsbEncoded, cv2.COLOR_BGR2RGB)
	dctEncoded = cv2.cvtColor(dctEncoded, cv2.COLOR_BGR2RGB)

	# figure
	fig = plot.figure("Images")
	images = ('Original', original), ('LSB', lsbEncoded), ('DCT', dctEncoded)

	for (i, (name, image)) in enumerate(images):
		ax = fig.add_subplot(1,3,i+1)
		ax.set_title(name)
		plot.imshow(image, cmap=plot.cm.gray)
		plot.axis('off')

	plot.show()

	# Compare all the images
	compareImages(original, original, "Original vs Original")
	compareImages(original, lsbEncoded, "Original vs LSB")
	compareImages(original, dctEncoded, "Original vs DCT")


if __name__=='__main__':
	main()