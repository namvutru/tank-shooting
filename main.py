import sys

import pygame
import os
import random

# General Setup
pygame.font.init()
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Tank-shooting")

# Game Screen
WIDTH = 850
HEIGHT = 650
Screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Text on Screen
LIVES = 5
Score = 0

# Load Background Images
BG = pygame.image.load(os.path.join("images", "back_ground.png"))

#  Load Tank Images
TANK_RED = pygame.image.load(os.path.join("images", "tank_red.png"))
TANK_GREEN = pygame.image.load(os.path.join("images", "tank_green.png"))
TANK_BLUE = pygame.image.load(os.path.join("images", "tank_blue.png"))
TANK_GRAY = pygame.image.load(os.path.join("images", "tank_gray.png"))
# Load Bullet Images
RED_BULLET = pygame.image.load(os.path.join("images", "bullet_red.png"))
GRAY_BULLET = pygame.image.load(os.path.join("images", "bullet_gray.png"))
GREEN_BULLET = pygame.image.load(os.path.join("images", "bullet_green.png"))
BLUE_BULLET = pygame.image.load(os.path.join("images", "bullet_blue.png"))

# Load Wall + GRASS + MAIN HOUSE
WALL = pygame.image.load(os.path.join("images", "wall.png"))
STEEL_WALL = pygame.image.load(os.path.join("images", "steel_wall.png"))
GRASS = pygame.image.load(os.path.join("images", "grass1.png")).convert_alpha(Screen)
HAWK = pygame.image.load(os.path.join("images", "hawk.png"))


def draw_map():
    map = ['.#..#.##.##.#..#.',
           '.#..#.##@##.#..#.',
           '.#..#.......#..#.',
           '......##.##......',
           '......##.##......',
           '@.###G......###G@',
           '.....G##.##..GGG.',
           '......#####..GGG.',
           '.#..#.#####.#..#.',
           '.#..#.##.##.#..#.',
           '.#..#.##.##.#..#.',
           '.#..#..###..#..#.',
           '.......#H#.......']

    map1 = ['.#..@.##.#@.#..#.',
            '.#..@.##@##.#..#.',
            '.#..#.......#.@#.',
            '......##.##.@....',
            '......##.##......',
            '@.###...@...###.@',
            '......##.##......',
            '...@..###@#......',
            '@#.@#.#####.#..#.',
            '.#..#.##.##.#..#.',
            '.#..#.##.##.#..#.',
            '.#..#..###..#..#.',
            '.......#H#.......']

    for row in range(13):  # 650/50=13
        for col in range(len(map[row])):  # 850/50=17
            if map[row][col] == '#':
                wall = Wall(WALL.get_width() * col + WALL.get_width() / 2,
                            WALL.get_height() * row + WALL.get_width() / 2, WALL)
                wall_group.add(wall)
            elif map[row][col] == '@':
                stone = Wall(STEEL_WALL.get_width() * col + STEEL_WALL.get_width() / 2,
                             STEEL_WALL.get_height() * row + STEEL_WALL.get_width() / 2, STEEL_WALL)
                steel_wall_group.add(stone)
            elif map[row][col] == 'G':
                grass = Wall(GRASS.get_width() * col + WALL.get_width() / 2,
                             GRASS.get_height() * row + WALL.get_width() / 2, GRASS)
                grass_group.add(grass)
            elif map[row][col] == 'H':
                hawk = Wall(HAWK.get_width() * col + WALL.get_width() / 2,
                            HAWK.get_height() * row + WALL.get_width() / 2, HAWK)
                hawk_group.add(hawk)

    # print(len(map[0][1]))
    for row in range(13):  # 850/50=17
        for col in range(len(map[row])):
            print(map[row][col], sep='', end='')
        print()


TYPE_BULLET = {}
TYPE_TANK = {}


