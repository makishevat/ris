import pygame

pygame.init()
screen=pygame.display.set_mode((800,800))
clock=pygame.time.Clock()
FPS=50
done=False
posX=400
posY=400

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN and event.key==pygame.K_UP:
            if posY>=30:
                posY-=25
        if event.type==pygame.KEYDOWN and event.key==pygame.K_DOWN:
            if posY<760:
                posY+=25
        if event.type==pygame.KEYDOWN and event.key==pygame.K_LEFT:
            if posX>=30:
                posX-=25
        if event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT:
            if posX<760:
                posX+=25
    screen.fill((255,255,255))
    pygame.draw.circle(screen,(255,0,0),(posX,posY),25)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()