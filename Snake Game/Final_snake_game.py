import pygame as pg
import random as r

pg.init()

#colours
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

#creating window
screen_width = 1100
screen_height = 600
gameWindow = pg.display.set_mode((screen_width,screen_height))
pg.display.set_caption("Snake Game")

pg.display.update()
clock = pg.time.Clock()
font = pg.font.SysFont(None, 55)
f1 = pg.font.SysFont(None, 47)
#Methods
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text,[x,y])

def text_wall(text, color, x, y):
    screen_text = f1.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def plot_snake(gameWindow, color, snk_list, snk_size):
    for x,y in snk_list:
        pg.draw.rect(gameWindow, color, [x, y, snk_size, snk_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)

        text_screen("Welcome to Snake Game", red, 300, 150)
        text_screen("Press space bar to play", red, 300, 200)
        #pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit_game = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    gameloop()
        pg.display.update()
        clock.tick(60)

def gameloop():
    game_exit = False
    game_over = False
    snake_x = 50
    snake_y = 110
    snake_size = 20
    score = 0
    velocity_x = 0
    velocity_y = 0
    food_x = r.randint((screen_width/2)-500, (screen_width/2)+500)
    food_y = r.randint((screen_height/2)-190, (screen_height/2)+200)
    fps = 30
    gameWindow.fill(black, (0, 50, 45, screen_height))
    gameWindow.fill(black, (1050, 50, 50, screen_height))
    gameWindow.fill(black, (0, 550, screen_width, 50))
    gameWindow.fill(black, (0, 50, screen_width, 50))
    snk_len = 1
    snk_list = []

    with open("HighScore.txt","r") as f:
        hs = f.read()
    while not game_exit:
        if game_over:
            with open("HighScore.txt", "w") as f:
                f.write(str(hs))
            gameWindow.fill(white)
            gameWindow.fill(black, (0, 50, 45, screen_height))
            gameWindow.fill(black, (1050, 50, 50, screen_height))
            gameWindow.fill(black, (0, 550, screen_width, 50))
            gameWindow.fill(black, (0, 50, screen_width, 50))
            text_screen("Score : " + str(score), red, 10, 10)
            text_screen("High Score : " + str(hs), red, (screen_width / 2) + 200, 10)
            text_screen("Game Over.", red, 300, 150)
            text_screen("Enter to continue",red,300,200)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game_exit = True
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        welcome()
        else:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game_exit = True
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RIGHT:
                        velocity_x = 5
                        velocity_y = 0
                    if event.key == pg.K_LEFT:
                        velocity_x = -5
                        velocity_y = 0
                    if event.key == pg.K_UP:
                        velocity_y = -5
                        velocity_x = 0
                    if event.key == pg.K_DOWN:
                        velocity_y = 5
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y
            gameWindow.fill(white)
            gameWindow.fill(black, (0, 50, 45, screen_height))
            gameWindow.fill(black, (1050, 50, 50, screen_height))
            gameWindow.fill(black, (0, 550, screen_width, 50))
            gameWindow.fill(black, (0, 50, screen_width, 50))
            if abs(food_x - snake_x) < 20 and abs(food_y - snake_y) < 20:
                score += 10
                food_x = r.randint((screen_width / 2) - 450, (screen_width / 2) + 450)
                food_y = r.randint((screen_height / 2) - 190, (screen_height / 2) + 200)

                snk_len += 5
                if score>int(hs):
                    hs = score
            gameWindow.fill(white)
            gameWindow.fill(black, (0, 50, 45, screen_height))
            gameWindow.fill(black, (1050, 50, 50, screen_height))
            gameWindow.fill(black, (0, 550, screen_width, 50))
            gameWindow.fill(black, (0, 50, screen_width, 50))
            text_screen("Score : " + str(score), red, 10, 10)
            text_screen("High Score : "+str(hs), red, (screen_width/2)+ 200, 10)
            pg.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list) > snk_len:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over = True
            if (snake_x < 50) or (snake_y < 109) or (snake_x > 1050) or (snake_y > 550):
                game_over = True
            plot_snake(gameWindow, black, snk_list, snake_size)
        text_wall("Don't Hit the Wall !!", white, ((screen_width / 2) / 2)+100, 60)
        pg.display.update()
        clock.tick(fps)

    pg.quit()
    quit()
welcome()
