import pygame
import time
import random

pygame.init()

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
yellow = (255, 255, 102)

# Размер экрана
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Змейка Томирис")

# Параметры
snake_block = 20
snake_speed = 3

clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Загрузка изображения яблока
apple_img = pygame.image.load("apple.png")
apple_img = pygame.transform.scale(apple_img, (15, 15))

# Функции
def your_score(score):
    value = score_font.render("Your score: " +str(score),True,yellow)
    dis.blit(value,[10, 10])

def snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block,snake_block])

def message(m, color):
    mesg = font_style.render(m, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])


# Начальные значения
x1=dis_width/2
y1=dis_height/2
x1_change=0
y1_change=0

snake_list=[]
length_of_snake=1

foodx=round(random.randrange(0,dis_width-snake_block)/snake_block)*snake_block
foody=round(random.randrange(0,dis_height-snake_block)/snake_block)*snake_block

game_over = False
game_close = False

# Главный цикл
while not game_over:
    while game_close:
        dis.fill(blue)
        message(" Game over ", red)
        your_score(length_of_snake - 1)
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                game_close = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
                    game_close = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over=True
            game_close=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x1_change!= snake_block:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT and x1_change!= -snake_block:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP and y1_change!= snake_block:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN and y1_change!= -snake_block:
                y1_change = snake_block
                x1_change = 0

    if x1>= dis_width or x1<0 or y1>= dis_height or y1< 0:
        game_close = True

    x1+= x1_change
    y1+= y1_change
    dis.fill(white)

    dis.blit(apple_img, (foodx, foody))
    snake_head = [x1, y1]
    snake_list.append(snake_head)

    if len(snake_list) > length_of_snake:
        del snake_list[0]

    for block in snake_list[:-1]:
        if block == snake_head:
            game_close = True

    snake(snake_block, snake_list)
    your_score(length_of_snake-1)

    pygame.display.update()

    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0,dis_width-snake_block)/snake_block)*snake_block
        foody = round(random.randrange(0,dis_height-snake_block)/snake_block)*snake_block
        length_of_snake+=1
        snake_speed+=1

    clock.tick(snake_speed)

pygame.quit()
quit()