#  Bullet Type - Chỉnh thuộc tính của đạn
def set_bullet():
    RED_BULLET_VEL = 2
    GREEN_BULLET_VEL = 3
    GRAY_BULLET_VEL = 4
    BLUE_BULLET_VEL = 4
    TYPE_BULLET["red"] = {
        "image": RED_BULLET,
        "vel": RED_BULLET_VEL
    }
    TYPE_BULLET["green"] = {
        "image": GREEN_BULLET,
        "vel": GREEN_BULLET_VEL
    }
    TYPE_BULLET["gray"] = {
        "image": GRAY_BULLET,
        "vel": GRAY_BULLET_VEL
    }
    TYPE_BULLET["blue"] = {
        "image": BLUE_BULLET,
        "vel": BLUE_BULLET_VEL
    }


#  Tank Type - Chỉnh thuộc tính xe tank
def set_Tank_stats():
    VEL_RED = 1
    HEALTH_RED = 3

    VEL_GREEN = 2
    HEALTH_GREEN = 2

    VEL_GRAY = 3
    HEALTH_GRAY = 1

    VEL_BLUE = 2.5
    HEALTH_BLUE = 2
    TYPE_TANK["red"] = {
        "image": TANK_RED,
        "vel": VEL_RED,
        "health": HEALTH_RED
    }
    TYPE_TANK["green"] = {
        "image": TANK_GREEN,
        "vel": VEL_GREEN,
        "health": HEALTH_GREEN
    }
    TYPE_TANK["gray"] = {
        "image": TANK_GRAY,
        "vel": VEL_GRAY,
        "health": HEALTH_GRAY
    }
    TYPE_TANK["blue"] = {
        "image": TANK_BLUE,
        "vel": VEL_BLUE,
        "health": HEALTH_BLUE
    }

set_bullet()
set_Tank_stats()



# Chose Player Image

PLAYER_COLOR = "blue"
REBORN_X = WIDTH / 2 - WALL.get_width() * 2
REBORN_Y = HEIGHT - WALL.get_height()

PLAYER_LASER = []
PLAYER_BARRIER = []

# Explosion
EXPLOSION = []
SMALL_EXPLOSION = []


