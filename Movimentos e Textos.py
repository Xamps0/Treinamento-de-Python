import pygame
import random

#Load/Carregar
pygame.init()

Janela_Largura = 640
Janela_Altura = 480

Janela = pygame.display.set_mode((Janela_Largura,Janela_Altura))
pygame.display.set_caption("Movimentos e textos")
clock = pygame.time.Clock()
FPS = 60

Fonte_Grande = pygame.font.SysFont('Arial', 20,True,False)
Fonte_Pequena = pygame.font.SysFont('Arial', 12,False,True )

Branco = (255,255,255)

Titulo = Fonte_Grande.render("Movimentos e textos", True, Branco)

Titulo_rect = Titulo.get_rect(center=(Janela_Largura/2,40))


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
    texto_x = Fonte_Pequena.render("Vel x: " + str(velocidadeX), True, Branco)
    texto_y = Fonte_Pequena.render("Vel y: " + str(velocidadeY), True, Branco)
    r = random.randrange(0,255)
    g = random.randrange(0,255)
    b = random.randrange(0,255)
    x += velocidadeX
    y += velocidadeY

    #Draw/Apresentação
    Janela.fill((0,0,0))
    Janela.blit(Titulo,Titulo_rect )
    Janela.blit(texto_x,(15,410))
    Janela.blit(texto_y,(15,425))
    pygame.draw.rect(Janela, (r,g,b),(x,y,100,100))

    pygame.display.update()


#Fechamento do jogo

pygame.quit()