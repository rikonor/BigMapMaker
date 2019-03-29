import glob
from PIL import Image

def getFileNames():
	return glob.glob("images/map_*.png")

def getFiles(file_names):
	return [Image.open(fname) for fname in file_names]

file_names = getFileNames()

nums = list(map(lambda s: s.split(".")[0].split("_")[1].lstrip("(").rstrip(")"), file_names))
nums_left = list(map(lambda s: int(s.split(",")[0]), nums))
nums_right= list(map(lambda s: int(s.split(",")[1]), nums))
numsInt = zip(nums_left, nums_right)
numOfRows = max(nums_left)+1
numOfColumns = max(nums_right)+1
print("Log: Detected %d columns, %d rows" % (numOfColumns, numOfRows))

fileNamesWithCoords = zip(file_names, numsInt)

files = getFiles(file_names)
filesWithCoords = zip(files, numsInt)

print("Log: Creating imgFull with size (%d,%d)." % (numOfColumns, numOfRows))
imgFull = Image.new('RGB', (500*numOfColumns, 500*numOfRows))

for img, coords in filesWithCoords:
	y = coords[0]
	x = coords[1]
	box = (500*x, 500*y, 500+500*x, 500+500*y)
	imgFull.paste(img, box)

# imgFull.save("images/mapFull.jpeg", "JPEG")
imgFull.save("images/mapFull.jpeg", quality=100, optimize=True, progressive=True)
