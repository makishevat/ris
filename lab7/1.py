import pygame
import datetime

pygame.init()
screen=pygame.display.set_mode((800,800))
pygame.display.set_caption("Mickey Clock")
clock_background=pygame.image.load("clock.png")
min_hand=pygame.image.load("min.png")
sec_hand=pygame.image.load("sec.png")

def rot_center(image, angle,x,y):
    rotated_image=pygame.transform.rotate(image,angle)
    new_rect=rotated_image.get_rect(center=image.get_rect(center=(x,y)).center)
    return rotated_image, new_rect

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    now=datetime.datetime.now()
    minut= int(now.strftime("%M"))
    sec= int(now.strftime("%S"))

    screen.fill((255,255,255))

    screen.blit(clock_background,(0,0))

    min_angle=-(360*minut/60)-55
    sec_angle=-(360*sec/60)+55


    clock=clock_background.get_rect()
    width=clock.width
    height=clock.height

    rotated_min, min_rect=rot_center(min_hand,min_angle,width//2,height//2)
    rotated_sec, sec_rect=rot_center(sec_hand,sec_angle,width//2,height//2)
    
    screen.blit(rotated_min,min_rect)
    screen.blit(rotated_sec, sec_rect)
    clock=pygame.time.Clock()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()