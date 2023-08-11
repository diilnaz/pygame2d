import pygame
from pygame.math import Vector2
snd_dir = 'media/snd/'            # Путь до папки со звуками
img_dir = 'media/img/'            # Путь до папки со спрайтами

width = 1366                      # ширина игрового окна
height = 768                      # высота игрового окна


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_dir + 'player/player.png')
        self.rect = self.image.get_rect()
        self.rect.center = [width/2, height/2]
        self.copy = self.image #копия картинки
        self.position = Vector2(self.rect.center)   #перемещение в центр ее копии
        self.direction = Vector2(0, -1)  # Направление вектора - “вверх”
        self.angle = 0 #поворот
        self.speed = 5 #скорость

    def rotate(self, rotate_speed):
        self.direction.rotate_ip(-rotate_speed)  # Изменяем направление взгляда
        self.angle += rotate_speed  # Изменяем угол поворота
        self.image = pygame.transform.rotate(self.copy, self.angle)  # Поворот картинки
        self.rect = self.image.get_rect(center=self.rect.center)  # Изменение рамки
    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.rotate(-5)
        if key[pygame.K_LEFT]:
            self.rotate(5)
        if key[pygame.K_UP]:
            self.position += self.speed * self.direction
            self.rect.center = self.position
        if key[pygame.K_DOWN]:
            self.position -= self.speed * self.direction
            self.rect.center = self.position
0