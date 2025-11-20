import pygame
import time
import random

pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
blue = (50, 153, 213)
yellow = (255, 255, 102)

# Game window size
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Snake Tomiris")

# Game parameters
snake_block = 20        # size of one snake block 
snake_speed = 3         # initial snake speed

clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Load images for food
apple_img = pygame.image.load("food1.png")
grape_img = pygame.image.load("food2.png")
mango_img = pygame.image.load("food3.png")

# Resize fruit images to cell size
apple_img = pygame.transform.scale(apple_img, (snake_block, snake_block))
grape_img = pygame.transform.scale(grape_img, (snake_block, snake_block))
mango_img = pygame.transform.scale(mango_img, (snake_block, snake_block))

# List of possible fruit images
food_images = [apple_img, grape_img, mango_img]

# Initial snake coordinates (center)
x1 = dis_width/2
y1 = dis_height/2
x1_change = 0
y1_change = 0

# Snake body list and size
snake_list = []
length_of_snake = 1

# Spawn first food
foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block

food_img = random.choice(food_images)   # select random food sprite

# Determine initial weight based on fruit type
if food_img == apple_img:
    food_weight = 1
elif food_img == grape_img:
    food_weight = 2
elif food_img == mango_img:
    food_weight = 3

food_spawn_time = time.time() #when the food spawned
food_lifetime = 10            #food disappears after 10s

score = 0
game_over = False
game_close = False

#Function: display score
def show_info(score):
    score_text = score_font.render("Score: " + str(score), True, yellow)
    dis.blit(score_text, [10, 10])

#Function: draw the snake
def snake_draw(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

#Function: show game over message
def message(m, color):
    mesg = font_style.render(m, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

while not game_over:

    #Show game over screen
    while game_close:
        dis.fill(blue)
        message(" Game over ", red)
        show_info(score)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                game_close = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game_over = True
                game_close = False

    #Player controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            game_close = False

        if event.type == pygame.KEYDOWN:
            #Move left
            if event.key == pygame.K_LEFT and x1_change != snake_block:
                x1_change = -snake_block
                y1_change = 0

            #Move right
            elif event.key == pygame.K_RIGHT and x1_change != -snake_block:
                x1_change = snake_block
                y1_change = 0

            #Move up
            elif event.key == pygame.K_UP and y1_change != snake_block:
                y1_change = -snake_block
                x1_change = 0

            #Move down
            elif event.key == pygame.K_DOWN and y1_change != -snake_block:
                y1_change = snake_block
                x1_change = 0

    #Check collision with screen borders
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_close = True

    #Move snake head
    x1 += x1_change
    y1 += y1_change

    #Clear screen
    dis.fill(white)

    #If food lived too long, replace it
    if time.time() - food_spawn_time > food_lifetime:
        foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
        foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
        food_img = random.choice(food_images)

        #Set weight based on fruit
        if food_img == apple_img:
            food_weight = 1
        elif food_img == grape_img:
            food_weight = 2
        elif food_img == mango_img:
            food_weight = 3

        food_spawn_time = time.time()

    #Draw food sprite
    dis.blit(food_img, (foodx, foody))

    #Add new snake head to body
    snake_head = [x1, y1]
    snake_list.append(snake_head)

    #Remove tail if snake is too long
    if len(snake_list) > length_of_snake:
        del snake_list[0]

    #Check if snake eats itself
    for block in snake_list[:-1]:
        if block == snake_head:
            game_close = True

    #Draw snake 
    snake_draw(snake_block, snake_list)
    show_info(score)
    pygame.display.update()

    #Check food collision
    if x1 == foodx and y1 == foody:
        length_of_snake += food_weight  # grow snake based on fruit

        #Add score based on fruit type
        if food_img == apple_img:
            score += 1
        elif food_img == grape_img:
            score += 2
        elif food_img == mango_img:
            score += 3

        #Spawn new food
        foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
        foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
        food_img = random.choice(food_images)

        #Set weight based on fruit
        if food_img == apple_img:
            food_weight = 1
        elif food_img == grape_img:
            food_weight = 2
        elif food_img == mango_img:
            food_weight = 3

        food_spawn_time = time.time()
        snake_speed+=1
    #Limit FPS based on snake speed
    clock.tick(snake_speed)

pygame.quit()
quit()

