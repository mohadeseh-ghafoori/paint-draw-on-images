from pickletools import uint8
import cv2 as cv
import numpy as np 
blank=np.zeros((300,300,3),dtype="uint8")
cv.imshow("blank",blank)
#paint the image with a certain color
blank[50:100,150:300]=0,0,255
cv.imshow("painted image",blank)
cv.waitKey(0)