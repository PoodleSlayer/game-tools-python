import os
from tkinter import filedialog
from tkinter import *
from PIL import Image

def genPalette(file):
	# get some useful file I/O strings
	filename = os.path.basename(file)
	pathWithoutExt = os.path.splitext(file)[0]
	fileWithoutExt = os.path.splitext(filename)[0]
	outputPath = os.path.dirname(os.path.splitext(pathWithoutExt)[0])
	outputPath = os.path.dirname(outputPath) + "/output/"
	outputFile = outputPath + fileWithoutExt + "_palette.txt"

	#print(filename + ", " + fileWithoutExt)
	print("output to " + outputFile)

	colorList = []

	im = Image.open(file).convert('RGB')

	width, height = im.size
	for x in range(width):
		for y in range(height):
			r, g, b = im.getpixel((x, y))
			if (r,g,b) not in colorList:
				colorList.append((r,g,b))

	# write the RGB list to a file
	with open(outputFile, "w") as outFile:
		for rgb in colorList:
			outFile.write(str(rgb) + "\n")


Tk().withdraw()
inputFile = filedialog.askopenfilename(title = "Select PNG", filetypes = [("PNG files","*.png")] )
if inputFile:
	genPalette(inputFile)
else:
	print("Please select a file!")
