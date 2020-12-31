#!/usr/bin/python

import os
import json
import subprocess
import sys
import platform
try:
    import applescript
except ImportError:
    print("applescript not found. Skipping module")
from tkinter  import *


## OPEN PROJECT DATA FILE
absPath = os.path.dirname(os.path.abspath(__file__))
with open("{}/projects.json".format(absPath)) as f:
    projects = json.load(f)

## CREATE GUI

def sel():
    btn_launch.config(text="Launch "+str(var.get()))

def getSel():
    return str(var.get())

def setSel(newVar):
    var.set(newVar)

root = Tk() # Create Window
root.title("StartMyProject")
root.rowconfigure(0, minsize=250, weight=1)
root.columnconfigure(0, minsize=250, weight=1)

frm_projects = Frame(master=root) # Creates a frame for our project options
lbl_projects = Label(master=frm_projects, text="Projects")
lbl_projects.pack(side=TOP)
var = StringVar()
for project in projects:
    title = project["title"]
    radio = Radiobutton(master=frm_projects, text=title, variable=var, value=title, command=sel)
    radio.pack( anchor = W)

# Selects the first project in the list
if(len(projects)>0):
    setSel(projects[0]["title"])

frm_projects.grid(row=0,column=0,padx=5,pady=5)

def launch():
    root.destroy()

frm_launch = Frame(master=root) # Create a frame for launch
btn_launch = Button(master=frm_launch,text="Launch {}".format(getSel()),fg="blue", command=launch)
btn_launch.pack(side=BOTTOM)
frm_launch.grid(row=1,column=0,padx=5,pady=5)

root.mainloop() # Create the GUI

print("----------------------------------------")
# Load selected project data

def selectProject():
    for project in projects:
        if project["title"] == getSel():
            return project

selected = selectProject()
if(selected == None):
    sys.exit("No project was selected. Exiting")
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
    editor = selected["os"][plat]["editor-cmd"]
    fileSys = "finder"
    openTerminal = "open {}".format(path)
elif plat == "Windows":
    # We are on Windows
    print("Using Windows")
    plat = "windows"
    path = selected["os"][plat]["path"]
    editor = selected["os"]["windows"]["editor-cmd"]
    fileSys = "explorer"
    openTerminal = 'start cmd.exe /k "cd {}"'.format(path)
elif plat == "Linux":
    # We are on Linux
    print("Using Linux")
    plat = "linux"
else:
    sys.exit("Unknown OS, please report. 0-0")

print("Loading {}\nFrom: $> {}\n".format(title, path))

# Open Editor
subprocess.Popen("code {}".format(path), shell=True,
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Open File System
subprocess.Popen('{} {}'.format(fileSys, path), shell=True,
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Open cmd/terminal
os.system(openTerminal)

## Execute any scripts
cmds = selected["os"][plat]["scripts"]["cmds"]

if plat == "Darwin":
    # We are on MacOS
    for cmd in cmds:
        script = "cd {} && {}".format(path, cmd)
        applescript.tell.app( 'Terminal', 'do script "' + script + '"') 
elif plat == "windows":
    # We are on Windows
    for cmd in cmds:
        # subprocess.Popen(args='{}'.format(cmd), cwd=path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # subprocess.Popen(args='dir', cwd=path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # os.system('cmd /k "cd {} && {}"'.format(path, cmd))
        driveLetter = path[:2]
        os.system('start cmd.exe /k "cd {} && {}"'.format( path, cmd))

elif plat == "Linux":
    # We are on Linux
    print("Run commands on Linux not yet supported")
else:
    sys.exit("Unknown OS, please report. 0-1")

# Finished. Print Ascii Art
asciiArt = ".  .            .  .      .         \n|__| _.._ ._   .|__| _. _.;_/*._  _ \n|  |(_][_)[_)\_||  |(_](_.| \|[ )(_]\n       |  |  ._|                 ._|\n"
print(asciiArt)
print("Project {}, has started. Happy Hacking".format(title))
