#!/usr/bin/env python

import os
import json
import click
import subprocess
import pathlib
import driver



# OPEN PROJECT DATA FILE
absPath = os.path.dirname(os.path.abspath(__file__))
with open("{}/projects.json".format(absPath)) as f:
    projects = json.load(f)


def selectProject(title: str):
    for project in projects:
        if project["title"] == title:
            return project




@click.group()
def smp():
    """A CLI wrapper for StartMyProject"""
    pass


@click.option('-t', '--title', help='Name of API (matches via substring - i.e. "at" would return "cat" and "atlas".')
@click.option('-l', '--lim', default=100, help='Limit the number of projects that are listed')
@smp.command()
def li(title: str, lim: int):
    """List projects, Prints all project if a limit is not defined."""
    for i in range(len(projects)):
        if(i == lim):
            break
        print(projects[i]["title"])


@click.argument('project_title')
@smp.command()
def start(project_title: str):
    """Start a Project."""
    print("Starting {}".format(project_title))

    args = {
        "action": "START",
        "payload": {
            "project": selectProject(project_title)
        }
    }
    
    driver.start(driver.parseArg(args))


@smp.group()
def config():
    """ A Wrapper for adding, removing, and configuring projects """
    pass


@config.command()
def add():
    """ Goes through the process of adding a project to the project list """
    print("Add")


@config.command()
def rm():
    """ Goes through the process of removing a project from the project list """
    print("Remove")


@config.command()
def edit():
    """ Goes through the process of editing a project in the project list """
    print("Edit")


if __name__ == '__main__':
    smp(prog_name="smp")


# temp = {
#     "action": "START",
#     "payload": projects["title"]
# }

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
