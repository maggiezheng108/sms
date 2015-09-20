# TechCrunch Disrupt
# SMS Project

# import statements
import random
import pygame
import time
import inputbox
from time import sleep
from pygame import *
from Tkinter import *
pygame.init()

# set font and bg color
font = pygame.font.SysFont("Calibri", 120)
font2 = pygame.font.SysFont("Calibri", 48)
black = (0,0,0)
grey = (96, 96, 96)

# set font colors
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
purple = (102, 0, 204)
pink = (255, 105, 255)
orange = (255, 128, 0)
brown = (98, 50, 2)
white = (255, 255, 255)

# define screen
width, height = 600, 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("BLUE")
screen.fill(black)

# class defining each word as an object Word
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

# dictionary of possibly colors
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

# dictionary of possible words
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

# creates Word object and displays in iddle of the screen
def gameplay(word):
    word.randomColor()
    word.randomString()
    text = font.render(word.getString(), 1, word.getColor())
    screen.blit(text, (300 - (text.get_width() / 2), 300 - (text.get_height() / 2)))

def titlescreen():
    screen.fill(white)
    title = font.render("BLUE", 1, black)
    screen.blit(title, (300 - (title.get_width() / 2), 300 - (title.get_height() / 2)))
    subtitle = font2.render("Press Enter to begin", 1, black)
    screen.blit(subtitle, (300 - (subtitle.get_width() / 2), 300 - (subtitle.get_height() / 2) + 100))
    pygame.display.flip()

#runs the game
def main():
    leaving = False
    play = 0
    correct = 0
    titlescreen()
    inkey = inputbox.get_key();
    if inkey != K_RETURN:
        return
    screen.fill(black)
    pygame.display.flip()
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
        text = font.render('Score: '+ correct, 1, white)
        screen.blit(text, (300 - (text.get_width() / 2), 300 - (text.get_height() / 2)))
        text2 = font2.render("Press Enter to play again", 1, white)
        screen.blit(text2, (300 - (text2.get_width() / 2), 300 - (text2.get_height() / 2) + 100))
        text3 = font2.render("Press Space to exit", 1, white)
        screen.blit(text3, (300 - (text3.get_width() / 2), 300 - (text3.get_height() / 2) + 150))
        pygame.display.flip()
        inkey = inputbox.get_key();
        if inkey == K_RETURN:
            main()
        elif inkey == K_SPACE:
            pass


if __name__ == '__main__': main()
    