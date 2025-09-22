import pygame, random

#Load/Carregar
pygame.init()
Janela = pygame.display.set_mode((640,480))
pygame.display.set_caption("Acerte o alvo!")
clock = pygame.time.Clock()
FPS = 60

Fonte_Pequena = pygame.font.SysFont('Arial', 12,True ,False )
pygame.mouse.set_visible(False)

alvo_contador = 0
alvo_pos_x = random.randrange(50, 560)
alvo_pos_y = random.randrange(50, 400)
alvo_tamanho = 30
pontos = 0

cor_preto = (0, 0, 0)
cor_azul = (0, 0, 230)
alvo_cor = cor_azul

rect_alvo = pygame.Rect(alvo_pos_x, alvo_pos_y, alvo_tamanho, alvo_tamanho)

#Inicio do Ciclo
run = True
while run:
    #Update/atualização
    clock.tick(FPS)

    mx, my = pygame.mouse.get_pos()
    rect_mira = pygame.Rect(mx, my, 2, 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if rect_mira.colliderect(rect_alvo):
                    alvo_cor = cor_preto
                    pontos += 1

    texto_x = Fonte_Pequena.render("Pontos: " + str(pontos), True, (255, 255, 255))

    #Draw/Apresentação
    Janela.fill((0,0,0))
    Janela.blit(texto_x, (15, 20))
    pygame.draw.rect(Janela, alvo_cor, rect_alvo)
    pygame.draw.circle(Janela, (255,0,0), (mx, my), 10, 2)
    pygame.display.update()
    alvo_contador += 1
    if alvo_contador == 80:

        alvo_pos_x = random.randrange(50, 560)

        alvo_pos_y = random.randrange(50, 400)
        rect_alvo = pygame.Rect(alvo_pos_x, alvo_pos_y, alvo_tamanho, alvo_tamanho)
        alvo_contador = 0
        alvo_cor = cor_azul


#Fechamento do jogo

pygame.quit()