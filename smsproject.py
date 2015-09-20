#TechCrunch Disrupt
#SMS Project

#import statements
import random
import pygame
import time
from time import sleep
from pygame import *
from Tkinter import *
pygame.init()

font = pygame.font.SysFont("Arial", 72)
white = (255,255,255)
black = (0,0,0)

blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
purple = (102, 0, 204)

width,height = 600, 600
screen = pygame.display.set_mode((width,height))
screen.fill(black)

class Word:

    def __init__(self):
        self.name = "name"
        self.color = "color"

    def random_color(self):
        key = random.randint(0, 4)
        self.name = colors[key]
        return self.name

    def random_string(self):
        key = random.randint(5, 9)
        self.color = words[key]
        return self.color

colors = {
    0: blue,
    1: red,
    2: green,
    3: yellow,
    4: purple,
}

words = {
    5: "BLUE",
    6: "RED",
    7: "GREEN",
    8: "YELLOW",
    9: "PURPLE",
}

def gameplay(word):
    text = font.render(word.random_string(), 1, word.random_color())
    screen.blit(text, (175, 250))


def main():

    play = True
    while play:
        word = Word()
        gameplay(word)
        pygame.display.update()
        sleep(5)
        play = False


if __name__ == '__main__': main()
    