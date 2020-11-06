#!/usr/bin/env python3
# -*- coding: utf-8 -*-

### Felix Postma 2020
# This script retrieves the time and name of audio clips rom an ableton session file,
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
# tk.filename = '/Users/flixor/Projects/AbletonTracklist/test.als'

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
os.remove(txtname)

## create .m3u file in .als folder
m3uname = re.sub('\.als$', ' playlist.m3u', tk.filename)
os.remove(m3uname)
print('#EXTM3U', file=open(m3uname, 'a'))

## find the clips 
for clip in root.iter('AudioClip'):
	## get time in beats (assuming 120 bpm!!) and convert to minutes
	time = float(clip.get('Time')) / 120.0
	## get name
	name_unclean = clip.find('Name').get('Value')
	## for proper tracklist: remove anything at the end of the name that matches 'my free mp3...'
	name = re.sub('\smy[\s-]*free[\s-]*mp3[a-z.]*\s*$', '', name_unclean)
	## remove album titles and such, anything thats not artist or title
	name = re.sub('\s[-_]\s.*\s[-_]\s', ' - ', name)	
	tracklist.append([time, name, name_unclean])

## create key to sort by time
def timekey(e):
	return e[0]

## sort according to time
tracklist.sort(key=timekey)


## create timestamp, and print!
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
	print(timestamp, name)
	## print to tracklist.txt
	print(timestamp, name, file=open(txtname, 'a'))
	## print unedited name to m3u playlist
	name_unclean = track[2]
	print('#EXTINF:0,'+name_unclean+'.mp3', file=open(m3uname, 'a'))
	print(re.sub(' ', '%20', name_unclean)+'.mp3', file=open(m3uname, 'a'))



