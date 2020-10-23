#modules needed for the project 
import numpy
import pandas
import cv2
import argparse

#using the argparse module to take image from command line
ap = argparse.ArgumentParser()
ap.add_argument('-i','--image', required=True, help="Image Path")
args= vars(ap.parse_args())
image_path = args['image']

#using opencv to read the image 
img = cv2.imread(image_path) #loads image from specific file, in this case it'll be from the terminal

#global variables
clicked = False
r = g = b = xpos = ypos = 0 #hex values and x,y cordinate of mouse

