# Required Libraries
import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
from pathlib import Path
import argparse
import numpy

# Argument parsing variable declared
ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image",
				required=True,
				help="Path to folder")

args = vars(ap.parse_args())

# Find all the images in the provided images folder
mypath = args["image"]
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
images = numpy.empty(len(onlyfiles), dtype=object)

# Iterate through every image
# and resize all the images.
count = 1
for n in range(0, len(onlyfiles)):

	path = join(mypath, onlyfiles[n])
	images[n] = cv2.imread(join(mypath, onlyfiles[n]),
						cv2.IMREAD_UNCHANGED)

	# Load the image in img variable
	img = cv2.imread(path, 1)

	# Define a resizing Scale
	# To declare how much to resize
	resize_width = 100
	resize_hieght = 100
	resized_dimensions = (resize_width, resize_hieght)

	# Create resized image using the calculated dimensions
	resized_image = cv2.resize(img, resized_dimensions,
							interpolation=cv2.INTER_AREA)

	# Save the image in Output Folder
	cv2.imwrite(
	'resize_to_100x100/papua/papua_' +str(count)+'_resized.jpg', resized_image);count+=1

print("Images resized Successfully")
