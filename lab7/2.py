import pygame
from pygame import mixer

pygame.init()
mixer.init()
pygame.display.set_caption("Music player")
screen=pygame.display.set_mode((800,800))
clock=pygame.time.Clock()
FPS=50
done=False
n=0
musics=['blindinglights.mp3','allthestars.mp3','easyonme.mp3','goodnews.mp3','serebro.mp3','godsplan.mp3']

def start(n):
    mixer.music.load(musics[n])
    mixer.music.set_volume(0.2)
    mixer.music.play()
    print(f" Now playing: {musics[n]}")

start(n)
paused=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
            if(paused==False):
                mixer.music.pause()
                paused=True
            else:
                mixer.music.unpause()
                paused=False
        if event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT:
            if n==5:n=0
            else: n+=1
            start(n)
        if event.type==pygame.KEYDOWN and event.key==pygame.K_LEFT:
            if n==0: n=5
            else: n-=1
            start(n)
        
    clock.tick(FPS)
pygame.quit()