# Python Timelapse Maker
Python timelapse maker with quasi-GUI

Dependencies: 

1- Pillow (pip install pillow)

2- OpenCV2 (pip install opencv-python)

3- glob (pip install glob2)

Usage: Executing the program pops window to select directory, files in that directory can be seen in the Gui, and rotation can be applied to EVERY image in the folder.

The images are loaded in alphabetical order and that is the order in which they are added to the result video, the default framerate is 30 (to change this, edit line 72 on the .py)

Generated video is saved on the directory of the images with the name entered in the command line.
