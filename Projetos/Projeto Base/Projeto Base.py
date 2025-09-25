import pygame

#Load/Carregar
pygame.init()
Janela = pygame.display.set_mode((640,480))
pygame.display.set_caption("Projeto Base")
clock = pygame.time.Clock()
FPS = 60


#Inicio do Ciclo
run = True
while run:
    #Update/atualização
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    #Draw/Apresentação

    pygame.display.update()


#Fechamento do jogo

pygame.quit()