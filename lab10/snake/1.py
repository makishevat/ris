import pygame
import time
import random
import psycopg2

pygame.init()

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
blue = (50, 153, 213)
yellow = (255, 255, 102)

# Размеры дисплея
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Snake Tomiris")

# Настройки змейки
snake_block = 20
snake_speed = 3

clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Загрузка картинок еды
apple_img = pygame.image.load("food1.png")
grape_img = pygame.image.load("food2.png")
mango_img = pygame.image.load("food3.png")
apple_img = pygame.transform.scale(apple_img, (snake_block, snake_block))
grape_img = pygame.transform.scale(grape_img, (snake_block, snake_block))
mango_img = pygame.transform.scale(mango_img, (snake_block, snake_block))
food_images = [apple_img, grape_img, mango_img]

food_weights = {apple_img: 1, grape_img: 2, mango_img: 3}

# Инициализация змейки
x1 = dis_width / 2
y1 = dis_height / 2
x1_change = 0
y1_change = 0
snake_list = []
length_of_snake = 1

# Инициализация еды
foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
food_img = random.choice(food_images)
food_weight = food_weights[food_img]
food_spawn_time = time.time()
food_lifetime = 10

score = 0
game_over = False
game_close = False
level = 1
paused = False

#Подключение к базе
def connect():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="Malika123)"
    )

def create_tables():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("CREATE TABLE IF NOT EXISTS usersdata(username VARCHAR(100) PRIMARY KEY, level INTEGER DEFAULT 1, last_score INTEGER DEFAULT 0)")
           

def get_or_create_user(username):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT level,last_score FROM usersdata WHERE username=%s", (username,))
            user = cur.fetchone()
            if user: 
                return user[0],user[1] 
            cur.execute("INSERT INTO usersdata(username) VALUES(%s) RETURNING level, last_score", (username,))
            new_user = cur.fetchone()
            conn.commit()
            return new_user[0], new_user[1]


def save_score(username, level, last_score):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE usersdata SET level=%s, last_score=%s WHERE username=%s", (level,last_score, username))
            conn.commit()

#Отображение счета
def show_info(score):
    s = score_font.render("Score: " + str(score), True, yellow)
    dis.blit(s, [10, 10])

#Рисуем змейку
def snake_draw(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

#Сообщение на экран
def message(m, color):
    mesg = font_style.render(m, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

#Загрузка уровня
def load_level(level):
    walls = []
    base_speed = 5

    if level == 1:
        return base_speed, walls

    #Количество стенок зависит от уровня
    wall_count = level * 5  

    #Генерация случайных координат стенок
    for i in range(wall_count):
        x = random.randrange(0, dis_width // snake_block) * snake_block
        y = random.randrange(0, dis_height // snake_block) * snake_block
        walls.append((x, y))

    speed = base_speed + level - 2
    return speed, walls

create_tables()
username = input("Введите имя: ")
level,last_score=get_or_create_user(username)
if last_score>0:
    print("Ваш прошлый уровень:", level)
    print("Ваш прошлый счёт:", last_score)
else:
    print("Вы новый игрок!")
    level = 1

snake_speed, walls = load_level(level)

#Игровой цикл
while not game_over:
    #Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0
            elif event.key == pygame.K_p:
                paused = not paused

    #Пауза
    while paused:
        dis.fill(blue)
        message("Paused. Press P to continue", yellow)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                paused = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                paused = False

    #Проверка столкновения с границами
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_close = True

    x1 += x1_change
    y1 += y1_change
    dis.fill(white)

    #Проверка столкновения с препятствиями
    snake_rect = pygame.Rect(x1, y1, snake_block, snake_block)
    for w in walls:
        wall_rect = pygame.Rect(w[0], w[1], snake_block, snake_block)
        pygame.draw.rect(dis,(0,128,0) , wall_rect)
        if snake_rect.colliderect(wall_rect):
            game_close = True

    #Обновление еды
    if time.time() - food_spawn_time > food_lifetime:
        foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
        foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
        food_img = random.choice(food_images)
        food_weight = food_weights[food_img]
        food_spawn_time = time.time()

    dis.blit(food_img, (foodx, foody))

    #Обновление змейки
    snake_head = [x1, y1]
    snake_list.append(snake_head)
    if len(snake_list) > length_of_snake:
        del snake_list[0]

    #Проверка самопересечения
    for block in snake_list[:-1]:
        if block == snake_head:
            game_close = True

    snake_draw(snake_block, snake_list)
    show_info(score)
    pygame.display.update()

    # Столкновение с едой
    if x1 == foodx and y1 == foody:
        length_of_snake += food_weight
        score += food_weight
        save_score(username, level, score)

        if score >= level * 5:
            level += 1
            snake_speed, walls = load_level(level)
            snake_speed += level-2
            print("LEVEL UP!", level)

        foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
        foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
        food_img = random.choice(food_images)
        food_weight = food_weights[food_img]
        food_spawn_time = time.time()

    while game_close:
        dis.fill(blue)
        message("Game Over! Press ESC to quit or R to restart", red)
        show_info(score)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                game_close = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
                    game_close = False
                if event.key == pygame.K_r:
                    x1 = dis_width / 2
                    y1 = dis_height / 2
                    x1_change = 0
                    y1_change = 0
                    snake_list = []
                    length_of_snake = 1
                    score = 0
                    level = 1
                    snake_speed, walls = load_level(level)
                    foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
                    foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
                    food_img = random.choice(food_images)
                    food_weight = food_weights[food_img]
                    food_spawn_time = time.time()
                    game_close = False

    clock.tick(snake_speed)

pygame.quit()
quit() 
