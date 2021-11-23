import os
import random
import sys

import pygame

# General Setup
pygame.font.init()
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Tank Shooting")

# Game Screen
SCREEN_WIDTH = 850
SCREEN_HEIGHT = 650
Screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
start_time = pygame.time.get_ticks()
# Text on Screen
LIVES = 3
Score = 0

######################################################### Load Images ########################################
# Load Background Images
BG = pygame.image.load(os.path.join("images", "back_ground.png"))

# Load Wall + GRASS + MAIN HOUSE
WALL = pygame.image.load(os.path.join("images", "wall.png"))
STEEL_WALL = pygame.image.load(os.path.join("images", "steel_wall.png"))
GRASS = pygame.image.load(os.path.join("images", "grass1.png"))
BASE = pygame.image.load(os.path.join("images", "vietnam.png"))

#  Load Tank Images
TANK_RED = pygame.image.load(os.path.join("images", "tank_red.png")).convert_alpha(Screen)
TANK_GREEN = pygame.image.load(os.path.join("images", "tank_green.png")).convert_alpha(Screen)
TANK_BLUE = pygame.image.load(os.path.join("images", "tank_blue.png")).convert_alpha(Screen)
TANK_GRAY = pygame.image.load(os.path.join("images", "tank_gray.png")).convert_alpha(Screen)

# Load Bullet Images
RED_BULLET = pygame.image.load(os.path.join("images", "bullet_red.png"))
GRAY_BULLET = pygame.image.load(os.path.join("images", "bullet_gray.png"))
GREEN_BULLET = pygame.image.load(os.path.join("images", "bullet_green.png"))
BLUE_BULLET = pygame.image.load(os.path.join("images", "bullet_blue.png"))


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
    SMALL_EXPLOSION.append(pygame.image.load(os.path.join("images", "bullet_collide (1).png")))
    SMALL_EXPLOSION.append(pygame.image.load(os.path.join("images", "bullet_collide (2).png")))
    SMALL_EXPLOSION.append(pygame.image.load(os.path.join("images", "bullet_collide (3).png")))
    SMALL_EXPLOSION.append(pygame.image.load(os.path.join("images", "bullet_collide (4).png")))
    SMALL_EXPLOSION.append(pygame.image.load(os.path.join("images", "bullet_collide (5).png")))
    SMALL_EXPLOSION.append(pygame.image.load(os.path.join("images", "bullet_collide (6).png")))
    SMALL_EXPLOSION.append(pygame.image.load(os.path.join("images", "bullet_collide (7).png")))
    SMALL_EXPLOSION.append(pygame.image.load(os.path.join("images", "bullet_collide (8).png")))

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

    # Load Spam
    SPAM.append(pygame.image.load(os.path.join("images", "spam (1).png")).convert_alpha(Screen))
    SPAM.append(pygame.image.load(os.path.join("images", "spam (2).png")).convert_alpha(Screen))
    SPAM.append(pygame.image.load(os.path.join("images", "spam (3).png")).convert_alpha(Screen))
    SPAM.append(pygame.image.load(os.path.join("images", "spam (4).png")).convert_alpha(Screen))
    SPAM.append(pygame.image.load(os.path.join("images", "spam (5).png")).convert_alpha(Screen))
    SPAM.append(pygame.image.load(os.path.join("images", "spam (6).png")).convert_alpha(Screen))
    SPAM.append(pygame.image.load(os.path.join("images", "spam (7).png")).convert_alpha(Screen))
    SPAM.append(pygame.image.load(os.path.join("images", "spam (8).png")).convert_alpha(Screen))
    SPAM.append(pygame.image.load(os.path.join("images", "spam (9).png")).convert_alpha(Screen))
    SPAM.append(pygame.image.load(os.path.join("images", "spam (10).png")).convert_alpha(Screen))
    SPAM.append(pygame.image.load(os.path.join("images", "spam (11).png")).convert_alpha(Screen))
    SPAM.append(pygame.image.load(os.path.join("images", "spam (12).png")).convert_alpha(Screen))
    SPAM.append(pygame.image.load(os.path.join("images", "spam (13).png")).convert_alpha(Screen))
    SPAM.append(pygame.image.load(os.path.join("images", "spam (14).png")).convert_alpha(Screen))
    SPAM.append(pygame.image.load(os.path.join("images", "spam (15).png")).convert_alpha(Screen))


######################################################### Tuy Chỉnh ########################################

# Ability Animation
PLAYER_LASER = []
PLAYER_BARRIER = []
# Explosion
EXPLOSION = []
SMALL_EXPLOSION = []
# Spam Animation
SPAM = []

#  Bullet Type
TYPE_BULLET = {}
#  Tank Type
TYPE_TANK = {}


# Chỉnh thuộc tính của đạn
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


# Chỉnh thuộc tính xe tank
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


# Thêm ảnh vào sheet
add_animation_sheet()
set_bullet()
set_Tank_stats()

######################################## Player ########################################################


