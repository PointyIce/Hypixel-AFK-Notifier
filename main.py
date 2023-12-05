import time
import pygame
pygame.mixer.init()
sound = pygame.mixer.Sound("./beep.mp3")
def follow(thefile):
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line
try:
    logFile = open(r"C:\Users\Jesse\.lunarclient\offline\multiver\logs\latest.log","r")
    loglines = follow(logFile)
    for line in loglines:
        if line[11:39] == "[Client thread/INFO]: [CHAT]":
            if line[40:]== "You will be afk-ed in 10 seconds!\n":
                print("line: "+line[40:]+"!!!!!")
                sound.play()
            else:
                print("line:"+line[40:])
except Exception as e:
    print(e)