# Load Animation Image (PLAYER_LASER,  PLAYER_BARRIER, EXPLOSION)
def add_animation_sheet():
    EXPLOSION.append(pygame.image.load(os.path.join("images", "explo (1).png")).convert_alpha(Screen))
    EXPLOSION.append(pygame.image.load(os.path.join("images", "explo (2).png")).convert_alpha(Screen))
    EXPLOSION.append(pygame.image.load(os.path.join("images", "explo (3).png")).convert_alpha(Screen))
    EXPLOSION.append(pygame.image.load(os.path.join("images", "explo (4).png")).convert_alpha(Screen))
    EXPLOSION.append(pygame.image.load(os.path.join("images", "explo (5).png")).convert_alpha(Screen))
    EXPLOSION.append(pygame.image.load(os.path.join("images", "explo (6).png")).convert_alpha(Screen))
    EXPLOSION.append(pygame.image.load(os.path.join("images", "explo (7).png")).convert_alpha(Screen))
    EXPLOSION.append(pygame.image.load(os.path.join("images", "explo (8).png")).convert_alpha(Screen))
    EXPLOSION.append(pygame.image.load(os.path.join("images", "explo (9).png")).convert_alpha(Screen))
    EXPLOSION.append(pygame.image.load(os.path.join("images", "explo (10).png")).convert_alpha(Screen))
    EXPLOSION.append(pygame.image.load(os.path.join("images", "explo (11).png")).convert_alpha(Screen))
    EXPLOSION.append(pygame.image.load(os.path.join("images", "explo (12).png")).convert_alpha(Screen))
    EXPLOSION.append(pygame.image.load(os.path.join("images", "explo (13).png")).convert_alpha(Screen))
    EXPLOSION.append(pygame.image.load(os.path.join("images", "explo (14).png")).convert_alpha(Screen))
    EXPLOSION.append(pygame.image.load(os.path.join("images", "explo (15).png")).convert_alpha(Screen))
    EXPLOSION.append(pygame.image.load(os.path.join("images", "explo (16).png")).convert_alpha(Screen))
    EXPLOSION.append(pygame.image.load(os.path.join("images", "explo (17).png")).convert_alpha(Screen))
    EXPLOSION.append(pygame.image.load(os.path.join("images", "explo (18).png")).convert_alpha(Screen))
    EXPLOSION.append(pygame.image.load(os.path.join("images", "explo (19).png")).convert_alpha(Screen))
    EXPLOSION.append(pygame.image.load(os.path.join("images", "explo (20).png")).convert_alpha(Screen))
    EXPLOSION.append(pygame.image.load(os.path.join("images", "explo (21).png")).convert_alpha(Screen))
    EXPLOSION.append(pygame.image.load(os.path.join("images", "explo (22).png")).convert_alpha(Screen))
    EXPLOSION.append(pygame.image.load(os.path.join("images", "explo (23).png")).convert_alpha(Screen))
    EXPLOSION.append(pygame.image.load(os.path.join("images", "explo (24).png")).convert_alpha(Screen))
    EXPLOSION.append(pygame.image.load(os.path.join("images", "explo (25).png")).convert_alpha(Screen))

    # Small Explosion
    SMALL_EXPLOSION.append(pygame.image.load(os.path.join("images", "bullet_collide (1).png")).convert_alpha(Screen))
    SMALL_EXPLOSION.append(pygame.image.load(os.path.join("images", "bullet_collide (2).png")).convert_alpha(Screen))
    SMALL_EXPLOSION.append(pygame.image.load(os.path.join("images", "bullet_collide (3).png")).convert_alpha(Screen))
    SMALL_EXPLOSION.append(pygame.image.load(os.path.join("images", "bullet_collide (4).png")).convert_alpha(Screen))
    SMALL_EXPLOSION.append(pygame.image.load(os.path.join("images", "bullet_collide (5).png")).convert_alpha(Screen))
    SMALL_EXPLOSION.append(pygame.image.load(os.path.join("images", "bullet_collide (6).png")).convert_alpha(Screen))
    SMALL_EXPLOSION.append(pygame.image.load(os.path.join("images", "bullet_collide (7).png")).convert_alpha(Screen))
    SMALL_EXPLOSION.append(pygame.image.load(os.path.join("images", "bullet_collide (8).png")).convert_alpha(Screen))
    # SMALL_EXPLOSION.append(pygame.image.load(os.path.join("images", "bullet_collide (9).png")).convert_alpha(Screen))
    # SMALL_EXPLOSION.append(pygame.image.load(os.path.join("images", "bullet_collide (10).png")).convert_alpha(Screen))
    # SMALL_EXPLOSION.append(pygame.image.load(os.path.join("images", "bullet_collide (11).png")).convert_alpha(Screen))
    # SMALL_EXPLOSION.append(pygame.image.load(os.path.join("images", "bullet_collide (12).png")).convert_alpha(Screen))
    # SMALL_EXPLOSION.append(pygame.image.load(os.path.join("images", "bullet_collide (13).png")).convert_alpha(Screen))
    # SMALL_EXPLOSION.append(pygame.image.load(os.path.join("images", "bullet_collide (14).png")).convert_alpha(Screen))
    # SMALL_EXPLOSION.append(pygame.image.load(os.path.join("images", "bullet_collide (15).png")).convert_alpha(Screen))

    # Load Laser
    PLAYER_LASER.append(pygame.image.load(os.path.join("images", "laser1.png")))
    PLAYER_LASER.append(pygame.image.load(os.path.join("images", "laser2.png")))
    PLAYER_LASER.append(pygame.image.load(os.path.join("images", "laser3.png")))
    PLAYER_LASER.append(pygame.image.load(os.path.join("images", "laser4.png")))
    PLAYER_LASER.append(pygame.image.load(os.path.join("images", "laser6.png")))
    PLAYER_LASER.append(pygame.image.load(os.path.join("images", "laser7.png")))
    PLAYER_LASER.append(pygame.image.load(os.path.join("images", "laser8.png")))
    PLAYER_LASER.append(pygame.image.load(os.path.join("images", "laser9.png")))
    PLAYER_LASER.append(pygame.image.load(os.path.join("images", "laser10.png")))
    PLAYER_LASER.append(pygame.image.load(os.path.join("images", "laser11.png")))
    PLAYER_LASER.append(pygame.image.load(os.path.join("images", "laser12.png")))

    # Load Barrier
    PLAYER_BARRIER.append(pygame.image.load(os.path.join("images", "barrier (1).png")).convert_alpha(Screen))
    PLAYER_BARRIER.append(pygame.image.load(os.path.join("images", "barrier (2).png")).convert_alpha(Screen))
    PLAYER_BARRIER.append(pygame.image.load(os.path.join("images", "barrier (3).png")).convert_alpha(Screen))
    PLAYER_BARRIER.append(pygame.image.load(os.path.join("images", "barrier (4).png")).convert_alpha(Screen))
    PLAYER_BARRIER.append(pygame.image.load(os.path.join("images", "barrier (5).png")).convert_alpha(Screen))
    PLAYER_BARRIER.append(pygame.image.load(os.path.join("images", "barrier (6).png")).convert_alpha(Screen))
    PLAYER_BARRIER.append(pygame.image.load(os.path.join("images", "barrier (7).png")).convert_alpha(Screen))
    PLAYER_BARRIER.append(pygame.image.load(os.path.join("images", "barrier (8).png")).convert_alpha(Screen))
    PLAYER_BARRIER.append(pygame.image.load(os.path.join("images", "barrier (9).png")).convert_alpha(Screen))
    PLAYER_BARRIER.append(pygame.image.load(os.path.join("images", "barrier (10).png")).convert_alpha(Screen))
    PLAYER_BARRIER.append(pygame.image.load(os.path.join("images", "barrier (11).png")).convert_alpha(Screen))
    PLAYER_BARRIER.append(pygame.image.load(os.path.join("images", "barrier (12).png")).convert_alpha(Screen))
    PLAYER_BARRIER.append(pygame.image.load(os.path.join("images", "barrier (13).png")).convert_alpha(Screen))
    PLAYER_BARRIER.append(pygame.image.load(os.path.join("images", "barrier (14).png")).convert_alpha(Screen))
    PLAYER_BARRIER.append(pygame.image.load(os.path.join("images", "barrier (15).png")).convert_alpha(Screen))
    PLAYER_BARRIER.append(pygame.image.load(os.path.join("images", "barrier (16).png")).convert_alpha(Screen))
    PLAYER_BARRIER.append(pygame.image.load(os.path.join("images", "barrier (17).png")).convert_alpha(Screen))
    PLAYER_BARRIER.append(pygame.image.load(os.path.join("images", "barrier (18).png")).convert_alpha(Screen))
    PLAYER_BARRIER.append(pygame.image.load(os.path.join("images", "barrier (19).png")).convert_alpha(Screen))
    PLAYER_BARRIER.append(pygame.image.load(os.path.join("images", "barrier (20).png")).convert_alpha(Screen))
    PLAYER_BARRIER.append(pygame.image.load(os.path.join("images", "barrier (21).png")).convert_alpha(Screen))
    PLAYER_BARRIER.append(pygame.image.load(os.path.join("images", "barrier (22).png")).convert_alpha(Screen))


