from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import pygame
import RPi.GPIO as GPIO

BUTTONPRESSED = True
BUTTON1=False
BUTTON2=False
BUTTON3=False
BUTTON4=False
audiofiles= []
directories = []


#enter main menu
DIR = os.getcwd()
DIR = DIR + "/main_menu"
os.chdir(DIR)

#init PREV_STATE to null 
PREV_STATE="null"

root = Tk()
root.geometry("1000x700")

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
def isr4(channel):
    global BUTTON4
    BUTTON4 = True
    print("Button 4")
#GPIO
def initGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(17, GPIO.FALLING,callback=isr1, bouncetime=200)
    GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(26, GPIO.FALLING,callback=isr2, bouncetime=200)
    GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(22, GPIO.FALLING,callback=isr3, bouncetime=200)
    GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(19, GPIO.FALLING,callback=isr4, bouncetime=200)
    
initGPIO()
initAudio()
menuPointer = 0
mainmenu = False
while True:
    #check for change in state
    if BUTTONPRESSED:
        #add all directories and files to list 
        list = os.listdir(path=".")
        for l in list:
            if(l.endswith(".mp3")):
                audiofiles.append(l)
            else:
                directories.append(l)
        audiofiles.sort()
        directories.sort()
        #check if in main menu 
        if(len(directories) != 0):
            mainmenu = True
            outFrame(directories[menuPointer])
            directoryPointer = directories[menuPointer]
            maxmenulen = len(directories)
            #navigate into directory to get mp3 file for directory
            os.chdir(directoryPointer)
            list = os.listdir(path=".")
            for l in list:
                if(l.endswith("voice.mp3")):
                    toplay = l;
            root.update()
            playAudio(toplay)
            os.chdir("..")
        else:
            mainmenu = False
            for a in audiofiles:    
                if(a.endswith("voice.mp3")):
                    audiofiles.remove(a)
            outFrame(audiofiles[menuPointer])
            toplay = audiofiles[menuPointer] 
            maxmenulen = len(audiofiles)
            root.update()
            playAudio(toplay)
        BUTTONPRESSED = False
        directories.clear()
        audiofiles.clear() 
    #check for inputs
    #inputs are reset at the end of functions 
    if BUTTON1:
        BUTTONPRESSED = True
        print(maxmenulen)
        if(menuPointer == (maxmenulen-1)):
            menuPointer = 0
        else:
            menuPointer += 1
        BUTTON1 = False
    elif BUTTON2:
        BUTTONPRESSED = True
        if(menuPointer == 0):
            menuPointer = maxmenulen - 1
        else:
            menuPointer -= 1
        BUTTON2 = False
    elif BUTTON3:
        BUTTONPRESSED = True
        os.chdir(directoryPointer)
        menuPointer = 0
        BUTTON3 = False
    elif BUTTON4:
        BUTTONPRESSED = True
        print(directories)
        if(mainmenu == False):
            os.chdir("..")
        menuPointer = 0
        BUTTON4 = False
