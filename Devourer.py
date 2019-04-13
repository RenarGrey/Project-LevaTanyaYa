import sys
import pygame
import random
import math
import settings
import iballs
import playballs

pygame.init()

screen = pygame.display.set_mode((settings.width, settings.height))
pygame.display.set_caption('FK')
clock = pygame.time.Clock()

ballplayer = playballs.Ball(30, 30, 0, 0, 20, 0, 200, 120, 0, 0, settings.mass)
balls = []
for i in range(settings.Number_of_enemies):
    balls.append(iballs.Ball(random.randint(40, 960), random.randint(40, 960), random.randint(-70, 70),
                      random.randint(-70, 70), random.randint(5, 20), random.randint(100, 150),
                      random.randint(100, 150), random.randint(100, 150), 0, 0))

while True:
    dt = clock.tick(50) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_0):
            sys.exit()


    for i in range(len(balls)):
        balls[i].update(dt)
    ballplayer.update(dt, playballs.Ball.acceleration_x(ballplayer), playballs.Ball.acceleration_y(ballplayer))

    for i in range(len(balls)):
        ballplayer.eat(balls[i], settings.relation)

    screen.fill((235, 235, 235))

    for i in range(len(balls)):
        if balls[i].radius > 0:
            balls[i].render(screen)
    ballplayer.render(screen)

    pygame.display.flip()