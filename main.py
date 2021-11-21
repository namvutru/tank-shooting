import sys

import pygame
import os
import random

# General Setup
pygame.font.init()
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Tank-shooting")

# Load Background Images
BG = pygame.image.load(os.path.join("images", "grass.png"))

# Game Screen
WIDTH = 850
HEIGHT = 650
Screen = pygame.display.set_mode((WIDTH, HEIGHT))

#  Load Tank Images
TANK_RED = pygame.image.load(os.path.join("images", "tank_red.png"))
# TANK_DARK = pygame.image.load(os.path.join("images", "tank_dark.png"))
# TANK_GREEN = pygame.image.load(os.path.join("images", "tank_green.png"))
# TANK_SAND = pygame.image.load(os.path.join("images", "tank_sand.png"))
TANK_BLUE = pygame.image.load(os.path.join("images", "tank_blue.png"))

#
# # Load Bullet Images
RED_BULLET = pygame.image.load(os.path.join("images", "bullet_red.png"))
# DARK_BULLET = pygame.image.load(os.path.join("images", "bullet_purple.png"))
# GREEN_BULLET = pygame.image.load(os.path.join("images", "bullet_green.png"))
# SAND_BULLET = pygame.image.load(os.path.join("images", "bulletsand2.png"))
BLUE_BULLET = pygame.image.load(os.path.join("images", "bullet_blue.png"))

# Load Wall
WALL = pygame.image.load(os.path.join("images", "wall.png"))
STEEL_WALL = pygame.image.load(os.path.join("images", "steel_wall.png"))

# Chose Player Image
PLAYER_TANK = TANK_BLUE
PLAYER_BULLET = BLUE_BULLET
PLAYER_LASER = []
for i in range(1,12):
    PLAYER_LASER.append(pygame.image.load(os.path.join("images"), "laser1.png"))


# Chose Enemy Image
ENEMY_TANK = TANK_RED
ENEMY_BULLET = RED_BULLET

# LIFE
lives = 5


# Player Class
class Player(pygame.sprite.Sprite):
    COOLDOWN = 30

    def __init__(self, pox_x, pox_y, image, vel=3):
        super().__init__()
        self.image = image
        self.vel = float(vel)
        self.rect = self.image.get_rect()
        self.rect.center = [float(pox_x), float(pox_y)]
        self.direction = 0
        self.cool_down_counter = 0
        self.TANK_WIDTH = self.rect.width
        self.TANK_HEIGHT = self.rect.height

    def collide(self, groups):
        if not (0 < self.rect.x < WIDTH - self.TANK_WIDTH and 0 < self.rect.y < HEIGHT - self.TANK_HEIGHT):
            return True
        for group in groups:
            if pygame.sprite.spritecollide(self, group, False):
                return True

        return False

    def move(self, vel):
        key = pygame.key.get_pressed()
        current_x = self.rect.x
        current_y = self.rect.y
        if key[pygame.K_UP]:
            self.rect.y -= vel
            self.direction = 0
        elif key[pygame.K_DOWN]:
            self.rect.y += vel
            self.direction = 180
        elif key[pygame.K_LEFT]:
            self.rect.x -= vel
            self.direction = 90
        elif key[pygame.K_RIGHT]:
            self.rect.x += vel
            self.direction = 270

        self.image = pygame.transform.rotate(PLAYER_TANK, self.direction)

        # Tank move out of screen
        if self.collide([wall_group, steel_wall_group, enemy_group]):
            self.rect.x = current_x
            self.rect.y = current_y

    def shot(self):
        if self.cool_down_counter == 0:
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                bullet = Bullet(self.rect.centerx, self.rect.centery, PLAYER_BULLET, self.direction)
                bullet_sound = pygame.mixer.Sound(os.path.join("sounds", "gun9.wav"))
                bullet_sound.play()
                if self.direction == 0:
                    bullet.rect.y -= self.TANK_HEIGHT / 2
                if self.direction == 90:
                    bullet.rect.x -= self.TANK_WIDTH / 2
                if self.direction == 180:
                    bullet.rect.y += self.TANK_HEIGHT / 2
                if self.direction == 270:
                    bullet.rect.x += self.TANK_WIDTH / 2
                player_bullet_group.add(bullet)
                self.cool_down_counter += 1

    def laser_fire(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_x]:
            laser = Laser(self.rect.centerx, self.rect.centery, self.direction)
            # bullet_sound = pygame.mixer.Sound(os.path.join("sounds", "gun9.wav"))
            # bullet_sound.play()
            if self.direction == 0:
                laser.rect.y -= self.TANK_HEIGHT / 2
            if self.direction == 90:
                laser.rect.x -= self.TANK_WIDTH / 2
            if self.direction == 180:
                laser.rect.y += self.TANK_HEIGHT / 2
            if self.direction == 270:
                laser.rect.x += self.TANK_WIDTH / 2
            player_bullet_group.add()

    def cooldown(self):  # Control Fire CoolDown
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def update(self):
        self.cooldown()
        self.move(self.vel)
        self.shot()
        self.laser_fire()


