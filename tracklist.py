#!/usr/bin/env python3
# -*- coding: utf-8 -*-

### Felix Postma 2020

import subprocess
from tkinter import *
from tkinter import filedialog
import subprocess
from xml.etree import ElementTree as ET


# initialise dialog window
tk = Tk()
tk.title('Find ALS')

# choose .als
tk.filename = filedialog.askopenfilename(initialdir="/Users/flixor/Projects/AbletonTracklist", title="Select A File", filetypes=(("Ableton session files", "*.als"),("all files", "*.*")))
# tk.mainloop() not necessary!
print(tk.filename)

# /Users/flixor/Projects/AbletonTracklist/test.als

# gzip to make xml
# p = subprocess.run(["gzip", "-cd", tk.filename], capture_output=True, shell=True)

# get xml elements


# print to txt


# remove xml



