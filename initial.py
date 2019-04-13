import sys
import pygame
import random
import math

pygame.init()

width = 1000
height = 1000

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
        
    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        if (self.x >= width - self.radius) or (self.x <= self.radius):
            self.vx = -self.vx
        if (self.y >= width - self.radius) or (self.y <= self.radius):
            self.vy = -self.vy

    def wall(self):
        if (self.x >= width - self.radius) or (self.x <= self.radius):
            self.radius = 20
        if (self.y >= width - self.radius) or (self.y <= self.radius):
            self.radius = 20

    def eat(self, ball1):
        if ((ball1.x-self.x)**2+(self.y-ball1.y)**2 <= (ball1.radius+self.radius)**2) and (ball1.radius < self.radius):
            self.radius += math.sqrt(ball1.radius)
            ball1.radius = 0


    def render(self, screen):
        pygame.draw.circle(screen, (self.r, self.g, self.b), (int(self.x), int(self.y)), int(self.radius))

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('FK')
clock = pygame.time.Clock()

ballplayer = Ball(30, 30, 0, 0, 20, 0, 200, 120)
balls = []
for i in range(70):
    balls.append(Ball(random.randint(40, 960), random.randint(40, 960), random.randint(-70, 70),
                      random.randint(-70, 70), random.randint(5, 20), random.randint(100, 150), random.randint(100, 150), random.randint(100, 150)))

while True:
    dt = clock.tick(50) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_0):
            sys.exit()
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            ballplayer.vx = -60
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            ballplayer.vx = 60
        if pygame.key.get_pressed()[pygame.K_UP]:
            ballplayer.vy = -60
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            ballplayer.vy = 60

    for i in range(len(balls)):
        balls[i].update(dt)
    ballplayer.update(dt)
    ballplayer.wall()

    for i in range(len(balls)):
        ballplayer.eat(balls[i])

    screen.fill((235, 235, 235))

    for i in range(len(balls)):
        if balls[i].radius > 0:
            balls[i].render(screen)
    ballplayer.render(screen)

    pygame.display.flip()