# Enemy Class
class Enemy(pygame.sprite.Sprite):
    COOLDOWN = 100
    MOVE_TIME = 50

    def __init__(self, pox_x, pox_y, image, vel=3):
        super().__init__()
        self.image = image
        self.vel = float(vel)
        self.rect = self.image.get_rect()
        self.rect.center = [float(pox_x), float(pox_y)]
        self.direction = 180
        self.fire_cool_down = 0
        self.move_cool_down = 0
        self.TANK_WIDTH = self.rect.width
        self.TANK_HEIGHT = self.rect.height

    def random_direction(self):
        choice = random.randint(0, 2)
        if choice == 0:  # xe tăng di chuyển
            self.move_cool_down = 30
        elif choice == 1:  # xe tăng đổi hướng
            self.direction = random.randint(0, 3) * 90

    def collide(self, groups):
        if not (0 < self.rect.x < WIDTH - self.TANK_WIDTH and 0 < self.rect.y < HEIGHT - self.TANK_HEIGHT):
            return True
        for group in groups:
            if pygame.sprite.spritecollide(self, group, False):
                return True
        enemy_allies = enemy_group.copy()
        enemy_allies.remove(self)
        if pygame.sprite.spritecollide(self, enemy_allies, False):
            return True
        return False

    def move(self):
        if self.move_cool_down == 0:
            self.random_direction()
            self.image = pygame.transform.rotate(ENEMY_TANK, self.direction)
            self.move_cool_down += 1

        current_x = self.rect.x
        current_y = self.rect.y
        if self.direction == 0:
            self.rect.y -= self.vel
        elif self.direction == 180:
            self.rect.y += self.vel
        elif self.direction == 90:
            self.rect.x -= self.vel
        elif self.direction == 270:
            self.rect.x += self.vel

        # không cho xe tank ra ngoài màn hình
        if self.collide([wall_group, steel_wall_group, player_group]):
            self.rect.x = current_x
            self.rect.y = current_y
            self.move_cool_down = 0

    def shot(self):
        if self.fire_cool_down == 0:
            bullet = Bullet(self.rect.centerx, self.rect.centery, ENEMY_BULLET, self.direction)
            bullet_sound = pygame.mixer.Sound(os.path.join("sounds", "gun10.wav"))
            bullet_sound.play()
            if self.direction == 0:
                bullet.rect.y -= self.TANK_HEIGHT / 2
            if self.direction == 90:
                bullet.rect.x -= self.TANK_WIDTH / 2
            if self.direction == 180:
                bullet.rect.y += self.TANK_HEIGHT / 2
            if self.direction == 270:
                bullet.rect.x += self.TANK_WIDTH / 2
            enemy_bullet_group.add(bullet)
            self.fire_cool_down += 1

    def cooldown(self):  # đếm ngược nạp đạn
        if self.fire_cool_down >= self.COOLDOWN:
            self.fire_cool_down = 0
        elif self.fire_cool_down > 0:
            self.fire_cool_down += 1

    def move_cooldown(self):  # đếm ngược thời gian di chuyển
        if self.move_cool_down >= self.MOVE_TIME:
            self.move_cool_down = 0
        elif self.move_cool_down > 0:
            self.move_cool_down += 1

    def update(self):
        self.move_cooldown()
        self.move()
        self.cooldown()
        self.shot()


