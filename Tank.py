import pygame
import os
import random
import time
pygame.font.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tank-shooting")

#Load image
TANK_RED = pygame.image.load(os.path.join("images", "tank_red.png"))
TANK_DARK = pygame.image.load(os.path.join("images", "tank_dark.png"))
TANK_GREEN = pygame.image.load(os.path.join("images", "tank_green.png"))
TANK_SAND = pygame.image.load(os.path.join("images", "tank_sand.png"))

#Player tank
TANK_BLUE = pygame.image.load(os.path.join("images", "tank_blue.png"))

#Bullets
RED_BULLET = pygame.image.load(os.path.join("images", "bulletred2.png"))
DARK_BULLET = pygame.image.load(os.path.join("images", "bulletdark2.png"))
GREEN_BULLET = pygame.image.load(os.path.join("images", "bulletgreen2.png"))
SAND_BULLET = pygame.image.load(os.path.join("images", "bulletsand2.png"))
BLUE_BULLET = pygame.image.load(os.path.join("images", "bulletblue2.png"))

#Background
BG = pygame.image.load(os.path.join("images", "grass.png"))

class Bullet:
	def __init__(self, x, y, img):
		self.x = x
		self.y = y
		self.img = img
		self.mask = pygame.mask.from_surface(self.img)

	def draw(self, window):
		window.blit(self.img, (self.x, self.y))

	def move(self, vel, last_direction):
		if last_direction == "up":
			self.y -= vel
		elif last_direction == "down":
			self.y += vel
		elif last_direction == "right":
			self.x += vel
		elif last_direction == "left":
			self.x -= vel

	def off_screen(self, height): #xoa dan sau khi bay ra khoi man hinh game
		return not(self.y <= height and self.y >= 0)

	def collision(self, obj): # tao va cham cho dan
		return collide(self, obj)

class Tank:
	COOLDOWN = 30

	def __init__(self, x, y, health = 100):
		self.x = x
		self.y = y
		self.health = health
		self.tank_img = None
		self.bullet_img = None
		self.bullets = []
		self.cool_down_counter = 0

	def draw(self, window):
		window.blit(self.tank_img, (self.x, self.y))
		for bullet in self.bullets:
			bullet.draw(window)

	def move_bullets(self, vel, obj, last_direction): # chuyen dong va va cham cua dan
		self.cooldown()
		for bullet in self.bullets:
			bullet.move(vel, last_direction)
			if bullet.off_screen(HEIGHT):
				self.bullets.remove(bullet)
			elif bullet.collision(obj):
				obj.health -= 10
				self.bullets.remove(bullet)

	def cooldown(self): #kiem soat cd tranh spam dan
		if self.cool_down_counter >= self.COOLDOWN:
			self.cool_down_counter = 0
		elif self.cool_down_counter > 0:
			self.cool_down_counter += 1

	def shoot(self):
		if self.cool_down_counter == 0:
			bullet = Bullet(self.x, self.y, self.bullet_img)
			self.bullets.append(bullet)
			self.cool_down_counter = 1

	def get_width(self):
		return self.tank_img.get_width()

	def get_height(self):
		return self.tank_img.get_height()

class Player(Tank):
	def __init__(self, x, y, health = 100):
		super().__init__(x, y, health)
		self.tank_img = TANK_BLUE
		self.bullet_img = BLUE_BULLET
		self.mask = pygame.mask.from_surface(self.tank_img)
		self.max_health = health

	def move_bullets(self, vel, objs, last_direction):
		self.cooldown()
		for bullet in self.bullets:
			bullet.move(vel, last_direction)
			if bullet.off_screen(HEIGHT):
				self.bullets.remove(bullet)
			else:
				for obj in objs:
					if bullet.collision(obj):
						objs.remove(obj)
						if bullet in self.bullets:
							self.bullets.remove(bullet)

	def draw(self, window, last_direction):
		super().draw(window)
		if (last_direction == "right"):
			self.tank_img = pygame.transform.rotate(TANK_BLUE, -90)
		elif (last_direction == "left"):
			self.tank_img = pygame.transform.rotate(TANK_BLUE, 90)
		elif (last_direction == "up"):
			self.tank_img = pygame.transform.rotate(TANK_BLUE, 0)
		elif (last_direction == "down"):
			self.tank_img = pygame.transform.rotate(TANK_BLUE, 180)

class Enemy(Tank):
	COLOR_MAP = {
		"red" : (TANK_RED, RED_BULLET),
		"dark" : (TANK_DARK, DARK_BULLET),
		"green" : (TANK_GREEN, GREEN_BULLET),
		"sand" : (TANK_SAND, SAND_BULLET)
	}

	def __init__(self, x, y, color, health = 100):
		super().__init__(x, y, health)
		self.tank_img, self.bullet_img = self.COLOR_MAP[color]
		self.mask = pygame.mask.from_surface(self.tank_img)

	def move(self, vel):
		self.y += vel

def collide(obj1, obj2): #xu li va cham
	offset_x = obj2.x - obj1.x
	offset_y = obj2.y - obj1.y
	return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

def main():
	run = True
	FPS = 60
	level = 0
	lives = 5
	player_vel = 3
	bullet_vel = 3
	last_direction = "up"

	main_font = pygame.font.SysFont("comicsans", 50)
	lost_font = pygame.font.SysFont("comicsans", 50)

	enemies = []
	wave_length = 5
	enemy_vel = 1

	player = Player(400, 550)

	clock = pygame.time.Clock()

	lost = False
	lost_count = 0

	def redraw_window():
		WIN.blit(BG, (0,0))
		#draw text
		lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
		WIN.blit(lives_label, (10, 10))

		for enemy in enemies:
			enemy.draw(WIN)

		player.draw(WIN, last_direction)

		if lost:
			lost_label = lost_font.render("You lost!!", 1, (255, 255, 255))
			WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

		pygame.display.update()

	while run:
		clock.tick(FPS)
		redraw_window()

		if player.health <= 0:
			lost = True
			lost_count += 1

		if lost:
			if lost_count > FPS * 3:
				run = False
			else:
				continue
			

		if len(enemies) == 0:
			level += 1
			wave_length += 5
			for i in range(wave_length):
				enemy = Enemy(random.randrange(100, WIDTH-100, 50), 0, random.choice(["red", "dark", "green", "sand"]))
				enemies.append(enemy)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT] and player.x - player_vel > 0:
			player.x -= player_vel
			last_direction = "left"
		elif keys[pygame.K_RIGHT] and player.x + player_vel + player.get_width() < WIDTH:
			player.x += player_vel
			last_direction = "right"
		elif keys[pygame.K_UP] and player.y - player_vel > 0:
			player.y -= player_vel
			last_direction = "up"
		elif keys[pygame.K_DOWN] and player.y + player_vel + player.get_height() < HEIGHT:
			player.y += player_vel
			last_direction = "down"
		if keys[pygame.K_SPACE]:
			player.shoot()

		for enemy in enemies[:]:
			enemy.move(enemy_vel)
			enemy.move_bullets(bullet_vel, player, last_direction)

		player.move_bullets(bullet_vel, enemies, last_direction)

main()
