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
