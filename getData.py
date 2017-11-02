import numpy as np
import pyscreenshot as ImageGrab
import cv2
import time
from getkey import getkey
import os
import pytesseract
import pyautogui
import random
import pickle
from helperFunction import findImage, getScore, getImage, getRandomAction, resetGame
try:
    import Image
except ImportError:
    from PIL import Image

resetImage = cv2.imread('endGameImage.jpg',0)



#problem
'''
Sleep seems to stop the broswer as well
as the script.  So i can't just
pause the screen untill something changes.
'''

def main():
    global resetImage
    time.sleep(1)
    #the open cv will spot the 
    #image at twice 
    # 
    loopAmount = 50000
    minimumScore = 80
    trainingData = []
    for i in range(0,loopAmount):
        gameMemory = []
        score = 0
        while(True):
            #time.sleep(0.005)                                            
            screen = getImage()
            action = getRandomAction()
            gameMemory.append([screen , action])
            if(findImage(resetImage, screen)["foundImage"] == True):
                score = getScore(screen)
                print("breaking")
                break
        print(i)
        print("score " + str(score))
        if(score > minimumScore):
            for data in gameMemory:
                trainingData.append([data[0],data[1]])
        #while reset icon is still on the screen
        #wait
        while(True):
            screen = getImage()
            if(findImage(resetImage, screen)["foundImage"] == False):
                print("no more reset icon")
                break
            resetGame()

    #make sure remove kedown on space par 
    pyautogui.keyUp("space")
    pyautogui.keyUp("space")
    print("ended")
    output = open('dataFirstAttempt.pickle', 'wb+')
    pickle.dump(trainingData,output)


main()