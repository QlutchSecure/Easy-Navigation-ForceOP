import webbrowser
import time 
import pyfiglet
import os
from tkinter import *

def forumsopen():
    URL = 'https://minecraftforceop.com/forums'
    webbrowser.open(URL)
def forceopopen():
    URL = 'https://minecraftforceop.com'
    webbrowser.open(URL)
def wikiopen():
    URL = 'https://minecraftforceop.com/forums/wiki'
    webbrowser.open(URL)
def downloadsopen():
    URL = 'https://minecraftforceop.com/forums/downloads/'
    webbrowser.open(URL)
def changelogopen():
    URL = 'https://minecraftforceop.com/forums/forums/2'
    webbrowser.open(URL)
def bugreportsopen():
    URL = 'https://minecraftforceop.com/forums/forums/7/'
    webbrowser.open(URL)
def serversopen():
    URL = 'https://minecraftforceop.com/forums/forums/30/'
    webbrowser.open(URL)
def requestsopen():
    URL = 'https://minecraftforceop.com/forums/forums/31/'
    webbrowser.open(URL)
def DandGopen():
    URL = 'https://minecraftforceop.com/forums/forums/21/'
    webbrowser.open(URL)
def CandGopen():
    URL = 'https://minecraftforceop.com/forums/forums/20/'
    webbrowser.open(URL)
def videosopen():
    URL = 'https://minecraftforceop.com/forums/forums/19/'
    webbrowser.open(URL)
def servicesopen():
    URL = 'https://minecraftforceop.com/forums/forums/28/'
    webbrowser.open(URL)
def productsopen():
    URL = 'https://minecraftforceop.com/forums/forums/29/'
    webbrowser.open(URL)
def installingopen():
    URL = 'https://minecraftforceop.com/forums/forums/6/'
    webbrowser.open(URL)
def codingopen():
    URL = 'https://minecraftforceop.com/forums/forums/12/'
    webbrowser.open(URL)
def OTandGopen():
    URL = 'https://minecraftforceop.com/forums/forums/17/'
    webbrowser.open(URL)

class App:
    def __init__(self, master):


        frame = Frame(master)
        frame.pack()
        frame.configure(background="#000000")

        self.button = Button(frame, text="Exit", bg="#000000", fg="#ffffff", font="none 18", command=quit)
        self.button.pack(side=BOTTOM)

        self.button = Button(frame, text="Wiki", bg="#000000", fg="#ffffff", font="none 18", command=wikiopen)
        self.button.pack(side=BOTTOM)

        self.button = Button(frame, text="Server", bg="#000000", fg="#ffffff", font="none 18", command=serversopen)
        self.button.pack(side=BOTTOM)

        self.button = Button(frame, text="Videos", bg="#000000", fg="#ffffff", font="none 18", command=videosopen)
        self.button.pack(side=BOTTOM)

        self.button = Button(frame, text="Coding", bg="#000000", fg="#ffffff", font="none 18", command=codingopen)
        self.button.pack(side=BOTTOM)

        self.button = Button(frame, text="Forums", bg="#000000", fg="#ffffff", font="none 18", command=forumsopen)
        self.button.pack(side=BOTTOM)

        self.button = Button(frame, text="Services", bg="#000000", fg="#ffffff", font="none 18", command=servicesopen)
        self.button.pack(side=BOTTOM)

        self.button = Button(frame, text="ForceOP", bg="#000000", fg="#ffffff", font="none 18", command=forceopopen)
        self.button.pack(side=BOTTOM)

        self.button = Button(frame, text="Products", bg="#000000", fg="#ffffff", font="none 18", command=productsopen)
        self.button.pack(side=BOTTOM)

        self.button = Button(frame, text="Installing", bg="#000000", fg="#ffffff", font="none 18", command=installingopen)
        self.button.pack(side=BOTTOM)

        self.button = Button(frame, text="Requests", bg="#000000", fg="#ffffff", font="none 18", command=requestsopen)
        self.button.pack(side=BOTTOM)

        self.button = Button(frame, text="Changelog", bg="#000000", fg="#ffffff", font="none 18", command=changelogopen)
        self.button.pack(side=BOTTOM)

        self.button = Button(frame, text="Downloads", bg="#000000", fg="#ffffff", font="none 18", command=downloadsopen)
        self.button.pack(side=BOTTOM)

        self.button = Button(frame, text="Bug Report", bg="#000000", fg="#ffffff", font="none 18", command=bugreportsopen)
        self.button.pack(side=BOTTOM)

        self.button = Button(frame, text="Discussion & Games", bg="#000000", fg="#ffffff", font="none 18", command=DandGopen)
        self.button.pack(side=BOTTOM)

        self.button = Button(frame, text="Contests & Giveaways", bg="#000000", fg="#ffffff", font="none 18", command=CandGopen)
        self.button.pack(side=BOTTOM)

        self.button = Button(frame, text="Other Tutorials/guides", bg="#000000", fg="#ffffff", font="none 18", command=OTandGopen)
        self.button.pack(side=BOTTOM)


root = Tk()
root.title("Easy Navigation")
root.configure(background="#000000")
root.geometry('580x880')

app = App(root)
Label(root, text="Easy Navigation To ForceOP", bg="#000000", fg="#ffffff", font="none 18").pack()

root.mainloop()
