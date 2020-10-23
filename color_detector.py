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

#using pandas to read teh csv file and giving names to each column
index = ['color','color_name','hex','R','G','B']
csv = pd.read_csv('colors.csv', names=index, header=None)

#now time for the math part to calculate shortest distance from all colors and find the most matching color
#we first need a function to do the caculations
def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R-int(csv.loc[i, "R"])) + abs(G-int(csv.loc[i, "G"])) + abs(B-int(csv.loc[i, "B"]))
        if d<= minimum:
            minimum = d
            cname= csv.loc[i, "color_name"]
        return cname

#