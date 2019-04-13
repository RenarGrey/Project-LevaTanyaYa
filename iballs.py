import sys
import pygame
import random
import math
import settings


class Ball:
    def __init__(self, x, y, vx, vy, radius, r, g, b, ax, ay):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.r = r
        self.g = g
        self.b = b

    def update(self, dt):

        self.x += self.vx * dt
        self.y += self.vy * dt
        if (self.x >= settings.width - self.radius):
            self.x -= self.radius + self.x - settings.width
            self.vx = -self.vx
        if (self.x <= self.radius):
            self.x += self.radius - self.x
            self.vx = -self.vx
        if (self.y >= settings.height - self.radius):
            self.y -= self.radius + self.y - settings.height
            self.vy = -self.vy
        if (self.y <= self.radius):
            self.y += self.radius - self.y
            self.vy = -self.vy

    def eat(self, ball1):
        if ((ball1.x - self.x) ** 2 + (self.y - ball1.y) ** 2 <= (ball1.radius + self.radius) ** 2) and (
                ball1.radius < self.radius):
            self.radius += math.sqrt(ball1.radius)
            ball1.radius = 0

    def render(self, screen):
        pygame.draw.circle(screen, (self.r, self.g, self.b), (int(self.x), int(self.y)), int(self.radius))