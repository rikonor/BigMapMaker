import glob
from PIL import Image, ImageDraw, ImageFont

# applyText to a large map (according to grid)
# or to a single keymap image

### CONSTANTS ###
letterImageSize = (80, 50)
textColor = (150, 150, 150)
textSize = 40

### AUX FUNCTIONS - TEXT###

def getSegmentText(xIndex, yIndex):
	return chr(ord('A')+yIndex) + str(xIndex+1)

def createTextImage(text = ''):
	# Create small image
	image = Image.new("RGBA", letterImageSize, (255,255,255,0))
	draw = ImageDraw.Draw(image)
	font = ImageFont.truetype("arial.ttf", textSize)
	draw.text((0, 0), text, fill=textColor, font=font)
	return image

def getMainImage(filename):
	# Get canvas image
	try:
		mainImage = Image.open(filename)
		return mainImage
	except:
		print("Image not found.")
		exit(1)

def pasteText(mainImage, textImage, pasteLocation):
	mainImage.paste(textImage, pasteLocation, mask=textImage)

def applyTextToKeymap(mainImage, text):
	# get mainImage dimensions
	xDim, yDim = mainImage.size
	# paste text on image
	textImage = createTextImage(text)
	# pasteLocation = (5, yDim/2 - letterImageSize[1]/2)
	pasteLocation = (5, yDim - letterImageSize[1] - 5)
	pasteText(mainImage, textImage, pasteLocation)

def applyTextToFullMap(mainImage):
	# get mainImage dimensions
	xDim, yDim = mainImage.size
	xSegments = xDim // 500
	ySegments = yDim // 500
	for xIndex in range(xSegments):
		for yIndex in range(ySegments):
			segmentText = getSegmentText(xIndex, yIndex)
			textImage = createTextImage(segmentText)
			xPasteLocation = xIndex * 500 + 250
			yPasteLocation = yIndex * 500 + 250 - letterImageSize[1]//2
			pasteLocation = (xPasteLocation, yPasteLocation)
			pasteText(mainImage, textImage, pasteLocation)

def saveMainImage(mainImage, filename):
	try:
		mainImage.save(filename, quality=100, optimize=True, progressive=True)
		# mainImage.show()
	except:
		print("Failed to save image.")
		exit(1)

def processImage(input_filename, output_filename="", method="keymap", keymapText = ""):
	# get main image
	mainImage = getMainImage(input_filename)
	# applyText to mainImage
	if 	method == "keymap":
		applyTextToKeymap(mainImage, keymapText)
	elif method == "fullmap":
		applyTextToFullMap(mainImage)
	# save or show
	if not output_filename:
		output_filename = input_filename
	saveMainImage(mainImage, output_filename)

### AUX FUNCTION - GLOB ###

def getFileNames():
	return glob.glob("images/map_*.png")

def getCoords(filenames):
	nums = map(lambda s: s.split(".")[0].split("_")[1].lstrip("(").rstrip(")"), filenames)
	nums_left = map(lambda s: int(s.split(",")[0]), nums)
	nums_right= map(lambda s: int(s.split(",")[1]), nums)
	numsInt = zip(nums_left, nums_right)
	return numsInt

def processAllKeyMaps():
	print("Attaching text to key maps.")
	filenames = getFileNames()
	numsInt = getCoords(filenames)
	fileNamesWithCoords = zip(filenames, numsInt)

	for filename, coords in fileNamesWithCoords:
		yIndex = coords[0]
		xIndex = coords[1]
		segmentText = getSegmentText(xIndex, yIndex)
		processImage(filename, method="keymap", keymapText=segmentText)

def processFullMap():
	print("Attaching text to full map.")
	mapFull_filename = "images/mapFullGrid.jpeg"
	processImage(mapFull_filename, method = "fullmap")

# Attach text to keymaps
processAllKeyMaps()
# Attach text to mapFull
processFullMap()

### MAIN ###
# processImage("pic2.png", method = "keymap")
# processImage("largemap.jpeg", "largemapKeys.jpeg", method = "fullmap")
