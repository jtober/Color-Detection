#modules needed for the project 
import numpy
import pandas as pd
import cv2
import argparse

#using the argparse module to take image from command line
ap = argparse.ArgumentParser()
ap.add_argument('-i','--image', required=True, help="Image Path")
args= vars(ap.parse_args())
img_path = args['image']

#using opencv to read the image 
img = cv2.imread(img_path) #loads image from specific file, in this case it'll be from the terminal

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

#function to get x,y coordinates of mouse double click and calculate rbg values
def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_function)

while(True):
    cv2.imshow('image',img)
    if (clicked):
        #create rectangle showing image 
        cv2.rectangle(img,(15,15), (750,60), (b,g,r), -1)
        #create text to display the color name and its RGB values
        text = getColorName(r,g,b) + ' R='+ str(r) + ' G='+ str(g) + 'B='+ str(b)

        cv2.putText(img, text, (50,50), 2,0.8,(255,255,255),2,cv2.LINE_AA)

        #making sure that light colors will display properly
        if (r+g+b>=600):
            cv2.putText(img, text, (50,50), 2,0.8,(0,0,0),2,cv2.LINE_AA)

        clicked = False
    #break loop if user presses 'esc' key
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows
