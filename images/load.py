import sys
import os
import pygame

pygame.init()

WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
COLOR_BACKGROUND = (128, 0, 128)

screen.fill(pygame.Color('white'))

if pygame.image.get_extended():
    print ('My pygame the best')
else:
    raise (SystemExit, 'Sorry, extended image module required')

windows_width = 220
windows_height= 220

image00 = pygame.image.load(os.path.join('images','iks00.png'))
image01 = pygame.image.load(os.path.join('images','iks01.png'))
image02 = pygame.image.load(os.path.join('images','iks02.png'))
image03 = pygame.image.load(os.path.join('images','iks03.png'))
image04 = pygame.image.load(os.path.join('images','iks04.png'))
image05 = pygame.image.load(os.path.join('images','iks05.png'))
image06 = pygame.image.load(os.path.join('images','iks06.png'))
image07 = pygame.image.load(os.path.join('images','iks07.png'))
image08 = pygame.image.load(os.path.join('images','iks08.png'))
image09 = pygame.image.load(os.path.join('images','iks09.png'))


newSurf = pygame.Surface((windows_width, windows_height))
newSurf.fill(pygame.Color('blue'))

newSurf.blit(image00, (20,20))
newSurf.blit(image01, (42,40))
newSurf.blit(image02, (64,60))
newSurf.blit(image03, (86,80))
newSurf.blit(image04, (108,100))
newSurf.blit(image05, (130,120))
newSurf.blit(image06, (152,140))
newSurf.blit(image07, (174,160))
newSurf.blit(image08, (196,180))
newSurf.blit(image09, (218,200))

      # = worked =
#pygame.image.save(newSurf,os.path.join('images','save_image_1.BMP'))
#print("save image_1")

screen.blit(image00, (20,20))
screen.blit(image01, (42,20))
screen.blit(image02, (64,20))
screen.blit(image03, (86,20))
screen.blit(image04, (108,20))
screen.blit(image05, (130,20))
screen.blit(image06, (152,20))
screen.blit(image07, (174,20))
screen.blit(image08, (196,20))
screen.blit(image09, (218,20))

screen.blit(newSurf, (200,200))

pygame.display.update()

x = input("число: ")
