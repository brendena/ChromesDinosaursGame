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

def findImage(imageToFind, image):
    res = cv2.matchTemplate(image,imageToFind,cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(res >= threshold)
    #print(loc)
    returnObject = {"foundImage": False,"loc": loc}
    if(len(loc[0]) > 0):
        returnObject["foundImage"] = True
    return returnObject

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

def jump():
    pyautogui.keyDown("space")
    pyautogui.keyUp("space")