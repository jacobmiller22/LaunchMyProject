#!/usr/bin/python

import os
import json
import subprocess
import sys
import platform
import applescript
from tkinter  import *


# Load project data

absPath = os.path.dirname(os.path.abspath(__file__))

with open("{}/projects.json".format(absPath)) as f:
    projects = json.load(f)

def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)

def getSel():
    return str(var.get())

root = Tk()
var = StringVar()

for project in projects:
    title = project["title"]
    radio = Radiobutton(root, text=title, variable=var, value=title, command=sel)
    radio.pack( anchor = W)


label = Label(root)
label.pack()
root.mainloop()

print("----------------------------------------")
# Load selected project data

def selectProject():
    for project in projects:
        if project["title"] == getSel():
            return project

selected = selectProject()
title = selected["title"]
plat = platform.system()
global path
global editor
global fileSys
global openTerminal


if plat == "Darwin":
    # We are on MacOS
    print("Using MacOS")
    plat = "macOS"
    path = selected["os"][plat]["path"]
    editor = selected["os"][plat]["editor"]
    fileSys = "finder"
    openTerminal = "open {}".format(path)
elif plat == "Windows":
    # We are on Windows
    print("Using Windows")
    plat = "windows"
    path = selected["os"][plat]["path"]
    editor = selected["os"]["windows"]["editor"]
    fileSys = "explorer"
    openTerminal = "start cmd & cd {}".format(path)
elif plat == "Linux":
    # We are on Linux
    print("Using Linux")
    plat = "linux"
else:
    sys.exit("Unknown OS, please report")


print("Loading {}\nFrom: $> {}\n".format(title, path))

# Open Editor
subprocess.Popen("code {}".format(path), shell=True,
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Open File System
subprocess.Popen('{} {}'.format(fileSys, path), shell=True,
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Open cmd/terminal
os.system(openTerminal)

## Execute any commands
# mac
script = selected["os"][plat]["scripts"]["cmds"][0]
applescript.tell.app( 'Terminal', 'do script "' + script + '"') 



# Maybe have an ascii image here?
asciiArt = ".  .            .  .      .         \n|__| _.._ ._   .|__| _. _.;_/*._  _ \n|  |(_][_)[_)\_||  |(_](_.| \|[ )(_]\n       |  |  ._|                 ._|\n"
print(asciiArt)
print("Project {}, has started. Happy Hacking".format(title))
