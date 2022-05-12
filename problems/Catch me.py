import math
import pygame

WIDTH = 600
HEIGHT = 600
FPS = 30

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

# Задаем цвета
WHITE = (255, 255, 255)
RED = (255, 10, 10)
BLACK = (0, 0, 0)
YELLOW = (225, 225, 0)
GREEN = (81,164,82)

#Хар-ки
SPEED = 10
ENEMY_SPEED = 0.7



class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.radius = 25
        pygame.draw.circle(self.image, YELLOW, self.image.get_rect().center, self.radius)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH -10, HEIGHT -10)
        self.speedx = 0
        self.speedy = 0


    def update(self):
        #Движение спрайта
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -SPEED
            self.speedy = 0
        if keystate[pygame.K_RIGHT]:
            self.speedx = SPEED
            self.speedy = 0
        if keystate[pygame.K_UP]:
            self.speedx = 0
            self.speedy = -SPEED
        if keystate[pygame.K_DOWN]:
            self.speedx = 0
            self.speedy = SPEED
        if keystate[pygame.K_LEFT] and keystate[pygame.K_UP]:
            self.speedx = -SPEED
            self.speedy = -SPEED
        if keystate[pygame.K_LEFT] and keystate[pygame.K_DOWN]:
            self.speedx = -SPEED
            self.speedy = SPEED
        if keystate[pygame.K_RIGHT] and keystate[pygame.K_UP]:
            self.speedx = SPEED
            self.speedy = -SPEED
        if keystate[pygame.K_RIGHT] and keystate[pygame.K_DOWN]:
            self.speedx = SPEED
            self.speedy = SPEED
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        #Пересечение границ
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def check_collision(self):
        if self.rect.right > player.rect.left and \
                self.rect.left < player.rect.right and \
                self.rect.bottom > player.rect.top and \
                self.rect.top < player.rect.bottom:
            return True

class Enemy(pygame.sprite.Sprite):
    def __init__(self,st_x,st_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = st_x
        self.rect.y = st_y
        self.speedx = 0
        self.speedy = 0

    def update(self,plx,ply):
        #Преследование игрока
        try:
            self.speedx = ENEMY_SPEED * (plx-self.rect.x)/float(math.sqrt(plx^2 + self.rect.x^2))
            self.speedy = ENEMY_SPEED * (ply-self.rect.y)/float(math.sqrt(ply^2 + self.rect.y^2))
        except ZeroDivisionError:
            self.speedx = 0
            self.speedy = 0
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        #Пересечение границ
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class Finish(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (25,25)
    def check_collision(self,player):
        if self.rect.right > player.rect.left and \
                self.rect.left < player.rect.right and \
                self.rect.bottom > player.rect.top and \
                self.rect.top < player.rect.bottom:
            return True

    def update(self):
        self.rect.center = (25, 25)

# Создаем игру и окно
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Catch me if you can')
clock = pygame.time.Clock()

txt = ""

all_sprites = pygame.sprite.Group()
player = Player()
finish = Finish()

#Добавляем врагов
enemies = pygame.sprite.Group()
a = Enemy(100,20)
b = Enemy(40,150)
enemies.add(a)
enemies.add(b)

all_sprites.add(a)
all_sprites.add(b)
all_sprites.add(player)
all_sprites.add(finish)
# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    player.update()
    enemies.update(player.rect.x, player.rect.y)
    finish.update()
    hits = pygame.sprite.spritecollide(player, enemies, False)#обработка столкновений с врагами
    if hits:
        running = False
        txt = "You LOST"

    if finish.check_collision(player):#обработка условия победы
        running = False
        txt = "You WIN"

    # Отрисовка
    screen.fill(WHITE)
    all_sprites.draw(screen)
    if txt !="":
        screen.fill(WHITE)
        draw_text(screen, txt, 40, WIDTH / 2, HEIGHT / 2)

    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()