import pygame
from player import Player               # Из файла player подключаем класс Player
from bullet import Bullet
from enemy_left import EnemyLeft
from enemy_right import EnemyRight
from enemy_top import EnemyTop
from enemy_bottom import EnemyBottom
pygame.init()                           # Инициализируем модуль pygame

width = 1366                            # ширина игрового окна
height = 768                            # высота игрового окна
fps = 30                                # частота кадров в секунду
game_name = "Shooter"                   # название нашей игры

def get_hit_sprite(hits_dict):
    for hit in hits_dict.values():
        return hit[0]

# Цвета
BLACK = "#000000"
WHITE = "#FFFFFF"
RED = "#FF0000"
GREEN = "#008000"
BLUE = "#0000FF"
CYAN = "#00FFFF"

all_sprites = pygame.sprite.Group()    # Создаем группу для всех спрайтов
mobs_sprites = pygame.sprite.Group()   # Создаем группу для спрайтов мобов
bullets_sprites = pygame.sprite.Group()   # Создаем группу для спрайтов пуль
players_sprites = pygame.sprite.Group()   # Создаем группу для спрайтов игроков

snd_dir = 'media/snd/'            # Путь до папки со звуками
img_dir = 'media/img/'            # Путь до папки со спрайтами

icon = pygame.image.load(img_dir + 'icon.png')         # Загружаем файл с иконкой
pygame.display.set_icon(icon)                # Устанавливаем иконку в окно

#Создаем игровой экран
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(game_name)   # Заголовок окна


player = Player()                       # Создаем игрока класса Player
enemy_left = EnemyLeft()
enemy_right = EnemyRight()
enemy_top = EnemyTop()
enemy_bottom = EnemyBottom()


all_sprites.add(player)                 # Добавляем игрока в группу спрайтов
players_sprites.add(player)             # Добавляем игрока в группу игроков
all_sprites.add([enemy_left, enemy_right, enemy_top, enemy_bottom])
mobs_sprites.add([enemy_left, enemy_right, enemy_top, enemy_bottom])

timer = pygame.time.Clock()             # Создаем таймер pygame
run = True

pygame.mixer.music.load(snd_dir + "music.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

while run:                              # Начинаем бесконечный цикл
    timer.tick(fps)			            # Контроль времени (обновление игры)
    all_sprites.update()                 # Выполняем действия всех спрайтов в группе
    for event in pygame.event.get():     # Обработка ввода (события)
        if event.type == pygame.QUIT:    # Проверить закрытие окна
            run = False                  # Завершаем игровой цикл
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.snd_shoot.play()
                bullet = Bullet(player)     # Создаем пулю передавая внутрь информацию об игроке
                all_sprites.add(bullet)     # Добавляем пулю ко всем спрайтам
                bullets_sprites.add(bullet) # Добавляем пулю ко всем пулям

    shots = pygame.sprite.groupcollide(bullets_sprites, mobs_sprites, True, True)
    if shots:
        sprite = get_hit_sprite(shots)  # Получаем спрайт из второй группы
        sprite.snd_expl.play()  # Воспроизводим звук скрежета

    scratch = pygame.sprite.groupcollide(mobs_sprites, players_sprites, False, False)
    if scratch:
        sprite = get_hit_sprite(scratch)
        sprite.snd_scratch.play()

    # Рендеринг (прорисовка)
    screen.fill(CYAN)                     # Заливка заднего фона
    all_sprites.draw(screen)              # Отрисовываем все спрайты
    pygame.display.update()               # Обновляем экран

pygame.quit()
