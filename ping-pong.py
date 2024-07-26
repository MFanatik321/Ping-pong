from pygame import *

WIN_W = 700
WIN_H = 500

#Окоши в которые можно прыгать
window = display.set_mode((WIN_W, WIN_H))
display.set_caption("Ping-pong")
background = transform.scale(image.load("planet.png"),(WIN_W, WIN_H))

#переменные
clock = time.Clock()
FPS = 60
clock.tick(120)

x1 = 15
y1 = 0

x2 = 600
y2 = 0

x3 = 320
y3 = 0

speed = 1

speed_x = 2
speed_y = 2

#Классы
class GameSprite(sprite.Sprite):
    def __init__(self, player_img, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_img), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def __init__(self, player_img, player_x, player_y, player_speed):
        super().__init__(player_img, player_x, player_y, player_speed)
        self.image = transform.scale(image.load(player_img), (45, 150))
    def update(self, up, down, stop_value=50):
        keys_pressed1 = key.get_pressed()
        if keys_pressed1[up] and self.rect.y > 5:
            self.rect.y -= speed
        if keys_pressed1[down] and self.rect.y < WIN_H - stop_value:
            self.rect.y += speed


class Ball(GameSprite):
    def __init__(self, player_img, player_x, player_y, player_speed):
        super().__init__(player_img, player_x, player_y, player_speed)
        self.image = transform.scale(image.load(player_img), (65, 65))
        self.speed_x = player_speed
        self.speed_y = player_speed
    def update(self, stop_value=50):
        if self.rect.y > WIN_H - 50 or self.rect.y < 0:
            self.speed_y *= -1
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

cat1 = Player('nyancat.png', x1, y1, speed)
cat2 = Player('nyancat2.png', x2, y2, speed)
ball = Ball('kapusta.png', x3, y3, speed)

#Цикл
font.init()
font = font.SysFont('Arial', 70)
lose1 = font.render('Player 1 LOSE', True, (255, 215, 0))
lose2 = font.render('Player 2 LOSE', True, (255, 215, 0))
finish = False
game = True
while game:
    if not finish:
        window.blit(background, (0, 0))
        ball.reset()
        ball.update()
        cat1.reset()
        cat1.update(K_w, K_s, 150)
        cat2.reset()
        cat2.update(K_UP, K_DOWN, 150)
        if sprite.collide_rect(cat1, ball):
            ball.speed_x *= -1 
        if sprite.collide_rect(cat2, ball):
            ball.speed_x *= -1
        if ball.rect.x > WIN_W - 50:
            window.blit(lose2, (150, 210))
            finish = True
        if ball.rect.x < 0:
            window.blit(lose1, (150, 210))
            finish = True
        display.update()
    for e in event.get():
        if e.type == QUIT:
            game = False
