import pygame
import random

#Load/Carregar
pygame.init()

Janela = pygame.display.set_mode((640,480))
pygame.display.set_caption("Projeto Geração")
clock = pygame.time.Clock()
FPS = 60

qnt = 5

Janela_Largura = 640
Janela_Altura = 480

velocidadeX = [0] * qnt
velocidadeY = [0] * qnt

for v in range(qnt):
    velocidadeX[v] = random.randrange(-6,6)
    velocidadeY[v] = random.randrange(-6, 6)

posicoesX = [0] * qnt
posicoesY = [0] * qnt

for p in range(qnt):
    posicoesX[p] = random.randrange(100,490)
    posicoesY[p] = random.randrange(100,330)

cores = [(0,0,0)] * qnt

for c in range(qnt):
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

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            elif event.key == pygame.K_r:
                qnt += 1
                posicoesX.append(random.randrange(100, 490))
                posicoesY.append(random.randrange(100, 330))
                velocidadeX.append(random.randrange(-6, 6))
                velocidadeY.append(random.randrange(-6, 6))
                r = random.randrange(0, 255)
                g = random.randrange(0, 255)
                b = random.randrange(0, 255)
                cores.append((r, g, b))

            elif event.key == pygame.K_c:
                for c in range(qnt):
                    r = random.randrange(0,255)
                    g = random.randrange(0,255)
                    b = random.randrange(0,255)
                    cores[c] = (r, g, b)

            elif event.key == pygame.K_v:
                for v in range(qnt):
                    velocidadeX[v] = random.randrange(-6,6)
                    velocidadeY[v] = random.randrange(-6, 6)

            elif event.key == pygame.K_p:
                for p in range(qnt):
                    posicoesX[p] = random.randrange(100,490)
                    posicoesY[p] = random.randrange(100,330)

    for v in range(qnt):
        posicoesX[v] += velocidadeX[v]
        posicoesY[v] += velocidadeY[v]

    for i in range(qnt):
        if(posicoesX[i] + 50 > Janela_Largura) or (posicoesX[i] < 0):
            velocidadeX[i] *= -1
        if (posicoesY[i] + 50 > Janela_Altura) or (posicoesY[i] < 0):
            velocidadeY[i] *= -1


    #Draw/Apresentação
    Janela.fill((0,0,0))
    for i in range(qnt):
        pygame.draw.rect(Janela, (cores[i]), (posicoesX[i], posicoesY[i], 50, 50 ))

    pygame.display.update()


#Fechamento do jogo

pygame.quit()