# Chose Player Color + Reborn Point
PLAYER_COLOR = "blue"
REBORN_X = SCREEN_WIDTH / 2 - WALL.get_width() * 2
REBORN_Y = SCREEN_HEIGHT - WALL.get_height()

# Enemy Color + Spam Time
enemy_color = ["red", "green", "gray", "blue"]
enemy_color.remove(PLAYER_COLOR)
spam_enemy_time = 150  # Thời gian xuất hiện đợt tank địch mới


# ######################################## Map Setup #################################################
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
                wall = Building(WALL.get_width() * col + WALL.get_width() / 2,
                                WALL.get_height() * row + WALL.get_width() / 2, WALL)
                wall_group.add(wall)
            elif map[row][col] == '@':
                stone = Building(STEEL_WALL.get_width() * col + STEEL_WALL.get_width() / 2,
                                 STEEL_WALL.get_height() * row + STEEL_WALL.get_width() / 2, STEEL_WALL)
                steel_wall_group.add(stone)
            elif map[row][col] == 'G':
                grass = Building(GRASS.get_width() * col + WALL.get_width() / 2,
                                 GRASS.get_height() * row + WALL.get_width() / 2, GRASS)
                grass_group.add(grass)
            elif map[row][col] == 'H':
                base = Building(BASE.get_width() * col + WALL.get_width() / 2,
                                BASE.get_height() * row + WALL.get_width() / 2, BASE)
                base_group.add(base)

    # print(len(map[0][1]))
    # for row in range(13):  # 850/50=17
    #     for col in range(len(map[row])):
    #         print(map[row][col], sep='', end='')
    #     print()


######################################## Class organize ##########################################


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
        if not (0 < self.rect.x < SCREEN_WIDTH - self.TANK_WIDTH and 0 < self.rect.y < SCREEN_HEIGHT - self.TANK_HEIGHT):
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
        if self.collide([wall_group, steel_wall_group, enemy_group, base_group]):
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

    def open_barrier(self, time=60):
        barrier = Barrier(time)
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
        if not (0 < self.rect.x < SCREEN_WIDTH - self.TANK_WIDTH and 0 < self.rect.y < SCREEN_HEIGHT - self.TANK_HEIGHT):
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
        if self.collide([wall_group, steel_wall_group, player_group, base_group]):
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
        if not (0 < self.rect.x < SCREEN_WIDTH and 0 < self.rect.y < SCREEN_HEIGHT):
            if self in player_bullet_group:
                player_bullet_group.remove(self)
            else:
                enemy_bullet_group.remove(self)

        if self in enemy_bullet_group and pygame.sprite.spritecollide(self, player_group, False):
            explosion_group.add(Explosion(self.rect.centerx, self.rect.centery, SMALL_EXPLOSION))
            global LIVES, player
            if not player.has_barrier:
                explosion_group.add(Explosion(player.rect.centerx, player.rect.centery, EXPLOSION))
                player_group.empty()
                if LIVES > 1:
                    spam_group.add(Spam(REBORN_X, REBORN_Y, "player"))
                    pygame.sprite.spritecollide(player, enemy_group, True)
                LIVES -= 1
            enemy_bullet_group.remove(self)

        buildings = (wall_group, base_group)
        for building in buildings:
            if pygame.sprite.spritecollide(self, building, True):
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
            LIVES -= 1
            spam_group.add(Spam(REBORN_X, REBORN_Y, "player"))
        else:
            self.image = self.laser_sheet[int(self.current_image)]


# Barrier Class
class Barrier(pygame.sprite.Sprite):
    global player

    def __init__(self, time):
        super().__init__()
        self.barrier_sheet = PLAYER_BARRIER

        self.current_images = 0
        self.image = self.barrier_sheet[self.current_images]

        self.rect = self.image.get_rect()
        self.rect.center = [player.rect.x, player.rect.y]

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


# Spam Class - Class hiệu ứng lúc tank xuất hiện
class Spam(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, spam_tank="enemy", time=200):
        super().__init__()
        self.spam_sheet = SPAM
        self.spam_tank = spam_tank
        self.spam_time = time  # Sprites Frame
        self.current_images = 0
        self.image = self.spam_sheet[self.current_images]

        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

    def update(self):
        self.current_images += 1
        if self.current_images >= self.spam_time:
            global LIVES, Score, player, enemy_color
            if self.spam_tank == "enemy":
                color_random = random.choice(enemy_color)
                enemy_random = Enemy(self.rect.centerx, self.rect.centery, color_random)
                if pygame.sprite.spritecollide(enemy_random, enemy_group, True):
                    explosion_group.add(Explosion(self.rect.centerx, self.rect.centery, EXPLOSION))
                if pygame.sprite.spritecollide(enemy_random, player_group, True):
                    explosion_group.add(Explosion(self.rect.centerx, self.rect.centery, EXPLOSION))
                    LIVES -= 1
                    if LIVES > 0:
                        spam_group.add(Spam(REBORN_X, REBORN_Y, "player"))
                enemy_group.add(enemy_random)
            else:

                if LIVES > 0:
                    player = Player(self.rect.centerx, self.rect.centery)
                    player_group.add(player)
                    player.open_barrier()
                    if pygame.sprite.spritecollide(player, enemy_group, True):
                        explosion_group.add(Explosion(self.rect.centerx, self.rect.centery, EXPLOSION))
                        Score += 1

            spam_group.remove(self)
        else:
            self.image = self.spam_sheet[self.current_images % len(self.spam_sheet)]


