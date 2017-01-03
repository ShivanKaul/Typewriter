import math
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random
import scipy.ndimage.filters

def create_typewriter_effect(img):
	gradient = np.gradient(img)
	print(gradient)
	new_img = np.zeros(img.shape)
	print(img.shape)
	for x in range(img.shape[0]):
		for y in range(img.shape[1]):
			dx = gradient[0][x,y]
			dy = gradient[1][x,y]
			if (dx > 0.1 or dy > 0.1):
				if(random.random()>0.7):
					new_img[x, y] = img[x,y]
				else:
					new_img[x, y] = 0
			else:
				new_img[x, y] = img[x,y]

	new_img = scipy.ndimage.filters.convolve(new_img, generate_gaussian(0.7, 4), mode='nearest')
	mpimg.imsave("result.jpg" , new_img, cmap=plt.get_cmap('gray'))


def generate_gaussian(sigma, N):
	neg = -int(N/2)
	pos = int(N/2)

	x_vals = range(neg, pos)
	y_vals = range(neg, pos)

	x, y = np.meshgrid(x_vals, y_vals)
	g = np.exp((-np.power(x, 2)/(2*(pow(sigma,2)))) - (np.power(y, 2)/(2*(pow(sigma, 2)))))
	g = np.divide(g, np.sum(g))
	return g

imname = sys.argv[1]
img = plt.imread(imname)/255

create_typewriter_effect(img)