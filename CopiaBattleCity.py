import sys, pygame, random
from pygame.locals import * 
import player, bala

pygame.init()

#Constantes
width, height = 800, 600
black = (0,0,0)
chrono = 2

#Atributos
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Trabajo Final")
fuente = pygame.font.Font(None, 30)
clock = pygame.time.Clock()
mensaje_font = pygame.font.Font(None, 50)
score_font = pygame.font.Font(None, 60)

#Objetos
jugador_izq = player.raqueta(30, 240)
jugador_der = player.raqueta(770, 240)
pelota_obj = bala.pelota(width/2, height/2 )

while True:
    
#Relleno del BackGround
    screen.fill((0,0,0))
    
    #Impresion del Cronometro
    if (chrono == 0):
        if (pelota_obj.score_der < pelota_obj.score_izq):
            mensaje = mensaje_font.render("Gano el de la Izquierda",0, (250,250,250))
            screen.blit(mensaje, (width/2 - 100, height/2-50))
        elif (pelota_obj.score_der > pelota_obj.score_izq):
            mensaje = mensaje_font.render("Gano el de la Derecha",0, (250,250,250))
            screen.blit(mensaje, (width/2 - 100, height/2-50))
        else:
            final = random.randint(0, 1)
            if (final == 0):
                pelota_obj.score_der += 1
            elif (final == 1):
                pelota_obj.score_izq += 1
    else:
        chrono = 15 - int(pygame.time.get_ticks() / 1000)
        contador = fuente.render(str(chrono), 1, (250,250,250))
        screen.blit(contador, ((width/2) - 15, 0))
        score_msg_izq = score_font.render(str(pelota_obj.score_izq), 1, (250,250,250) )
        screen.blit(score_msg_izq, ((width/4) - 20, 0))
        score_msg_der = score_font.render(str(pelota_obj.score_der), 1, (250,250,250) )
        screen.blit(score_msg_der, ((width * 0.75) , 0))
        pelota_obj.animacion(width, height)

#Impresion de los Personajes
    jugador_izq.dibujar(screen)
    jugador_der.dibujar(screen)
    pelota_obj.dibujar(screen)

##Controlador de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        jugador_der.direccion(event)
        jugador_izq.direccion_izq(event)

#Para mantener en movimiento los objetos con las teclas pulsadas
    if (jugador_der.up == 1):
        jugador_der.rect = jugador_der.rect.move(0, -15)
    elif (jugador_der.up == 0):
        jugador_der.rect = jugador_der.rect.move(0, 15) 

    if (jugador_izq.up == 1):
        jugador_izq.rect = jugador_izq.rect.move(0, -15)
    elif (jugador_izq.up == 0):
        jugador_izq.rect = jugador_izq.rect.move(0, 15)
    

#Rebote de la pelota
    pelota_obj.rebote(jugador_izq.rect, jugador_der.rect)

#Carga la pantalla 
    pygame.display.flip()
    clock.tick(20) 