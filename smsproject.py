#TechCrunch Disrupt
#SMS Project

#import statements
import random
import pygame
import time
import inputbox
from time import sleep
from pygame import *
from Tkinter import *
pygame.init()

font = pygame.font.SysFont("Calibri", 120)
black = (0,0,0)

blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
purple = (102, 0, 204)
pink = (255,105,255)
orange = (255,128,0)
brown = (98,50,2)
white = (255,255,255)
grey = (96,96,96)

width,height = 600, 600
screen = pygame.display.set_mode((width,height))
screen.fill(black)

class Word:

    def __init__(self):
        self.name = "name"
        self.color = "color"
        self.num = "num"

    def randomColor(self):
        self.num = random.randint(0, 8)
        self.color = colors[self.num]

    def randomString(self):
        key = random.randint(0, 8)
        self.name = words[key]

    def getColor(self):
        return self.color

    def getString(self):
        return self.name

    def getKey(self):
        return self.num

colors = {
    0: blue,
    1: red,
    2: green,
    3: yellow,
    4: purple,
    5: pink,
    6: orange,
    7: brown,
    8: white,
}

words = {
    0: "BLUE",
    1: "RED",
    2: "GREEN",
    3: "YELLOW",
    4: "PURPLE",
    5: "PINK",
    6: "ORANGE",
    7: "BROWN",
    8: "WHITE",
}

def gameplay(word):
    word.randomColor()
    word.randomString()
    text = font.render(word.getString(), 1, word.getColor())
    screen.blit(text, (300 - (text.get_width() / 2), 300 - (text.get_height() / 2)))



def main():

    play = 0
    correct = 0
    while play < 21:
        clock = pygame.time.Clock()
        clock.tick()
        word = Word()
        gameplay(word)
        answer = inputbox.ask(screen, "")

        clock.tick()
        time = (2000-clock.get_time())
        
        if clock.get_time() >= 2000 or answer.upper() != words[word.getKey()]:
                screen.fill(grey)
                pygame.display.flip()
                play += 1
                continue
            # if answer.upper() != words[word.getKey()]:
            #     screen.fill(grey)
            #     pygame.display.flip()
            #     play += 1
            #     continue
            # else:
            #     screen.fill(grey)
            #     pygame.display.flip()
            #     play += 1
            #     continue
        else:
            pass
        time = str(2000-clock.get_time())
        text = font.render(time, 1, (255,255,255))
        screen.blit(text, (50, 50))
        screen.fill(black)
        pygame.display.flip()
        play += 1
        if answer.upper() == words[word.getKey()]:
                correct += 1
    else:
        print(correct)
        correct = str(correct)
        text = font.render('Score: '+ correct, 1, (255,255,255))
        screen.blit(text, (300 - (text.get_width() / 2), 300 - (text.get_height() / 2)))
        pygame.display.flip()
        sleep(5)

if __name__ == '__main__': main()
    