add_animation_sheet()


# Tank Class
class Tank(pygame.sprite.Sprite):

    def __init__(self, pox_x, pox_y, color):
        super().__init__()
        self.color = color
        self.image = TYPE_TANK[color]["image"]
        self.vel = TYPE_TANK[color]["vel"]
        self.health = TYPE_TANK[color]["health"]
        self.rect = self.image.get_rect()
        self.rect.center = [float(pox_x), float(pox_y)]

        self.direction = 0
        self.cool_down_counter = 0
        self.TANK_WIDTH = self.rect.width
        self.TANK_HEIGHT = self.rect.height

    def collide(self, groups):
        pass

    def move(self):
        pass

    def shot(self):
        pass

    def cooldown(self):
        pass


# Player Class
class Player(Tank):
    COOLDOWN = 30

    def __init__(self, pox_x, pox_y):
        super().__init__(pox_x, pox_y, PLAYER_COLOR)
        self.moveable = True
        self.has_barrier = False

    def collide(self, groups):
        if not (0 < self.rect.x < WIDTH - self.TANK_WIDTH and 0 < self.rect.y < HEIGHT - self.TANK_HEIGHT):
            return True
        for group in groups:
            if pygame.sprite.spritecollide(self, group, False):
                return True

        return False

    def move(self):
        if not self.moveable:
            return
        key = pygame.key.get_pressed()
        current_x = self.rect.x
        current_y = self.rect.y
        if key[pygame.K_UP]:
            self.rect.y -= self.vel
            self.direction = 0
        elif key[pygame.K_DOWN]:
            self.rect.y += self.vel
            self.direction = 180
        elif key[pygame.K_LEFT]:
            self.rect.x -= self.vel
            self.direction = 90
        elif key[pygame.K_RIGHT]:
            self.rect.x += self.vel
            self.direction = 270

        self.image = pygame.transform.rotate(TYPE_TANK[PLAYER_COLOR]["image"], self.direction)

        # Tank move out of screen
        if self.collide([wall_group, steel_wall_group, enemy_group]):
            self.rect.x = current_x
            self.rect.y = current_y

    def shot(self):
        if self.cool_down_counter == 0:
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                bullet = Bullet(self.rect.centerx, self.rect.centery, self.color, self.direction)
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
        if key[pygame.K_x] and len(player_laser_group) == 0 and len(player_barrier_group) == 0:
            self.moveable = False
            laser = Laser(self.rect.centerx, self.rect.centery, self.direction)
            self.open_barrier(22)
            laser_sound = pygame.mixer.Sound(os.path.join("sounds", "laser.wav"))
            laser_sound.play()
            if self.direction == 0:
                laser.rect.y -= (PLAYER_LASER[0].get_height() / 2) + self.TANK_WIDTH * 2
            if self.direction == 90:
                laser.rect.x -= PLAYER_LASER[0].get_width() / 2
            if self.direction == 180:
                laser.rect.y += (PLAYER_LASER[0].get_height() / 2) + self.TANK_HEIGHT * 2
            if self.direction == 270:
                laser.rect.x += PLAYER_LASER[0].get_width() / 2
            player_laser_group.add(laser)

    def cooldown(self):  # Control Fire CoolDown
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def open_barrier(self, time):
        barrier = Barrier(self.rect.centerx, self.rect.centery, time)
        player_barrier_group.add(barrier)

    def update(self):
        self.cooldown()
        self.move()
        self.shot()
        self.laser_fire()


