from matplotlib import pyplot as plt
import cv2 as cv
import numpy as np

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("input", help="Path to input file")
parser.add_argument("min_threshold")
parser.add_argument("max_threshold")
args=parser.parse_args()
input=args.input
Cmin, Cmax = int(args.min_threshold), int(args.max_threshold)

img=cv.imread('image.png',cv.IMREAD_GRAYSCALE)
img = cv.GaussianBlur(img,(5,5),1)
edges = cv.Canny(img,Cmin,Cmax)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.axis("off")
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.axis("off")
plt.show()



