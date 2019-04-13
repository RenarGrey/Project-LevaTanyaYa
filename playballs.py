import sys
import pygame
import math
import settings


class Ball:
    def __init__(self, x, y, vx, vy, radius, r, g, b, ax, ay, m):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay
        self.radius = radius
        self.r = r
        self.g = g
        self.b = b
        self.m = m

    def acceleration_x(self):
        self.ax = 0
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.ax += settings.g
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.ax -= settings.g
        return self.ax

    def acceleration_y(self):
        self.ay = 0
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.ay += settings.g
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.ay -= settings.g
        return self.ay

    def update(self, dt, ax, ay):

        self.vx += (ax - self.vx * self.m) * dt
        self.vy += (ay - self.vy * self.m) * dt

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



    def eat(self, ball, relation):
        if ((ball.x - self.x) ** 2 + (self.y - ball.y) ** 2 <= (ball.radius + self.radius) ** 2) and (
                ball.radius < self.radius):
            if self.radius < settings.max_rad:
                self.radius = math.sqrt(self.radius **2 + ball.radius ** 2)
            ball.radius = 0

    def render(self, screen):
        pygame.draw.circle(screen, (self.r, self.g, self.b), (int(self.x), int(self.y)), int(self.radius))