# Enemy Class
class Enemy(Tank):
    COOLDOWN = 100
    MOVE_TIME = 50

    def __init__(self, pos_x, pos_y, color):
        super().__init__(pos_x, pos_y, color)
        self.direction = 180
        self.fire_cool_down = 0
        self.move_cool_down = 0

    def random_direction(self):
        choice = random.randint(0, 2)
        if choice == 0:  # xe tăng di chuyển
            self.move_cool_down = 30
        elif choice == 1:  # xe tăng đổi hướng
            self.direction = random.randint(0, 3) * 90

    def collide(self, groups):
        if pygame.sprite.spritecollide(self, player_laser_group, False):
            explosion_group.add(Explosion(self.rect.centerx, self.rect.centery, EXPLOSION))
            return False
        if pygame.sprite.spritecollide(self, player_bullet_group, True):
            self.health -= 1
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
            self.image = pygame.transform.rotate(TYPE_TANK[self.color]["image"], self.direction)
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
            bullet = Bullet(self.rect.centerx, self.rect.centery, self.color, self.direction)
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
        self.COOLDOWN = random.randint(100, 150)

    def move_cooldown(self):  # đếm ngược thời gian di chuyển
        if self.move_cool_down >= self.MOVE_TIME:
            self.move_cool_down = 0
        elif self.move_cool_down > 0:
            self.move_cool_down += 1

    def death(self):
        global Score
        if self.health <= 0:
            explosion_group.add(Explosion(self.rect.centerx, self.rect.centery, EXPLOSION))
            enemy_group.remove(self)
            Score += 1

    def update(self):
        self.move_cooldown()
        self.move()
        self.cooldown()
        self.shot()
        self.death()


