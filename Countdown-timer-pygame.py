# https://stackoverflow.com/questions/30720665/countdown-timer-in-pygame
import pygame
pygame.init()
screen = pygame.display.set_mode((128, 128))
clock = pygame.time.Clock()

counter, text = 0, '0'.rjust(3)

pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

while True:
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT:
            counter += 1
            text = str(counter).rjust(3) if counter < 10 else 'boom!'
        if e.type == pygame.QUIT: break
    else:
        screen.fill((255, 255, 255))
        screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
        pygame.display.flip()
        clock.tick(600)
        myTime = pygame.time.get_ticks()
        print(myTime/1000)
        continue
    break