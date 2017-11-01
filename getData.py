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

try:
    import Image
except ImportError:
    from PIL import Image

resetImage = cv2.imread('endGameImage.jpg',0)

def findResetImage(image):
    global resetImage
    res = cv2.matchTemplate(image,resetImage,cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(res >= threshold)
    print(loc)
    if(len(loc[0]) > 0):
        return True
    return False

def getScore(image):
    subImage = image[0:20, 530:-1]
    pilImage =  Image.fromarray(subImage)
    screenText = pytesseract.image_to_string(pilImage, config="-c tessedit_char_whitelist=0123456789 -psm 6") #only want to match numbers
    return int(screenText)

def getImage():
    fScreenWidth =  1280
    screen = ImageGrab.grab(bbox=(fScreenWidth + 690,130,fScreenWidth + 1300, 270)) # X1,Y1,X2,Y2
    screen = np.asanyarray(screen)
    return screen

def getRandomAction():
    num = random.randrange(0,2)
    if num == 0:
        pyautogui.keyDown("space")
        return [0,1]
    else:
        pyautogui.keyUp("space")
        return [1,0]
    
def resetGame():
    pyautogui.keyUp("space")
    pyautogui.keyDown("space")
    time.sleep(0.01)
    pyautogui.keyUp("space")
    pyautogui.keyDown("space")
    time.sleep(0.01)

def main():
    time.sleep(1)
    #the open cv will spot the 
    #image at twice 
    # 
    loopAmount = 3 * 2
    minimumScore = 100
    trainingData = []
    for i in range(0,loopAmount):
        gameMemory = []
        score = 0
        while(True):
            print("going through")
            screen = getImage()
            action = getRandomAction()
            gameMemory.append([screen , action])
            if(findResetImage(screen) == True):
                score = getScore(screen)
                print("breaking")
                break
        if(score > minimumScore):
            for data in gameMemory:
                trainingData.append(data[0],data[1])
        resetGame()
    
    pyautogui.keyUp("space")
    pyautogui.keyUp("space")
    print("ended")

main()