# Bullet Class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, color, direction):
        super().__init__()
        self.direction = direction
        self.image = pygame.transform.rotate(TYPE_BULLET[color]["image"], direction + 90)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.vel = TYPE_BULLET[color]["vel"]

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
        global Score
        if not (0 < self.rect.x < WIDTH and 0 < self.rect.y < HEIGHT):
            if self in player_bullet_group:
                player_bullet_group.remove(self)
            else:
                enemy_bullet_group.remove(self)

        if self in enemy_bullet_group and pygame.sprite.spritecollide(self, player_group, False):
            explosion_group.add(Explosion(self.rect.centerx, self.rect.centery, SMALL_EXPLOSION))
            global LIVES, player
            if not player.has_barrier:
                explosion_group.add(Explosion(player.rect.centerx, player.rect.centery, EXPLOSION))
                if LIVES > 1:
                    player_group.remove(player)
                    player = Player(REBORN_X, REBORN_Y)
                    player_group.add(player)
                    player.open_barrier(45)
                    pygame.sprite.spritecollide(player, enemy_group, True)
                LIVES -= 1
            enemy_bullet_group.remove(self)

        if pygame.sprite.spritecollide(self, wall_group, True):
            explosion_group.add(Explosion(self.rect.centerx, self.rect.centery, SMALL_EXPLOSION))
            if self in player_bullet_group:
                player_bullet_group.remove(self)
            else:
                enemy_bullet_group.remove(self)

        if pygame.sprite.spritecollide(self, steel_wall_group, False):
            explosion_group.add(Explosion(self.rect.centerx, self.rect.centery, SMALL_EXPLOSION))
            if self in player_bullet_group:
                player_bullet_group.remove(self)
            else:
                enemy_bullet_group.remove(self)

        if pygame.sprite.spritecollide(self, enemy_group, False) and self in player_bullet_group:
            explosion_group.add(Explosion(self.rect.centerx, self.rect.centery, SMALL_EXPLOSION))

    def update(self):
        self.move()
        self.collide()


# Laser Class
class Laser(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, direction):
        super().__init__()
        self.laser_sheet = PLAYER_LASER.copy()

        for i in range(len(self.laser_sheet)):
            self.laser_sheet[i] = pygame.transform.rotate(PLAYER_LASER[i], direction + 90)

        self.current_image = 0
        self.image = self.laser_sheet[self.current_image]

        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

    def collide(self):
        global Score
        if pygame.sprite.spritecollide(self, enemy_group, True):
            Score += 1
        pygame.sprite.spritecollide(self, wall_group, True)
        pygame.sprite.spritecollide(self, steel_wall_group, True)

    def update(self):
        self.collide()
        self.current_image += 0.25
        if self.current_image >= len(self.laser_sheet):
            global LIVES, player
            player_laser_group.remove(self)
            explosion_group.add(Explosion(player.rect.centerx, player.rect.centery, EXPLOSION))
            player_group.empty()
            if LIVES > 1:
                player = Player(REBORN_X, REBORN_Y)
                player_group.add(player)
                pygame.sprite.spritecollide(player, enemy_group, True)
                player.open_barrier(45)
            LIVES -= 1
        else:
            self.image = self.laser_sheet[int(self.current_image)]


