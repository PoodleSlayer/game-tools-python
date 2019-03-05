from tkinter import filedialog
from tkinter import *
import os

# This script helps to cleanup .meta files in Unity projects.
# In my specific case I added a bunch of sprites that had " (n)"
# appended to the end for duplicate file names so I wanted to
# remove the spaces and parentheses.
# Example:
#    "player (1).png" becomes "player_1.png"
#
# To use, simply browse to the folder with .meta files you wish to
# clean up. tkinter is handy.

Tk().withdraw()
folderpath = filedialog.askdirectory()
print(folderpath)

for filename in os.listdir(folderpath):
	if not filename.endswith(".meta"):
		newName = filename
		newName = newName.replace("(", "")
		newName = newName.replace(")", "")
		newName = newName.replace(" ", "_")
		filepath = folderpath + "/" + filename
		newpath = folderpath + "/" + newName
		print(filepath)
		print(newpath)
		os.rename(filepath, newpath)