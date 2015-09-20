#TechCrunch Disrupt
#SMS Project

#import statements
import random
import pygame
from pygame import *
pygame.init()

#font = pygame.font.Font("Arial",16)
font = pygame.font.SysFont("Arial", 16)
font2 = pygame.font.SysFont("Serif", 20)
font3 = pygame.font.SysFont("Arial",14)
white = (255,255,255)
black = (0,0,0)

blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
purple = (102, 0, 204)

width,height = 600, 600
extraW = 400
screen = pygame.display.set_mode((width+extraW,height))
pygame.display.set_caption("SMS PROJECT")
screen.fill(white)

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

def main():
    text = Word()
    print(text.random_string())
    print(text.random_color())



if __name__ == '__main__': main()
    