# Barrier Class
class Barrier(pygame.sprite.Sprite):
    global player

    def __init__(self, pos_x, pos_y, time):
        super().__init__()
        self.barrier_sheet = PLAYER_BARRIER

        self.current_images = 0
        self.image = self.barrier_sheet[self.current_images]

        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

        self.time = time
        player.has_barrier = True

    def move(self):
        self.rect.centerx = player.rect.centerx
        self.rect.centery = player.rect.centery

    def protect(self):
        pygame.sprite.spritecollide(self, enemy_bullet_group, True)

    def update(self):
        self.current_images += 0.5
        self.move()
        self.protect()
        if self.current_images >= self.time:
            player_barrier_group.empty()
            player.has_barrier = False
        else:
            self.image = self.barrier_sheet[int(self.current_images) % len(self.barrier_sheet)]


# Explosion Class
class Explosion(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, animation):
        super().__init__()
        self.explosion_sheet = animation

        self.current_images = 0
        self.image = self.explosion_sheet[self.current_images]

        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        if animation == EXPLOSION:
            explode_sound = pygame.mixer.Sound(os.path.join("sounds", "explode_sound.wav"))
            explode_sound.play()

    def update(self):
        self.current_images += 1
        if self.current_images >= len(self.explosion_sheet):
            explosion_group.remove(self)
        else:
            self.image = self.explosion_sheet[self.current_images]


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
player = Player(REBORN_X, REBORN_Y)
player_group = pygame.sprite.Group()
player_group.add(player)
player_bullet_group = pygame.sprite.Group()
player_laser_group = pygame.sprite.Group()
player_barrier_group = pygame.sprite.Group()

# Set Main House
hawk_group = pygame.sprite.Group()

# Set Wall
wall_group = pygame.sprite.Group()
# for i in range(30):
#     wall = Wall(WALL.get_width() * random.randint(1, 16),
#                 WALL.get_height() * random.randint(1, 12), WALL)
#     if check_over_lap(wall, [wall_group, player_group]):
#         wall_group.add(wall)

# Set Steel Wall
steel_wall_group = pygame.sprite.Group()
# for i in range(30):
#     wall = Wall(STEEL_WALL.get_width() * random.randint(1, 16),
#                 STEEL_WALL.get_height() * random.randint(1, 12), STEEL_WALL)
#     if check_over_lap(wall, [wall_group, steel_wall_group, player_group]):
#         steel_wall_group.add(wall)

# Set Grass
grass_group = pygame.sprite.Group()

# Draw Demo Level 1
draw_map()

# Set Enemy
enemy_group = pygame.sprite.Group()
color_random = ["red", "green", "gray", "blue"]
color_random.remove(PLAYER_COLOR)
for i in range(30):
    color_chose = random.choice(color_random)
    enemy = Enemy(TYPE_TANK[color_chose]["image"].get_width() * random.randint(1, 16),
                  TYPE_TANK[color_chose]["image"].get_height() * random.randint(1, 12),
                  color_chose)
    if check_over_lap(enemy, [wall_group, enemy_group, steel_wall_group, player_group]):
        enemy_group.add(enemy)
enemy_bullet_group = pygame.sprite.Group()

# Set Explosion
explosion_group = pygame.sprite.Group()

# Game run
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    Screen.blit(BG, (0, 0))

    grass_group.draw(Screen)
    hawk_group.draw(Screen)

    wall_group.draw(Screen)
    steel_wall_group.draw(Screen)

    player_laser_group.draw(Screen)
    player_laser_group.update()
    player_bullet_group.draw(Screen)
    player_bullet_group.update()
    player_group.draw(Screen)
    player_group.update()
    player_barrier_group.draw(Screen)
    player_barrier_group.update()

    enemy_group.draw(Screen)
    enemy_group.update()
    enemy_bullet_group.draw(Screen)
    enemy_bullet_group.update()

    explosion_group.draw(Screen)
    explosion_group.update()

    main_font = pygame.font.SysFont("comicsans", 30)
    lives_label = main_font.render(f"Lives: {LIVES}", True, (255, 255, 255))
    score_label = main_font.render(f"Scores: {Score}", True, (255, 255, 255))
    Screen.blit(lives_label, (10, 10))
    Screen.blit(score_label, (10, 40))

    clock.tick(60)
