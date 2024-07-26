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

x1 = 100
y1 = 250

x2 = 550
y2 = 250

x3 = 350
y3 = 250

speed1 = 1
speed2 = 1
speed3 = 1


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
        self.image = transform.scale(image.load(player_img), (95, 355))
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= speed1
        if keys_pressed[K_s] and self.rect.y < 435:
            self.rect.y += speed1

cat1 = Player('nyancat.png', x1, y1, speed1)
cat2 = Player('nyancat2.png', x2, y2, speed2)
ball = GameSprite('kapusta.png', x3, y3, speed3)

game = True
while game:
    window.blit(background, (0, 0))
    ball.reset()
    cat1.reset()
    cat1.update()
    cat2.reset()
    cat2.update()
    for e in event.get():
        if e.type == QUIT:
            game = False

display.update()
