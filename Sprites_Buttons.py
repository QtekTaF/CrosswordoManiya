import os
import sys
import pygame

pygame.font.init()
font = pygame.font.SysFont("Grobold", 20)
pygame.init()

class Button(pygame.sprite.Sprite):
    def __init__(self, color, color_hover, rect, callback, text='', outline=None):
        super().__init__()
        self.text = text

        tmp_rect = pygame.Rect(0, 0, *rect.size)

        self.org = self._create_image(color, outline, text, tmp_rect)
        self.hov = self._create_image(color_hover, outline, text, tmp_rect)

        self.image = self.org

        self.rect = rect
        self.callback = callback

    def _create_image(self, color, outline, text, rect):

        img = pygame.Surface(rect.size)

        if outline:

            img.fill(outline)
            img.fill(color, rect.inflate(-4, -4))
        else:
            img.fill(color)

        if text != '':
            text_surf = font.render(text, 1, pygame.Color('black'))

            text_rect = text_surf.get_rect(center=rect.center)
            img.blit(text_surf, text_rect)
        return img

    def update(self, events):

        pos = pygame.mouse.get_pos()
        hit = self.rect.collidepoint(pos)

        self.image = self.hov if hit else self.org
        for event in events:

             if event.type == pygame.MOUSEBUTTONDOWN and hit:
                 self.callback(self)
run = True


class ButtonI(pygame.sprite.Sprite):
    def __init__(self, color, color_hover, rect, callback, text='',outline=None,filename=''):
#    def __init__(self,pos,filename):
        #super().__init__()
        pygame.sprite.Sprite.__init__(self)

      #  self.image = pygame.image.load(filename).convert_alpha()
 #       self.rect = self.image.get_rect()
        self.text = text
        self.filename = 'iks04.png'
#        tmp_rect = pygame.Rect(0, 0, *rect.size)

      #  self.org = self._create_image(color, outline, text, tmp_rect)
       # self.hov = self._create_image(color_hover, outline, text, tmp_rect)

        #self.image = self.org
        self.image = pygame.image.load(os.path.join('images',filename))
        self.rect = rect
        self.callback = callback




    def update(self, events):

        pos = pygame.mouse.get_pos()
        hit = self.rect.collidepoint(pos)

       # self.image = pygame.image.load(os.path.join('images',filename))
        for event in events:

             if event.type == pygame.MOUSEBUTTONDOWN and hit:
                 self.callback(self)
run = True

class ButtonIL(pygame.sprite.Sprite):
    def __init__(self, color, color_hover, rect, callback, text='',outline=None,filename=''):
#    def __init__(self,pos,filename):
        #super().__init__()
        pygame.sprite.Sprite.__init__(self)

      #  self.image = pygame.image.load(filename).convert_alpha()
 #       self.rect = self.image.get_rect()
        self.text = text
        self.filename = 'scr00.png'
#        tmp_rect = pygame.Rect(0, 0, *rect.size)

      #  self.org = self._create_image(color, outline, text, tmp_rect)
       # self.hov = self._create_image(color_hover, outline, text, tmp_rect)

        #self.image = self.org
        self.image = pygame.image.load(os.path.join('images/Letters',filename))
        self.rect = rect
        self.callback = callback




    def update(self, events):

        pos = pygame.mouse.get_pos()
        hit = self.rect.collidepoint(pos)

       # self.image = pygame.image.load(os.path.join('images',filename))
        for event in events:

             if event.type == pygame.MOUSEBUTTONDOWN and hit:
                 self.callback(self)
run = True
