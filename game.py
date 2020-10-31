import pygame #만들때 필요한 라이브러리
import sys #창끄기 실습
import time #시간 라이브러리
import random #랜덤 라이브러리

from pygame.locals import *

WHITE = (255, 255,255)

WINDOW_WIDTH = 800
WINDOW_HEIGH = 600

if __name__ == '__main__':
    pygame.init()
window = pygame.display.set_mode()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGH), 0, 32)
pygame.display.set_caption('Python Game')
surface = pygame.Surface(window.get_size())
surface = surface.convert()
surface.fill(WHITE)
clock = pygame.time.Clock()
pygame.key.set_repeat(1, 40)
window.blit(surface, (0,0))
