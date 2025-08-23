import pygame

pygame.init()

janela = pygame.display.set_mode((500,500))
pygame.display.set_caption("Formas")

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
ciano = (0,255,255)
pink = (255,0,255)
yellow = (255,255,0)
white = (255,255,255)


larg = 100
alt = 200

x = 100
y = 300

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.rect(janela,ciano,(x-80,y-250,larg-50,alt-150))
    pygame.draw.rect(janela,red,(x,y-250,larg,alt-100))
    pygame.draw.rect(janela,pink,(x+50,y-100,larg,alt))
    pygame.draw.circle(janela,green,(x+300,y-200),60)
    pygame.draw.polygon(janela,yellow,((x+220,y),(x+320,y),(x+270,y-100)))
    pygame.draw.polygon(janela, blue, ((x + 220, y+100), (x + 270, y+180),(x + 320, y+100), (x + 270, y+20)))
    pygame.display.update()




pygame.quit()