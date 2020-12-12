#!/usr/bin/python

import os
import json
import subprocess


# Load project data
with open("./projects.json") as f:
    projects = json.load(f)

print(projects)
print("\n\n")
# Load the first project
title = projects[0]["title"]
path = projects[0]["os"]["windows"]["path"]

print("Loading {}\nFrom: $> {}\n".format(title, path))

exit_code = os.system("cd {}".format(path))

editor = projects[0]["os"]["windows"]["editor"]

# Open Editor
if(editor == "vscode"):
    print("opening with vscode")
    subprocess.Popen("code {}".format(path), shell=True,
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# Open File explorer or Finder
# subprocess.Popen('explorer {}'.format(path))

# Open Command Prompt
os.system("start cmd & cd {}".format(path))

# Execute any commands
cmds = []
cmds.append("cd {}\\server".format(path))
script = projects[0]["os"]["windows"]["scripts"]["cmds"][0]
print(cmds)
print(path)
# os.system("start \"\" cmd /k \"cd /D C:\\ & color 04\"".format(path, command))
# subprocess.Popen("cd {} && {}".format(path, command), shell=True,
#                  stdout=subprocess.PIPE, stderr=subprocess.PIPE)

subprocess.Popen(["cd {}\\server".format(
    path), "{}".format(script)], shell=True)


print("finished")
