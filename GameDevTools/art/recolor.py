import os
from tkinter import filedialog
from tkinter import *
from PIL import Image

def recolor(file, themeName):
	# get some useful strings
	# file is the full path and filename
	filename = os.path.basename(file)
	pathWithoutExt = os.path.splitext(file)[0]
	fileWithoutExt = os.path.splitext(filename)[0]
	outputPath = os.path.dirname(os.path.splitext(pathWithoutExt)[0])
	outputPath = os.path.dirname(outputPath) + "/output/"

	# for testing just exit here to avoid image processing
	#return

	print("recoloring " + filename)
	#print(file)
	#print(fileWithoutExt)
	im = Image.open(file).convert('RGB')

	width, height = im.size
	for x in range(width):
		for y in range(height):
			r, g, b = im.getpixel((x, y))

			tempKey = -1
			for key, value in originalMap.items():
				if value == (r,g,b):
					tempKey = key
					break
			
			r2, g2, b2 = (0,0,0)
			if tempKey != -1:
				r2,g2,b2 = newMap[tempKey]
				im.putpixel((x,y),(r2,g2,b2))

	im.save(outputPath + fileWithoutExt + "_" + themeName + ".png")


Tk().withdraw()
inputFolder = filedialog.askdirectory()
print(inputFolder)

# make a map of RGB values to convert between
#
# (0,0,0) outlines
# (25,25,25) highlights on outlines
# (51,51,51) background
#
# (0,127,14) gradient, dark end
# (0,200,0) gradient
# (0,255,33) gradient
# (255,255,255) gradient, light end
originalMap = {
	0 : (0,0,0),
	1 : (25,25,25),
	2 : (51,51,51),
	3 : (0,127,14),
	4 : (0,200,0),
	5 : (0,255,33),
	6 : (255,255,255)
	}
newMap = {
	0 : (0,0,0),
	1 : (25,25,25),
	2 : (51,51,51),
	3 : (0,14,127),
	4 : (0,0,200),
	5 : (0,33,255),
	6 : (255,255,255)
	}
theme = "blue"

for filename in os.listdir(inputFolder):
	recolor(inputFolder + "/" + filename, theme)
