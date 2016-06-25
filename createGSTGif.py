# Greyscale threshold gif project
# take valid image file
# confirm if/convert to greyscale
# create mask for each value [0...255]
# create gif of all masks in order to create effect

# base imports
from sys import argv
import os
# image imports
import cv2
import numpy as np

# need these 2 to do the gif transform. cv2 lacks this file extension..
from PIL import Image, ImageSequence
from images2gif import writeGif

# flags: 1-color, 0-greyscale, -1-alphachannel
cvImGrey = cv2.imread(os.path.abspath(argv[1]), 0)

# confirmed type is <type 'numpy.ndarray'>
# print(type(cvImGrey))

def binaryThresholdByValue(x, img):
	'''return binary thresholded mask of pixels
	   at value x, where x is range(0, 256)'''

	if 0 <= x < 256:
		try:
			ret, mask = cv2.threshold(img, x, x, cv2.THRESH_BINARY)
			return Image.fromarray(np.asarray(mask))
		except Exception as e:
			print "Error: {}".format(e)
		

	return None

def getArrayOfThresholdMasks(img):
	'''returns array of masks'''

	return [binaryThresholdByValue(x, img) for x in range(256)]

def threshToGif(imgName, thresholds):
	'''write a gif!'''

	writeGif(imgName, thresholds, duration=0.05)


thresholds = getArrayOfThresholdMasks(cvImGrey)

threshToGif(argv[1].split('.')[0] + '.gif', thresholds)
