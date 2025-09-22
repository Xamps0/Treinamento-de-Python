import pygame

#Load/Carregar
pygame.init()
Janela = pygame.display.set_mode((640,480))
pygame.display.set_caption("Projeto Base")
clock = pygame.time.Clock()
FPS = 60

jogador_pos_x = 320
jogador_pos_y = 360
jogador_vel_x = 2
jogador_vel_y = 2
jogador_mov_x = 0
jogador_mov_y = 0
jogador_cor = (219, 189, 39)
jogador_dur_pulo = 30
jogador_cont_pulo = 0


#Inicio do Ciclo
run = True
while run:
    #Update/atualização
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                jogador_mov_x = jogador_vel_x
            elif event.key == pygame.K_LEFT:
                jogador_mov_x = -jogador_vel_x
            elif event.key == pygame.K_UP and  jogador_mov_y == 0:
                jogador_mov_y = -jogador_vel_y
                jogador_cont_pulo = 0

        elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    jogador_mov_x = 0
    jogador_pos_x += jogador_mov_x
    jogador_pos_y += jogador_mov_y

    if jogador_mov_y != 0:
        jogador_cont_pulo += 1
        if jogador_cont_pulo == jogador_dur_pulo:
            jogador_mov_y *= -1
        elif jogador_cont_pulo == jogador_dur_pulo *2:
            jogador_mov_y = 0



    #Draw/Apresentação
    Janela.fill((0,0,0))
    pygame.draw.rect(Janela, (51, 52, 39), (0, 400, 640, 80))
    pygame.draw.rect(Janela, jogador_cor, (jogador_pos_x, jogador_pos_y, 20, 40))
    pygame.display.update()


#Fechamento do jogo

pygame.quit()