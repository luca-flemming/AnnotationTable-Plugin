# AnnotationTable-Plugin for ImageJ/FIJI

This small tool helps you to create annotation tables for [AutoGaitA](https://github.com/mahan-hosseini/AutoGaitA) a toolbox for kinematic analysis of pose estimation data.

After opening a video in ImageJ/Fiji you can save a series of timepoints within a log window at the press of a button. After going through a whole video a list of time points can then be copied and transposed into your annotation table excel file.

## How to set up:
1. First you have to move the “AnnotationTable_Plugin.py” file into the “plugins” folder. To open this folder go to File -> Show Folder -> Plugins.
  <img src="https://github.com/luca-flemming/AnnotationTable-Plugin/blob/main/IMAGES/img1.png" width="700" height="460"/>

2. Next open ImageJ/Fiji and go to Plugins -> Shortcuts -> Add Shortcut...
  <img src="https://github.com/luca-flemming/AnnotationTable-Plugin/blob/main/IMAGES/img2.png" width="700" height="460"/>

3. Then choose a hotkey and select “AnnotationTable-Plugin” from the dropdown menu.
  <img src="https://github.com/luca-flemming/AnnotationTable-Plugin/blob/main/IMAGES/img3.png" width="525" height="345"/>

   Click “okay” and restart ImageJ/Fiji
 
## How to use:
1. Before opening ImageJ/Fiji you need to update the FPS number that the script uses for calculation according to your video.
To do this you open the AnnotationScript.py file (with the text editor on Mac, or Notepad on Windows), adjust the number and save.
If you changed the FPS after opening ImageJ/Fiji you need to restart the program.
  <img src="https://github.com/luca-flemming/AnnotationTable-Plugin/blob/main/IMAGES/img4.png" width="700" height="290"/>

2. Now you can start ImageJ/Fiji and open a video. After pressing your hotkey a log window will open in which the time point is recorded in seconds with as many decimals as needed by AutoGaitA for the specific frame rate. With each press you create a new time point.
  <img src="https://github.com/luca-flemming/AnnotationTable-Plugin/blob/main/IMAGES/img5.png" width="700" height="460"/>
   
   If you accidentally saved the wrong time point you can correct this by simply clicking on the value and pressing delete.

  <img src="https://github.com/luca-flemming/AnnotationTable-Plugin/blob/main/IMAGES/img6.png" width="525" height="345"/>

3. Once you are done with the whole video you can select all the time points in the log window and copy them in the annotation table excel sheet.
  <img src="https://github.com/luca-flemming/AnnotationTable-Plugin/blob/main/IMAGES/img7.png" width="525" height="345"/>

   In order to transpose them into the corresponding row you need to paste them into an empty area and select and copy them again. Otherwise transpose won’t work unfortunately.
  <img src="https://github.com/luca-flemming/AnnotationTable-Plugin/blob/main/IMAGES/img8.png" width="700" height="460"/>


## License:

The AnnotationTable plugin is licensed under GPL v3.0 

This plugin is provided without warranty of any kind, express or implied, including, but not limited to, the implied warranty of fitness for a particular purpose.
  
