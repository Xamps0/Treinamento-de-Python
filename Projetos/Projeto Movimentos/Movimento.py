import pygame
import random

#Load/Carregar
pygame.init()
Janela = pygame.display.set_mode((640,480))
pygame.display.set_caption("Movimento")
clock = pygame.time.Clock()
FPS = 60

velocidadeX = random.uniform(-1.5,1.5)
velocidadeY = random.uniform(-1.5,1.5)

x = 270
y = 190

#Inicio do Ciclo
run = True
while run:
    #Update/atualização
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    velocidadeX = random.uniform(-1.5, 1.5)
    velocidadeY = random.uniform(-1.5, 1.5)
    r = random.randrange(0,255)
    g = random.randrange(0,255)
    b = random.randrange(0,255)
    x += velocidadeX
    y += velocidadeY

    #Draw/Apresentação
    Janela.fill((0,0,0))

    pygame.draw.rect(Janela, (r,g,b),(x,y,100,100))

    pygame.display.update()


#Fechamento do jogo

pygame.quit()