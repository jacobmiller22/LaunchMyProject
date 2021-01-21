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


def create_project_struct(title: str, description: str, os: str, path: str, editor_cmd: str, cmds: [str]):
    print("Creating Project")


@click.group()
def smp():
    """A CLI wrapper for StartMyProject"""
    pass


@click.option('-t', '--title', help='Name of API (matches via substring - i.e. "at" would return "cat" and "atlas".')
@click.option('-l', '--lim', default=None, help='Limit the number of projects that are listed')
@click.option('-A', '--show-All', is_flag=True, help='Show all projects that are listed')
@smp.command()
def li(title: str, lim: int, show_all: str):
    """List projects, Prints all project if a limit is not defined."""
    p = 1
    for i in range(len(projects)):
        if(i == lim):
            break
        p = i
        if(p % 5 == 0 and p != 0 and not show_all):
            valid = True
            while valid:
                res = input(
                    "Continue listing? {} more projects to display (y/n)".format(len(projects) - i))
                if(res.lower() in "yes"):
                    break
                elif(res.lower() in "no"):
                    valid = False
                    break
            if(not valid):
                break
        print(projects[i]["title"])


@click.argument('project_title')
@smp.command()
def start(project_title: str):
    """Start project [PROJECT_TITLE]"""
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

    # Create new project
    title = input("Project title? ")
    description = input("Project summary? ")
    os = input("Platform? (macos, windows, or linux) ")
    path = input("Absolute path to project: ")
    editor_cmd = input(
        'Command to open editor (use "Code ." to open vscode): ')

    project_to_add = {}

    args = {
        "action": "REMOVE",
        "payload": {
            "projects": projects,
            "project": project_to_add
        }
    }


@click.argument('project_title')
@config.command()
def rm(project_title: str):
    """ Goes through the process of removing a project from the project list """
    project_to_remove = selectProject(project_title)

    if(project_to_remove == None):
        print('Project "{}", does not exist.'.format(project_title))
        return

    args = {
        "action": "REMOVE",
        "payload": {
            "projects": projects,
            "project": project_to_remove
        }
    }

    driver.rm(driver.parseArg(args))


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