# Bullet Class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, image, direction, vel=5):
        super().__init__()
        self.direction = direction
        self.image = pygame.transform.rotate(image, direction + 90)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.vel = vel

    def move(self):
        if self.direction == 0:
            self.rect.y -= self.vel
        if self.direction == 90:
            self.rect.x -= self.vel
        if self.direction == 180:
            self.rect.y += self.vel
        if self.direction == 270:
            self.rect.x += self.vel

    def collide(self):
        if not (0 < self.rect.x < WIDTH and 0 < self.rect.y < HEIGHT):
            if self in player_bullet_group:
                player_bullet_group.remove(self)
            else:
                enemy_bullet_group.remove(self)

        if pygame.sprite.spritecollide(self, enemy_group, False):
            if self in player_bullet_group:
                player_bullet_group.remove(self)
                pygame.sprite.spritecollide(self, enemy_group, True)

        if self in enemy_bullet_group and pygame.sprite.spritecollide(self, player_group, True):
            global lives
            if lives > 1:
                player = Player(WIDTH / 2 - PLAYER_TANK.get_width(), HEIGHT - PLAYER_TANK.get_height(), PLAYER_TANK)
                player_group.add(player)
            lives -= 1
            enemy_bullet_group.remove(self)

        if pygame.sprite.spritecollide(self, wall_group, True):
            if self in player_bullet_group:
                player_bullet_group.remove(self)
            else:
                enemy_bullet_group.remove(self)

        if pygame.sprite.spritecollide(self, steel_wall_group, False):
            if self in player_bullet_group:
                player_bullet_group.remove(self)
            else:
                enemy_bullet_group.remove(self)

    def update(self):
        self.move()
        self.collide()


# Laser Class
class Laser(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, direction):
        super().__init__()
        self.laser_sheet = PLAYER_LASER

        for i in range(len(self.laser_sheet)):
            self.laser_sheet[i] = pygame.transform.rotate(self.laser_sheet[i],direction)

        self.current_image = 0
        self.image = self.laser_sheet[self.current_image]

        self.rect = self.image.get_rect()
        self.rect.midleft = [pos_x, pos_y]

    def update(self):
        self.current_image += 1
        if self.current_image >= len(self.laser_sheet):
            player_laser_group.remove(self)
        self.image = self.laser_sheet[self.current_image]


# Wall Class
class Wall(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]


# Generate Rule - Check Overlap
def check_over_lap(object, groups):
    for group in groups:
        if pygame.sprite.spritecollide(object, group, False):
            return False
    return True


# Set Player
player1 = Player(WIDTH / 2 - PLAYER_TANK.get_width(), HEIGHT - PLAYER_TANK.get_height(), PLAYER_TANK)
player_group = pygame.sprite.Group()
player_group.add(player1)
player_bullet_group = pygame.sprite.Group()
player_laser_group = pygame.sprite.Group()
# Set Wall
wall_group = pygame.sprite.Group()
for i in range(30):
    wall = Wall(WALL.get_width() * random.randint(1, 16),
                WALL.get_height() * random.randint(1, 12), WALL)
    if check_over_lap(wall, [wall_group, player_group]):
        wall_group.add(wall)

# Set Steel Wall
# Set Wall
steel_wall_group = pygame.sprite.Group()
for i in range(30):
    wall = Wall(STEEL_WALL.get_width() * random.randint(1, 16),
                STEEL_WALL.get_height() * random.randint(1, 12), STEEL_WALL)
    if check_over_lap(wall, [wall_group, steel_wall_group, player_group]):
        steel_wall_group.add(wall)

# Set Enemy
enemy_group = pygame.sprite.Group()
for i in range(30):
    enemy = Enemy(ENEMY_TANK.get_width() * random.randint(1, 16),
                  ENEMY_TANK.get_height() * random.randint(1, 12),
                  ENEMY_TANK)
    if check_over_lap(enemy, [wall_group, enemy_group, steel_wall_group, player_group]):
        enemy_group.add(enemy)
enemy_bullet_group = pygame.sprite.Group()

# Game run
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    Screen.blit(BG, (0, 0))

    wall_group.draw(Screen)
    steel_wall_group.draw(Screen)

    player_laser_group.draw(Screen)
    player_laser_group.update()
    player_bullet_group.draw(Screen)
    player_bullet_group.update()
    player_group.draw(Screen)
    player_group.update()

    enemy_group.draw(Screen)
    enemy_group.update()
    enemy_bullet_group.draw(Screen)
    enemy_bullet_group.update()


    main_font = pygame.font.SysFont("comicsans", 50)
    lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
    Screen.blit(lives_label, (10, 10))

    clock.tick(60)
