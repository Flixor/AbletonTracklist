#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Felix Postma 2020

from tkinter import filedialog
from xml.etree import ElementTree as ET

tk = Tk()
tk.title('Find ALS')

# how to get to directory?

tk.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("Ableton session files", "*.als"),("all files", "*.*")))

tk.mainloop()

# gzip to make xml


# get xml elements


# print to txt


# remove xml



