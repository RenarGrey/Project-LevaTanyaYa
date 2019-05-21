import sys
import pygame
import random
import math
import settings


class Block:
    def __init__(self, x, y, lex, ley, r, g, b):
        self.x = x
        self.y = y
        len = [lex, ley]
        lenx = random.choice(len)
        if lenx == lex:
            leny = ley
                else:
            leny = lex
        self.lenx = lenx
        self.leny = leny
        self.r = r
        self.g = g
        self.b = b
        self.center_x = x + lenx / 2
        self.center_y = y + leny / 2

    def render(self, screen):
        Rect = pygame.Rect(self.x, self.y, self.lenx, self.leny)
        pygame.draw.rect(screen, (self.r, self.g, self.b), (self.x, self.y, self.lenx, self.leny))
