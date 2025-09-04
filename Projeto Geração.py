import pygame
import random

#Load/Carregar
pygame.init()
Janela = pygame.display.set_mode((640,480))
pygame.display.set_caption("Projeto Geração")
clock = pygame.time.Clock()
FPS = 60


posicoesX = [0] * 5
posicoesY = [0] * 5

for p in range(5):
    posicoesX[p] = random.randrange(100,490)
    posicoesY[p] = random.randrange(100,330)

velocidadeX = [0] * 5
velocidadeY = [0] * 5

for v in range(5):
    velocidadeX[v] = random.randrange(-6,6)
    velocidadeY[v] = random.randrange(-6, 6)

cores = [(0,0,0)] * 5

for c in range(5):
    r = random.randrange(0,255)
    g = random.randrange(0,255)
    b = random.randrange(0,255)
    cores[c] = (r, g, b)


#Inicio do Ciclo
run = True
while run:
    #Update/atualização
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    #Draw/Apresentação
    Janela.fill((0,0,0))
    for i in range(5):
        pygame.draw.rect(Janela,(cores[i]),(posicoesX[i],posicoesY[i], 50,50 ))

    pygame.display.update()


#Fechamento do jogo

pygame.quit()