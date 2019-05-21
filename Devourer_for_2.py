import sys
import pygame
import random
import settings
import iballs
import iblocks
import playballs

pygame.init()

screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
pygame.display.set_caption('FIELD')
clock = pygame.time.Clock()

blocks = []
for j in range(settings.Number_of_blocks):
    blocks.append(iblocks.Block(random.randint(0, settings.canvas_width), random.randint(0, settings.canvas_height),
                    random.randint(10, 40), random.randint(100, 150), random.randint(100, 150), random.randint(0, 50), random.randint(0, 50)))

ballplayer = playballs.Ball(settings.screen_width / 3, settings.screen_height / 3, 0, 0, settings.size, 100, 200, 20, 0, 0, settings.mass, pygame.K_RIGHT, pygame.K_LEFT, pygame.K_DOWN, pygame.K_UP)
ballplayer2 = playballs.Ball((settings.screen_width - settings.screen_width / 3), (settings.screen_height - settings.screen_height / 3), 0, 0, settings.size, 0, 200, 120, 0, 0, settings.mass, pygame.K_d, pygame.K_a, pygame.K_s, pygame.K_w)
balls = []
for i in range(settings.Number_of_enemies):
    balls.append(iballs.Ball(random.randint(0, settings.canvas_width), random.randint(0, settings.canvas_height), random.randint(-70, 70),
                      random.randint(-70, 70), random.randint(5, 20), random.randint(100, 150),
                      random.randint(100, 150), random.randint(100, 150)))

while True:
    dt = clock.tick(50) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_0):
            sys.exit()


    for i in range(len(balls)):
        balls[i].update(dt, blocks)
    ballplayer.update(dt, playballs.Ball.acceleration_x(ballplayer), playballs.Ball.acceleration_y(ballplayer), blocks)
    ballplayer2.update(dt, playballs.Ball.acceleration_x(ballplayer2), playballs.Ball.acceleration_y(ballplayer2), blocks)

    for i in range(len(balls)):
        ballplayer.eat(balls[i], settings.relation)
        ballplayer2.eat(balls[i], settings.relation)

    screen.fill((235, 235, 235))

    for i in range(len(balls)):
        if balls[i].radius > 0:
            balls[i].render(screen)
    ballplayer.render(screen)
    ballplayer2.render(screen)

    for i in range(len(blocks)):
        blocks[i].render(screen)

    pygame.display.flip()
