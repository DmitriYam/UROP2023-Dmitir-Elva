import os
import pygame

pygame.mixer.init()
def playAudio(voicefile):
    pygame.mixer.music.load(voicefile)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

DIR = os.getcwd()

DIR = DIR + "/main_menu"
os.chdir(DIR)

list = os.listdir(path=".")     

audiofiles= []
directories = []

for l in list:
    if(l.endswith(".mp3")):
        temp = f"{DIR}/{l}"
        audiofiles.append(l)
    else:
        directories.append(l)
    #print(temp)

for i in audiofiles:
    print(i)
    #playAudio(i)

os.chdir(directories[1])

currdir = os.getcwd()

print(DIR)

print(list)

print(audiofiles)

print(directories)

print(currdir)

list = os.listdir(path=".")

audiofiles.clear()
directories.clear()

for l in list:
    if(l.endswith(".mp3")):
        temp = f"{DIR}/{l}"
        audiofiles.append(l)
    else:
        directories.append(l)
    #print(temp)
print(audiofiles)
#playAudio(audiofiles[0])

print(directories)