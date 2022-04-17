from calendar import c
from pickletools import uint8
import cv2 as cv
import numpy as np 
blank=np.zeros((300,300,3),dtype="uint8")
cv.imshow("blank",blank)
#paint the image with a certain color
blank[50:100,150:300]=0,0,255
cv.imshow("painted image",blank)
#draw a rectangular 
cv.rectangle(blank,(0,0),(50,50),(200,155,200),thickness=cv.FILLED)
cv.imshow("image with rectangular",blank)
cv.waitKey(0)