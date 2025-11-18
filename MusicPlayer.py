import pygame
import requests
import json

def loadMusic(fileName):
    try:
        pygame.mixer.music.load(fileName)
        print("File loaded successfully")
    except IOError:
        print("File was not found")

def playMusic(fileName):
    pygame.mixer.music.play()

def stopMusic(fileName):
    pygame.mixer.music.stop()

def setVolume(volume):
    pygame.mixer.music.set_volume(volume)

def pauseMusic():
    pygame.mixer.music.pause()
def resumeMusic():
    pygame.mixer.music.unpause()



pygame.mixer.init()
print("Welcome to my custom music file player")
fileName=input("Enter the name of the file you wish to play: ")
loadMusic(fileName)

while True:
    print("What option would you like to do?")
    print("1:Start playing music")
    print("2:Pause")
    print("3:Resume")
    print("4:Stop")
    print("5:Change Song")
    print("6:Change Volume")
    choice=int(input("Enter your choice: "))
    if(choice==1):
        playMusic(fileName)
        continue
    elif(choice==4):
        stopMusic(fileName)
        continue
    elif(choice==2):
        pauseMusic()
        continue
    elif(choice==3):
        resumeMusic()
    elif(choice==5):
        volume=float(input("Enter your volume of choice from 0.0-1.0: "))
        if(volume>1.0):
            print("Volume must be between 0.0 and 1.0")
        elif(volume<0.0):
            print("Volume must be between 0.0 and 1.0")
        setVolume(volume)
        continue
    elif(choice==4):
        filename=input("Enter the name of the file you wish to play: ")
        loadMusic(fileName)
        continue
