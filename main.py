from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import pygame

STATE="mainMenu"
#init PREV_STATE to null 
PREV_STATE="null"
root = Tk()
root.geometry("1000x700")

def mainMenu():
    mainMenuFrame = Frame(root, bg='#F5F5F5', bd=5)
    mainMenuFrame.place(relx=0.2,rely=0, relwidth=0.6,relheight=0.16)
    mainMenuLabel = Label(mainMenuFrame, text="Main menu", bg='black', fg='white', font=('Arial',30))
    mainMenuLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


def exampleLesson1():
    exampleLesson1Frame = Frame(root, bg='#F5F5F5', bd=5)
    exampleLesson1Frame.place(relx=0.2,rely=0, relwidth=0.6,relheight=0.16)
    exampleLesson1Label = Label(exampleLesson1Frame, text="example Lesson 1", bg='black', fg='white', font=('Arial',30))
    exampleLesson1Label.place(relx=0,rely=0, relwidth=1, relheight=1)

def exampleLesson2():
    exampleLesson2Frame = Frame(root, bg='#F5F5F5', bd=5)
    exampleLesson2Frame.place(relx=0.2,rely=0, relwidth=0.6,relheight=0.16)
    exampleLesson2Label = Label(exampleLesson2Frame, text="example Lesson 2", bg='black', fg='white', font=('Arial',30))
    exampleLesson2Label.place(relx=0,rely=0, relwidth=1, relheight=1)

#### Audio 
def initAudio():
    pygame.mixer.init()

def playAudio(voicefile):
    pygame.mixer.music.load(voicefile)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

initAudio()
    
while True:
    #check for change in state

    if PREV_STATE != STATE:
        if(STATE=="mainMenu"):
            mainMenu()
            audiofile = "main_menu_voice.mp3"
        if(STATE=="lesson1"):
            exampleLesson1()
            audiofile = "example_lesson_1_voice.mp3"
        if(STATE=="lesson2"):
            exampleLesson2()
            audiofile = "example_lesson_2_voice.mp3"
        root.update()
        playAudio(audiofile)
        PREV_STATE = STATE
    
    #poll for io changes
    STATE = "lesson2"

    



    