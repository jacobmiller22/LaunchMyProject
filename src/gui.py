from tkinter import * 
import tkinter as tk
# Create gui


class GUI: 
    def __init__(self, main, projects):
        self.main = main
        self.selected = ""
        self.build(projects=projects)

        

    def build(self, projects):
        self.main.title = "RunMyProject"
        self.label = Label(self.main, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(self.main, text="Greet", command=self.greet)
        self.greet_button.pack()
        self.buildProjects(projects=projects)

        self.close_button = Button(self.main, text="Close", command=self.main.quit)
        self.close_button.pack()
        

    def sel(self):
        self.selected = str(var.get())

    var = StringVar()
    def buildProjects(self, projects):

        # projectRadios = []
        
        for project in projects:

            title = project["title"]
            radio = tk.ttk.Radiobutton(self.main, text=title, variable=var, value=title, command=sel)
            radio.pack()
            # projectRadios.append(radio)

    def getSelected(self):
        return self.selected



    def greet(self):
        print("Greetings!")

