from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import pygame
import RPi.GPIO as GPIO

STATE="mainMenu"
BUTTON1 = 0
BUTTON2=False
BUTTON3=False

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
#interrupt service routines
def isr1(channel):
    global BUTTON1
    BUTTON1 = 1
    print("Button 1")
def isr2(channel):
    global BUTTON2
    BUTTON2 = True
    print("Button 2")
def isr3(channel):
    global BUTTON3
    BUTTON3 = True
    print("Button 3")

#GPIO
def initGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(17, GPIO.FALLING,callback=isr1, bouncetime=200)
    GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(26, GPIO.FALLING,callback=isr2, bouncetime=200)
    GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(22, GPIO.FALLING,callback=isr3, bouncetime=200)

initGPIO()
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
    #check for inputs
    #inputs are reset at the end of functions 
    if BUTTON1 == 1:
        STATE = "lesson1"
        print("lesson1")
        BUTTON1 = False
    elif BUTTON2:
        STATE = "lesson2"
        BUTTON2 = False
    elif BUTTON3:
        STATE = "mainMenu"
        BUTTON3 = False

