#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Felix Postma 2021

# This script retrieves the time and name of audio clips from an Ableton session file (.als),
# and prints this out in a tracklist format that is suitable for pasting into Mixcloud.


from tkinter import *
from tkinter import filedialog
import subprocess
import os
from xml.etree import ElementTree as ET
import math
import re


## initialise dialog window
tk = Tk()
tk.title('Ignore me pls')
## hide root GUI window
tk.withdraw()

## choose .als
tk.filename = filedialog.askopenfilename(initialdir="/", title="Select an Ableton session file", filetypes=(("ALS files", "*.als"), ("All files", "*.*")))

## tk.mainloop() not necessary!
m = re.search('\.als$', tk.filename)
if not m:
	print("No ALS file selected!")
	exit()

## gzip to get xml from als
p = subprocess.run(['gunzip', '-c', tk.filename], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

## get xml data
root = ET.fromstring(p.stdout)

## create tracklist list
tracklist = []

## create .txt file in .als folder
txtname = re.sub('\.als$', ' tracklist.txt', tk.filename)
if os.path.exists(txtname):
    os.remove(txtname)

## find all clips in arrangement view
for sample in root.iter('Sample'):
	for clip in sample.iter('AudioClip'):
		## get time in beats (assuming 120 bpm!!) and convert to minutes
		time = float(clip.get('Time')) / 120.0
		## get name
		name = clip.find('Name').get('Value')
		## remove album titles and such, anything thats not artist or title
		name = re.sub('\s[-_]\s.*\s[-_]\s', ' - ', name)	
		tracklist.append([time, name])

## create key to sort by time
def timekey(e):
	return e[0]

## sort according to time
tracklist.sort(key=timekey)

## isolate .als file name from full path
alsname = re.search('[^/]+\.als$', tk.filename)[0]

## get number of samples found in ableton session
n = len(tracklist)
print("Found "+str(n)+" tracks in "+alsname+".")

## Check whether a tracklist can actually be made (>0 tracks)
if n == 0:
	## session is empty
	print("No tracklist has been created.")
else:
	## create MM:SS timestamp, and print!
	for track in tracklist:
		time = track[0]
		mins = math.floor(time)
		secs = round((time % 1) * 60)
		## add a leading 0 if seconds is a single digit
		secsstr = str(secs)
		if len(secsstr) == 1: 
			secsstr = '0'+secsstr
		timestamp = str(mins)+':'+secsstr
		name = track[1]
		## print to tracklist.txt
		print(name, timestamp, file=open(txtname, 'a'))

	print("Created tracklist at "+txtname)
