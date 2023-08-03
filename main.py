from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import pygame
import RPi.GPIO as GPIO

BUTTONPRESSED = FALSE
BUTTON1 = False
BUTTON2=False
BUTTON3=False
audiofiles= []
directories = []


#enter main menu
DIR = os.getcwd
DIR = DIR + "/main_menu"
os.chdir(DIR)

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

def outFrame(input):
    genericFrame = Frame(root, bg='#F5F5F5', bd=5)
    genericFrame.place(relx=0.2,rely=0, relwidth=0.6,relheight=0.16)
    genericLabel = Label(genericFrame, text=input, bg='black', fg='white', font=('Arial',30))
    genericLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
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
    BUTTON1 = True
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
    list = os.listdir(path=".")
    for l in list:
        if(l.endswith(".mp3")):
           # temp = f"{DIR}/{l}"
            audiofiles.append(l)
        else:
            directories.append(l)
        #print(temp)

    #check for change in state
    if BUTTONPRESSED:
        outFrame(directories[0])
        root.update()
        playAudio(audiofiles[0])
        BUTTONPRESSED = False

    #check for inputs
    #inputs are reset at the end of functions 
    if BUTTON1:
        BUTTONPRESSED = True
        BUTTON1 = False
    elif BUTTON2:
        BUTTONPRESSED = True
        BUTTON2 = False
    elif BUTTON3:
        BUTTONPRESSED = True
        BUTTON3 = False