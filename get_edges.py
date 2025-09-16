from matplotlib import pyplot as plt
import cv2 as cv
import skimage
import argparse

'''
Command line usage: python3 get_edges.py <Cmin> <Cmax>
    Cmin - Minimum threshold for Canny
    Cmax - Maximum threshold for Canny
    Optional flag: -c - Use the camera input instead of the test image

Functions:
    get_edges(img, Cmin, Cmax):
        img - source image
        Cmin - Minimum threshold for Canny
        Cmax - Maximum threshold for Canny
        return value - processed image
'''

def get_edges(img, Cmin,Cmax):
    try:
        img = cv.GaussianBlur(img,(5,5),1)
        img = cv.Canny(img,Cmin,Cmax)
    except:
        print("get_edges(): the input is not an image supported by opencv")
        return None
    return img

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("min_threshold",help="Minimum threshold for Canny")
    parser.add_argument("max_threshold",help="Maximum threshold for Canny")
    parser.add_argument("-c",help="Use the camera input instead of the test image",action="store_true")
    args=parser.parse_args()
    if(args.c):
            cam = cv.VideoCapture(0)
            _, img = cam.read()
    else:
        img = skimage.data.coins()
    
    edges = get_edges(img,int(args.min_threshold), int(args.max_threshold))
    if edges is None:
        exit()

    plt.subplot(121),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.axis("off")
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.axis("off")
    plt.show()



