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
cv.rectangle(blank,(0,0),(50,50),(200,155,200),thickness=cv.FILLED) #thickness=-1 is also for filling,but other numbers like 2 will thicken rectangular 
cv.imshow("image with rectangular",blank)
#draw a circle
cv.circle(blank,(250,250),20,(100,182,250),thickness=2)
cv.imshow("image with circle",blank)
cv.waitKey(0)