import pygame
import random
import math
import settings
import reflection


class Ball:
    def __init__(self, x, y, vx, vy, radius, r, g, b):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.r = r
        self.g = g
        self.b = b

    def update(self, dt, blocks):

        self.x += self.vx * dt
        self.y += self.vy * dt
        if (self.x >= settings.canvas_width - self.radius):
            self.x -= self.radius + self.x - settings.canvas_width
            self.vx = -self.vx
        if (self.x <= self.radius):
            self.x += self.radius - self.x
            self.vx = -self.vx
        if (self.y >= settings.canvas_height - self.radius):
            self.y -= self.radius + self.y - settings.canvas_height
            self.vy = -self.vy
        if (self.y <= self.radius):
            self.y += self.radius - self.y
            self.vy = -self.vy

        for j in range(settings.Number_of_blocks):
            if (abs(self.x - blocks[j].center_x) <= self.radius + blocks[j].lenx / 2) and \
                    (abs (self.y - blocks[j].center_y) <= self.radius + blocks[j].leny / 2) and \
                    ((math.sqrt ((self.x - blocks[j].center_x) ** 2 + (self.y - blocks[j].center_y) ** 2)) <= (self.radius + 1/2 * math.sqrt(blocks[j].lenx ** 2 + blocks[j].leny ** 2))):
                if (abs(self.x - blocks[j].center_x) <= self.radius + blocks[j].lenx / 2) and (blocks[j].center_y - (blocks[j].leny / 2) <= self.y) and \
                        (self.y <= blocks[j].center_y + (blocks[j].leny / 2)):
                    self.vx = -self.vx
                    if self.x < blocks[j].center_x:
                        self.x -= (self.radius + self.x) - (blocks[j].center_x - blocks[j].lenx / 2)
                    if self.x > blocks[j].center_x:
                        self.x += (blocks[j].center_x + blocks[j].lenx / 2) - (self.x - self.radius)
                if (self.y - blocks[j].center_y <= self.radius + blocks[j].leny / 2) and \
                        (blocks[j].center_x - (blocks[j].lenx / 2) <= self.x) and \
                        (self.x <= blocks[j].center_x + (blocks[j].lenx / 2)):
                    self.vy = -self.vy
                    if self.y < blocks[j].center_y:
                        self.y -= (self.radius + self.y) - (blocks[j].center_y - blocks[j].leny / 2)
                    if self.y > blocks[j].center_y:
                        self.y += (blocks[j].center_y + blocks[j].leny / 2) - (self.y - self.radius)
                if (abs(self.x - blocks[j].center_x) < self.radius + blocks[j].lenx / 2) and \
                    (abs (self.y - blocks[j].center_y) < self.radius + blocks[j].leny / 2) and \
                    ((math.sqrt((self.x - blocks[j].center_x + blocks[j].lenx / 2) ** 2 + (self.y - blocks[j].center_y + blocks[j].leny / 2) ** 2) < self.radius) or
                    (math.sqrt((self.x - blocks[j].center_x - blocks[j].lenx / 2) ** 2 + (self.y - blocks[j].center_y + blocks[j].leny / 2) ** 2) < self.radius) or
                    (math.sqrt((self.x - blocks[j].center_x + blocks[j].lenx / 2) ** 2 + (self.y - blocks[j].center_y - blocks[j].leny / 2) ** 2) < self.radius) or
                    (math.sqrt((self.x - blocks[j].center_x - blocks[j].lenx / 2) ** 2 + (self.y - blocks[j].center_y - blocks[j].leny / 2) ** 2) < self.radius)):
                    self.vx = reflection.reflect(self.x, self.y, blocks[j].center_x, blocks[j].center_y, self.vx, self.vy, 0, 0)[0]
                    self.vy = reflection.reflect(self.x, self.y, blocks[j].center_x, blocks[j].center_y, self.vx, self.vy, 0, 0)[1]
                    if (math.sqrt((self.x - blocks[j].center_x + blocks[j].lenx / 2) ** 2 + (self.y - blocks[j].center_y + blocks[j].leny / 2) ** 2) < self.radius):
                        self.x -= -(math.sqrt((self.x - blocks[j].center_x + blocks[j].lenx / 2) ** 2 +
                                (self.y - blocks[j].center_y + blocks[j].leny / 2) ** 2)) + self.radius
                        self.y -= -(math.sqrt((self.x - blocks[j].center_x + blocks[j].lenx / 2) ** 2 +
                                (self.y - blocks[j].center_y + blocks[j].leny / 2) ** 2)) + self.radius
                    if (math.sqrt((self.x - blocks[j].center_x - blocks[j].lenx / 2) ** 2 + (self.y - blocks[j].center_y - blocks[j].leny / 2) ** 2) < self.radius):
                        self.x += -(math.sqrt((self.x - blocks[j].center_x - blocks[j].lenx / 2) ** 2 +
                                (self.y - blocks[j].center_y - blocks[j].leny / 2) ** 2)) + self.radius
                        self.y += -(math.sqrt((self.x - blocks[j].center_x - blocks[j].lenx / 2) ** 2 +
                                (self.y - blocks[j].center_y - blocks[j].leny / 2) ** 2)) + self.radius
                    if (math.sqrt((self.x - blocks[j].center_x - blocks[j].lenx / 2) ** 2 + (self.y - blocks[j].center_y + blocks[j].leny / 2) ** 2) < self.radius):
                        self.x += -(math.sqrt((self.x - blocks[j].center_x - blocks[j].lenx / 2) ** 2 +
                                (self.y - blocks[j].center_y + blocks[j].leny / 2) ** 2)) + self.radius
                        self.y -= -(math.sqrt((self.x - blocks[j].center_x - blocks[j].lenx / 2) ** 2 +
                                (self.y - blocks[j].center_y + blocks[j].leny / 2) ** 2)) + self.radius
                    if (math.sqrt((self.x - blocks[j].center_x + blocks[j].lenx / 2) ** 2 + (self.y - blocks[j].center_y - blocks[j].leny / 2) ** 2) < self.radius):
                        self.x -= -(math.sqrt((self.x - blocks[j].center_x + blocks[j].lenx / 2) ** 2 +
                                (self.y - blocks[j].center_y - blocks[j].leny / 2) ** 2)) + self.radius
                        self.y += -(math.sqrt((self.x - blocks[j].center_x + blocks[j].lenx / 2) ** 2 +
                                (self.y - blocks[j].center_y - blocks[j].leny / 2) ** 2)) + self.radius



    def eat(self, ball):
        if ((ball.x - self.x) ** 2 + (self.y - ball.y) ** 2 <= (ball.radius + self.radius) ** 2) and (
                ball.radius < self.radius):
            if self.radius < settings.max_rad:
                self.radius = math.sqrt(self.radius **2 + ball.radius ** 2)
            ball.radius = 0

    def render(self, screen):
        pygame.draw.circle(screen, (self.r, self.g, self.b), (int(self.x), int(self.y)), int(self.radius))