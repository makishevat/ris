import pygame
import time
import random
import psycopg2
import json
from datetime import datetime

pygame.init()

# ------------------ Настройки БД (измени под свою) ------------------
DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "Malika123)"
# -------------------------------------------------------------------

# Подключение к БД
conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
cur = conn.cursor()

# Создаем таблицы, если их нет
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    level INT DEFAULT 1,
    record INT DEFAULT 0
);
""")
cur.execute("""
CREATE TABLE IF NOT EXISTS user_scores (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    score INT,
    level INT,
    save_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")
cur.execute("""
CREATE TABLE IF NOT EXISTS user_states (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    state_json TEXT,
    saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")
conn.commit()

# ------------------ Pygame / окно / шрифты ------------------
# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
blue = (50, 153, 213)
yellow = (255, 215, 0)
gray = (200, 200, 200)

# Размер окна
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Snake Tomiris")

# Параметры змейки
snake_block = 20  # cell size
base_speed = 3    # базовая скорость (level 1)

clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# ------------------ Загружаем ресурсы ------------------
# Фрукты (положи файлы рядом с .py)
apple_img = pygame.image.load("food1.png")
grape_img = pygame.image.load("food2.png")
mango_img = pygame.image.load("food3.png")
apple_img = pygame.transform.scale(apple_img, (snake_block, snake_block))
grape_img = pygame.transform.scale(grape_img, (snake_block, snake_block))
mango_img = pygame.transform.scale(mango_img, (snake_block, snake_block))
food_images = [apple_img, grape_img, mango_img]

# Текстура стены (твоя картинка)
wall_img = pygame.image.load("walls2.png")
wall_img = pygame.transform.scale(wall_img, (snake_block, snake_block))

# ------------------ Ввод/регистрация пользователя ------------------
def get_or_create_user():
    username = input("Введите username: ").strip()
    if not username:
        username = "player"

    cur.execute("SELECT id, level, record FROM users WHERE username=%s", (username,))
    row = cur.fetchone()
    if row:
        user_id, level, record = row
        print(f"Привет, {username}! Твой уровень: {level}, рекорд: {record}")
    else:
        cur.execute("INSERT INTO users(username, level, record) VALUES(%s, %s, %s) RETURNING id, level, record",
                    (username, 1, 0))
        conn.commit()
        user_id, level, record = cur.fetchone()
        print(f"Создан новый пользователь: {username}")
    return username, user_id, level, record

username, user_id, user_level, user_record = get_or_create_user()

# Логика вычисления уровня по рекорду (вариант A — стандарт)
def calc_level_from_record(record):
    lvl = record // 10 + 1
    if lvl < 1:
        lvl = 1
    if lvl > 3:
        lvl = 3
    return lvl

# Устанавливаем начальный уровень (по рекорду)
user_level = calc_level_from_record(user_record)
snake_speed = base_speed + (user_level - 1) * 3

# ------------------ Генерация стен для уровней ------------------
def get_walls_for_level(level):
    walls = []
    if level == 1:
        return walls

    # Level 2: рамка + внутренняя вертикальная колонна + горизонтальная полоса
    if level == 2:
        # рамка по периметру
        for x in range(0, dis_width, snake_block):
            walls.append([x, 0])
            walls.append([x, dis_height - snake_block])
        for y in range(0, dis_height, snake_block):
            walls.append([0, y])
            walls.append([dis_width - snake_block, y])

        # внутренняя колонна (вертикальная) слева
        for y in range(100, 500, snake_block):
            walls.append([200, y])

        # правая горизонтальная полоса
        for x in range(400, 700, snake_block):
            walls.append([x, 300])

    # Level 3: более сложный лабиринт (пример)
    if level == 3:
        # рамка
        for x in range(0, dis_width, snake_block):
            walls.append([x, 0])
            walls.append([x, dis_height - snake_block])
        for y in range(0, dis_height, snake_block):
            walls.append([0, y])
            walls.append([dis_width - snake_block, y])

        # внутренняя сетка/лабиринт
        for x in range(120, 680, snake_block * 4):
            for y in range(80, 520, snake_block):
                walls.append([x, y])

        for x in range(220, 600, snake_block):
            if x % (snake_block * 3) != 0:
                walls.append([x, 220])

        # пара блоков по центру
        for y in range(260, 360, snake_block):
            walls.append([380, y])
            walls.append([420, y])

    return walls

walls = get_walls_for_level(user_level)

# ------------------ Вспомогательные функции ------------------
def show_info(score, level, record):
    score_text = score_font.render(f"Score: {score}  Level: {level}  Record: {record}", True, yellow)
    dis.blit(score_text, [10, 10])

def snake_draw(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def draw_walls(walls):
    for wall in walls:
        dis.blit(wall_img, (wall[0], wall[1]))

def message(m, color, y_offset=0):
    mesg = font_style.render(m, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3 + y_offset])

# Сохранение результата (game over) в user_scores и обновление рекорда/уровня
def save_score(user_id, score, level):
    cur.execute("INSERT INTO user_scores(user_id, score, level) VALUES(%s, %s, %s)",
                (user_id, score, level))
    # обновляем рекорд и уровень пользователя, если нужно
    cur.execute("SELECT record FROM users WHERE id=%s", (user_id,))
    r = cur.fetchone()[0]
    new_record = r
    if score > r:
        new_record = score
        new_level = calc_level_from_record(new_record)
        cur.execute("UPDATE users SET record=%s, level=%s WHERE id=%s", (new_record, new_level, user_id))
    conn.commit()

# Сохранение состояния игры (snake body, head, food, score и т.п.) - JSON
def save_state(user_id, state_dict):
    state_json = json.dumps(state_dict)
    cur.execute("INSERT INTO user_states(user_id, state_json) VALUES(%s, %s)", (user_id, state_json))
    conn.commit()

# ------------------ Начальные параметры игры ------------------
# Позиция головы (центр)
x1 = dis_width / 2
y1 = dis_height / 2
x1_change = 0
y1_change = 0

snake_list = []
length_of_snake = 1

# Спавн еды
def spawn_food():
    fx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
    fy = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
    fimg = random.choice(food_images)
    fw = 1 if fimg == apple_img else 2 if fimg == grape_img else 3
    return fx, fy, fimg, fw

foodx, foody, food_img, food_weight = spawn_food()
food_spawn_time = time.time()
food_lifetime = 10

score = 0
game_over = False
game_close = False
paused = False

# Функция паузы: P - продолжить, S - сохранить состояние и выйти из паузы
def pause_menu():
    global paused
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False
                    return "continue"
                if event.key == pygame.K_s:
                    # Сохраняем текущее состояние в user_states
                    state = {
                        "snake_list": snake_list,
                        "length": length_of_snake,
                        "head": [x1, y1],
                        "changes": [x1_change, y1_change],
                        "food": [foodx, foody],
                        "score": score,
                        "level": user_level,
                        "saved_at": datetime.now().isoformat()
                    }
                    try:
                        save_state(user_id, state)
                        print("Состояние сохранено.")
                    except Exception as e:
                        print("Ошибка при сохранении состояния:", e)
                    paused = False
                    return "saved"

        dis.fill(gray)
        message("PAUSED", blue)
        message("Press P to continue, S to save state (console) ", blue, 40)
        pygame.display.update()
        clock.tick(5)

# ------------------ Игровой цикл ------------------
while not game_over:

    while game_close:
        # Отобразить экран game over, сохранить результат
        dis.fill(blue)
        message("Game Over", red)
        message("Press ESC to exit", red, 40)
        pygame.display.update()

        # Сохраняем результат в БД (после каждой игры)
        try:
            save_score(user_id, score, user_level)
            print(f"Игра окончена. Сохранено {score} очков для {username}.")
        except Exception as e:
            print("Ошибка сохранения счета:", e)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                game_close = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game_over = True
                game_close = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            # Движение змейки (запрет обратного хода)
            if event.key == pygame.K_LEFT and x1_change == 0:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT and x1_change == 0:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP and y1_change == 0:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN and y1_change == 0:
                y1_change = snake_block
                x1_change = 0

            # Пауза
            if event.key == pygame.K_p:
                res = pause_menu()
                if res == "quit":
                    game_over = True

    # Перемещение головы
    x1 += x1_change
    y1 += y1_change

    # Проверка выхода за границы окна
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_close = True

    dis.fill(white)

    # Обновление еды при истечении времени
    if time.time() - food_spawn_time > food_lifetime:
        foodx, foody, food_img, food_weight = spawn_food()
        food_spawn_time = time.time()

    # Отрисовка стен
    walls = get_walls_for_level(user_level)
    draw_walls(walls)

    # Отрисовка еды
    dis.blit(food_img, (foodx, foody))

    # Обновление тела змейки
    snake_head = [x1, y1]
    snake_list.append(snake_head)

    if len(snake_list) > length_of_snake:
        del snake_list[0]

    # Проверка самоколлизии
    for block in snake_list[:-1]:
        if block == snake_head:
            game_close = True

    # Проверка столкновения со стеной (если совпадает координата)
    # walls хранит список [x, y] кратных snake_block
    if snake_head in walls:
        game_close = True

    # Рисуем змейку, инфо, обновляем экран
    snake_draw(snake_block, snake_list)
    show_info(score, user_level, user_record)
    pygame.display.update()

    # Съедание еды
    if x1 == foodx and y1 == foody:
        length_of_snake += food_weight
        score += food_weight

        # Спавн новой еды
        foodx, foody, food_img, food_weight = spawn_food()
        food_spawn_time = time.time()

        # При поедании увеличиваем скорость немного
        snake_speed += 0.5

    # Ограничение FPS по текущей скорости
    clock.tick(snake_speed)

    # При завершении игры (game_close) в цикле выше произойдет сохранение
    # и обновление рекорда при необходимости

# Закрываем pygame и соединение с бд
pygame.quit()
cur.close()
conn.close()
quit()
