import pygame, random
from pygame.locals import*

class pelota(pygame.sprite.Sprite):
     
    def __init__(self, ancho, alto):
        pygame.sprite.Sprite.__init__(self)
        self.imagen = pygame.image.load("personajes/bala.png")
        self.rect = self.imagen.get_rect()
        self.rect.top = alto
        self.rect.left = ancho
        self.rect_inicio = self.rect
        self.velocidad = [random.choice((10, -10)) , random.choice((10, -10))]
        self.score_izq = 0
        self.score_der = 0

    def dibujar (self, ventana):
        ventana.blit(self.imagen, self.rect)

    def animacion(self, ancho, alto):
        self.rect = self.rect.move(self.velocidad)
        if self.rect.left < 0: 
            self.score_der += 1
            self.rect = self.rect_inicio
            self.velocidad = [random.choice((10, -10)) , random.choice((10, -10))]
        elif self.rect.right > ancho:
            self.score_izq += 1
            self.rect = self.rect_inicio
            self.velocidad = [random.choice((10, -10)) , random.choice((10, -10))]
        if self.rect.top < 0 or self.rect.bottom > alto:
            self.velocidad[1] = -self.velocidad[1]

    def rebote(self, raqueta_uno, raqueta_dos):
        if self.rect.colliderect(raqueta_uno) or self.rect.colliderect(raqueta_dos):
           self.velocidad[0] = -self.velocidad[0] 
    