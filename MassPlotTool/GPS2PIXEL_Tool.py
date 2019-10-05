#Please refer to readme prior to use# 

import pandas as pd

#Input image longitudes (this will be our x-axis)
leftmost_long = 
rightmost_long = 

#Input image latitudes (this will be our y-axis)
upper_lat = 
lower_lat =

#Input image dimensions 
x = 
y = 

#load GPS coordinates as pandas dataframe 
df = pd.read_csv(r'\coordinates.csv', sep=',',header=0) 

#Compute longitude per individual pixel 
long_per_pix = (rightmost_long - leftmost_long)/x
print(long_per_pix)

#Compute longitude per individual pixel 
lat_per_pix = (upper_lat - lower_lat)/y
print(lat_per_pix)

#Calculate a pixel value for each coordinate 
df['pix_long'] = (df['longitude'] - leftmost_long)/long_per_pix
df['pix_lat'] = (upper_lat - df['latitude'])/lat_per_pix

#save df as csv 
df.to_csv (r'\GPS2PIXEL.csv', index = None, header=True)
