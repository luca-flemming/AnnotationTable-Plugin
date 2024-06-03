from ij import IJ, WindowManager 
from ij.gui import GenericDialog
from ij.gui import StackWindow
from ij.plugin import Hotkeys
from ij.measure import ResultsTable

# ----- CHANGE FPS HERE -----
fps = 30


# ----- Display FPS Reminder -----
if IJ.getLog() is None:
	IJ.log("Remember to adjust the FPS value in the script file\n" + "FPS are currently set to " + str(fps))


# ----- Get Current Frame -----
imp = IJ.getImage()
#imp.getOriginalFileInfo().directory
current_frame = StackWindow(imp).getImagePlus().currentSlice


# ----- Add to Log -----
time = float(current_frame) / float(fps)
if fps < 10:
    rounded_time = round(time, 1)
elif fps < 100:
	rounded_time = round(time, 2)
elif fps < 1000: 
	rounded_time = round(time, 3)
else:
	rounded_time = round(time, 4)
	
IJ.log(str(rounded_time))


