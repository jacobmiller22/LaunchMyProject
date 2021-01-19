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


# temp = {
#     "action": "ADD",
#     "payload": {
#         "project": {
#             "title": "My project title",
#             "description": "tbd",
#             "os": {
#                 "windows": {
#                     "path": "C:\\Users\\jacob\\Documents\\Projects\\StartMyProject",
#                     "editor-cmd": "code .",
#                     "scripts": {
#                         "cmds": [""],
#                         "bash-scripts": []
#                     }
#                 }
#             }
#         }
#     }
# }




def parseArg(args: dict):

    action = args["action"]

    if(action == "ADD"):
        print("Add project")
    elif(action == "RM"):
        print("Remove Project")
    elif(action == "EDIT"):
        print("Edit Project")
    elif(action == "START"):
        print("Start Project")
        return args["payload"]["project"]

    print("Parsing arguments")







def start(selected: dict):
    
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
        openTerminal = 'start cmd.exe /k "{} && cd {}"'.format(path[:2], path)
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
    if plat == "macOS":
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
            os.system('start cmd.exe /k "{} && cd {} && {}"'.format(path[:2], path, cmd))
    
    elif plat == "Linux":
        # We are on Linux
        print("Run commands on Linux not yet supported")
    else:
        sys.exit("Unknown OS, please report. 0-1")
    
    # Finished. Print Ascii Art
    asciiArt = ".  .            .  .      .         \n|__| _.._ ._   .|__| _. _.;_/*._  _ \n|  |(_][_)[_)\_||  |(_](_.| \|[ )(_]\n       |  |  ._|                 ._|\n"
    print(asciiArt)
    print("Project {}, has started. Happy Hacking".format(title))
    
    
    if(selected == None):
        sys.exit("No project was selected. Exiting")

