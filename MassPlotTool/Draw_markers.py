# Import libraries 
import numpy as np 
import cv2
import pandas as pd

#Import the csv with pixel locations  
df = pd.read_csv('[GPS2PIXEL csv]', sep=',',header=0)

# load map image 
img = cv2.imread('[Image file location]',1)

#Extract the pixel columns 
df1 = df[['pix_long','pix_lat']]

#Convert to array 
arr = df1.to_numpy()

#Place markers using Opencv. Visit https://docs.opencv.org/3.4/d6/d6e/group__imgproc__draw.html for marker types 
for row in arr:
    cv2.drawMarker(img, tuple(row),(0,0,255), markerType=cv2.MARKER_STAR, markerSize=50, thickness=4, line_type=cv2.LINE_AA)
    
#Save file with markers 
cv2.imwrite("[Output location].jpg",img)