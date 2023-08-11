import random
from pygame.math import Vector2
import pygame


snd_dir = 'media/snd/'                                  # Путь до папки со звуками
img_dir = 'media/img/'                                  # Путь до папки со спрайтами

width = 1366                                            # ширина игрового окна
height = 768                                            # высота игрового окна


# Создаем класс врага сверху
class EnemyTop(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)             # Враг - спрайт

        self.image = pygame.image.load(img_dir + 'enemy_top/1.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width)          # По горизонтали - случайное положение
        self.rect.y = 0                                 # По вертикали - сверху
        self.copy = self.image
        self.position = Vector2(self.rect.center)
        self.direction = Vector2(0, -1)
        self.angle = 0
        self.speedx = random.randint(-5, -1)
        self.speedy = random.randint(-5, 5)
    def rotate(self, rotate_speed):
        self.direction.rotate_ip(-rotate_speed)
        self.angle += rotate_speed
        self.image = pygame.transform.rotate(self.copy, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
#это врагам
    def update(self):
        self.rotate(5)  # Вращаемся на 5 градусов против часовой стрелки
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.x > width or self.rect.right < 0 or self.rect.bottom < 0:
            self.rect.x = random.randint(0, width)
            self.rect.y = height
            self.speedx = random.randint(-5, 5)
            self.speedy = random.randint(-5, -1)