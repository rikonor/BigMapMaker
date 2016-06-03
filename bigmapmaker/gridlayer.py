import sys
from PIL import Image, ImageDraw

# 1 Get file from args
if len(sys.argv) != 2:
	print "Error: Please enter a filename."
	sys.exit(2)
img = Image.open(sys.argv[1])

# 2 Manual Filename
# img = Image.open("pic.jpeg")

# Start work
xDim, yDim = img.size

# Create xLine
xLine = Image.new('RGBA', (xDim, 1   ) ) # Horizontal Line
xDraw = ImageDraw.Draw(xLine)
xDraw.polygon([ (0,0), (xDim ,0) ], outline=(255,255,255,200))

# Create yLine
yLine = Image.new('RGBA', (1   , yDim) ) # Vertical   Line
yDraw = ImageDraw.Draw(yLine)
yDraw.polygon([ (0,0), (0 ,yDim) ], outline=(255,255,255,200))

# paste xLine along image
yStartIndex = 1
yEndIndex = yDim/500
for yCurrentIndex in range(yStartIndex, yEndIndex):
	yOffset = (0, yCurrentIndex*500)
	img.paste(xLine, yOffset, mask=xLine)

# paste yLine along image
xStartIndex = 1
xEndIndex = xDim/500
for xCurrentIndex in range(xStartIndex, xEndIndex):
	xOffset = (xCurrentIndex*500, 0)
	img.paste(yLine, xOffset, mask=yLine)

img.save("images/mapFullGrid.jpeg", quality=100, optimize=True, progressive=True)
