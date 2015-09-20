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
        key = random.randint(0, 4)
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
    0: "BLUE",
    1: "RED",
    2: "GREEN",
    3: "YELLOW",
    4: "PURPLE",
}

def gameplay(word):
    text = font.render(word.random_string(), 1, word.random_color())
    screen.blit(text, (300 - (text.get_width() / 2), 300 - (text.get_height() / 2)))


def main():

    play = 0
    while play < 20:

        word = Word()
        gameplay(word)
        answer = inputbox.ask(screen, "")
        screen.fill(black)
        pygame.display.flip()
        play += 1



if __name__ == '__main__': main()
    