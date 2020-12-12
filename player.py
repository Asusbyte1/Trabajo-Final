import pygame
from pygame.locals import*

class raqueta(pygame.sprite.Sprite):
     
    def __init__(self, ancho, alto):
        pygame.sprite.Sprite.__init__(self)
        self.imagen = pygame.image.load("personajes/player.png")
        self.rect = self.imagen.get_rect()
        self.rect.top = alto
        self.rect.left = ancho
        self.rect_inicio = self.rect
        self.up = 2
        
    def dibujar (self, ventana):
        ventana.blit(self.imagen, (self.rect))

    def direccion(self, event):
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                self.up = 1
            if event.key == pygame.K_DOWN:
                self.up = 0
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.up = 2

    def direccion_izq(self, event):
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_w:
                self.up = 1
            if event.key == pygame.K_s:
                self.up = 0
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_w or event.key == pygame.K_s:
                self.up = 2
        