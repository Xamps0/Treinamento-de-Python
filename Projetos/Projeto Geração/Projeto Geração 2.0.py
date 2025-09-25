import pygame
import random

#Load/Carregar
pygame.init()

Janela_Largura = 640
Janela_Altura = 480

Janela = pygame.display.set_mode((Janela_Largura,Janela_Altura))
pygame.display.set_caption("Projeto Geração 2.0")
clock = pygame.time.Clock()
FPS = 60

qnt = 5

velocidadeX = [0] * qnt
velocidadeY = [0] * qnt

posicoesX = [0] * qnt
posicoesY = [0] * qnt

cores = [(0,0,0)] * qnt

for i in range(qnt):
    #velocidade
    velocidadeX[i] = random.randrange(-6,6)
    velocidadeY[i] = random.randrange(-6, 6)

    #posicao
    posicoesX[i] = random.randrange(100, Janela_Largura - 150)
    posicoesY[i] = random.randrange(100, Janela_Altura - 150)

    #cor
    r = random.randrange(0,255)
    g = random.randrange(0,255)
    b = random.randrange(0,255)
    cores[i] = (r, g, b)

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
                    r = random.randrange(0, 255)
                    g = random.randrange(0, 255)
                    b = random.randrange(0, 255)
                    cores[c] = (r, g, b)

            elif event.key == pygame.K_v:
                for v in range(qnt):
                    velocidadeX[v] = random.randrange(-6, 6)
                    velocidadeY[v] = random.randrange(-6, 6)

            elif event.key == pygame.K_p:
                for p in range(qnt):
                    posicoesX[p] = random.randrange(100, 490)
                    posicoesY[p] = random.randrange(100, 330)

    for i in range(qnt):
        if(posicoesX[i] + 50 > Janela_Largura):
            velocidadeX[i] *= -1
        if (posicoesY[i] + 50 > Janela_Altura):
            velocidadeY[i] *= -1
        if (posicoesX[i] < 0):
            velocidadeX[i] *= -1
        if (posicoesY[i] < 0):
            velocidadeY[i] *= -1


        posicoesX[i] += velocidadeX[i]
        posicoesY[i] += velocidadeY[i]


    #Draw/Apresentação
    Janela.fill((0,0,0))
    for i in range(qnt):
        pygame.draw.rect(Janela, (cores[i]), (posicoesX[i], posicoesY[i], 50, 50 ))

    pygame.display.update()


#Fechamento do jogo

pygame.quit()