# Building Class
class Building(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]


# Button Class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action


######################################## Group + Level organize ##########################################

# Generate Rule - Check Overlap
def check_over_lap(object, groups):
    for group in groups:
        if pygame.sprite.spritecollide(object, group, False):
            return False
    return True


# Group
player_group = pygame.sprite.Group()
player_bullet_group = pygame.sprite.Group()
player_laser_group = pygame.sprite.Group()
player_barrier_group = pygame.sprite.Group()

enemy_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()

base_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
steel_wall_group = pygame.sprite.Group()
grass_group = pygame.sprite.Group()

explosion_group = pygame.sprite.Group()
spam_group = pygame.sprite.Group()

# Spam Player
spam_group.add(Spam(REBORN_X, REBORN_Y, "player", 100))

# Draw Wall
# for i in range(30):
#     wall = Wall(WALL.get_width() * random.randint(1, 16),
#                 WALL.get_height() * random.randint(1, 12), WALL)
#     if check_over_lap(wall, [wall_group, player_group]):
#         wall_group.add(wall)

# Draw Steel Wall
# for i in range(30):
#     wall = Wall(STEEL_WALL.get_width() * random.randint(1, 16),
#                 STEEL_WALL.get_height() * random.randint(1, 12), STEEL_WALL)
#     if check_over_lap(wall, [wall_group, steel_wall_group, player_group]):
#         steel_wall_group.add(wall)


# Draw Demo Level 1
draw_map()


# Spam Enemy
def spam_enemy():
    for i in range(random.randint(1, 5)):
        spam = Spam(WALL.get_width() * random.randint(1, 16), WALL.get_height() * random.randint(1, 12))
        if check_over_lap(spam, [wall_group, enemy_group, steel_wall_group, player_group, base_group, spam_group]):
            spam_group.add(spam)
        else:
            i -= 1

 ##################################### GUI ########################################

# Game over

def Game_over():
    if LIVES <= 0 or len(base_group) == 0:
        return True


# Game run
def main_rank():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # if Game_over():
        #     break

        pygame.display.flip()
        Screen.blit(BG, (0, 0))

        grass_group.draw(Screen)
        base_group.draw(Screen)
        base_group.update(Screen)

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

        spam_group.draw(Screen)
        spam_group.update()

        if (start_time - pygame.time.get_ticks()) % spam_enemy_time == 0:
            spam_enemy()

        main_font = pygame.font.SysFont("comicsans", 30)
        lives_label = main_font.render(f"Lives: {LIVES}", True, (255, 255, 255))
        score_label = main_font.render(f"Scores: {Score}", True, (255, 255, 255))
        Screen.blit(lives_label, (10, 10))
        Screen.blit(score_label, (10, 40))

        clock.tick(60)


# -------------

def main_level():
    pass

def screen_chose():


    level_img = pygame.image.load('images/level_img.png').convert_alpha()
    rank_img = pygame.image.load('images/rank_img.png').convert_alpha()

    # tạo button
    button_level = Button(100, 200, level_img, 0.8)
    button_rank = Button(500, 200, rank_img, 0.8)
    run = True

    while run:
        screen.fill((0, 0, 0))

        if button_level.draw(screen):
            main_level()
        if button_rank.draw(screen):
            main_rank()

        # if close
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()


# màn hình tính điểm chơi rank
def screen_rank():
    pass



def screen_lose():

    image_lose = pygame.image.load('images/play.png').convert_alpha()


def screen_win():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Tank Shooting')
    image_win = pygame.image.load('images/image_win.png.png').convert_alpha()


# ------------

SCREEN_WIDTH = 850
SCREEN_HEIGHT = 650

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tank-shooting')


start_img = pygame.image.load('images/play.png').convert_alpha()
exit_img = pygame.image.load('images/exit.png').convert_alpha()

# tạo button
size_button = 0.8
start_button = Button(100, 200, start_img, size_button)
exit_button = Button(550, 200, exit_img, size_button)

# game !stop
run = True

while run:
    pygame.display.flip()
    opening_background = pygame.image.load('images/opening_background.png')
    screen.blit(opening_background, (0, 0))
    caption = pygame.image.load('images/game_name.png')
    screen.blit(caption, (175,50))
    if start_button.draw(screen):
        print("Play")
        screen_chose()
        run = False
    if exit_button.draw(screen):
        run = False
        pygame.quit()
        sys.exit()


    # if close
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
# -------------
