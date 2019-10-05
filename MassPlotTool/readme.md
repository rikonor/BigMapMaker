# Mass Plot Tool 
## Introduction 
 I was recently given the task of generating a large map in a single image for a city (Karachi, Pakistan) and place hundreds of markers on it at specific coordinates. Rikonor’s BigMapmaker really helped me with generating a large map image, but now I had to find a way to efficiently place markers on it. I created this handy tool to help with the process. Here's how to use the Mass Plot Tool. 

 **Step 1**
Add all the coordinates you wish to mark in the coordinates.csv file.

**Step 2**
Record the starting and ending coordinates for your image. An easier way to think about this step is as follows: You need the left-most longitude, right-most longitude, upper latitude and lower latitude

**Step 3**
Open the GPS2PIXEL py file and and input the recorded values and image dimensions. When you run this tool, a pixel location will be calculated for each GPS coordinate and saved as a csv file. 

**Step 4**
Open and run Draw_markers.py. You have a few different options for markers. I've linked the documentation page in the code.

That's all. 
-Saad 

