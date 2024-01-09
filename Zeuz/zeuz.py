import pygame, random
from random import randint

WIDTH = 1200
HEIGHT = 700
BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = (0, 255, 0)
RED = (255,0,0)
BLUE = (0,0,255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zeuz")
clock = pygame.time.Clock()

def draw_text1(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, WHITE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_text2(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, BLACK)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_hp_bar(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, GREEN, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

def draw_mana_bar(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BLUE, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

class Player1(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/zuus.png").convert(),(40,65))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centerx = 50
		self.rect.centery = HEIGHT * 1//3
		self.speed_x = 0
		self.hp = 100
		self.mana = 100
		

	def update(self):
		self.hp += 1/50
		self.mana += 1/50
		if self.mana < 0:
			self.mana = 0
		if self.mana > 100:
			self.mana = 100
		if self.hp < 0:
			self.hp = 0
		if self.hp > 100:
			self.hp = 100
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_a]:
			self.speed_x = -5
		if keystate[pygame.K_d]:
			self.speed_x = 5
		self.rect.x += self.speed_x
		if keystate[pygame.K_w]:
			self.speed_y = -5
		if keystate[pygame.K_s]:
			self.speed_y = 5
		self.rect.y += self.speed_y
		if self.rect.right > WIDTH + self.rect.x:
			self.rect.right = WIDTH + self.rect.x
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 10:
			self.rect.top = 10
		if self.rect.bottom > 700:
			self.rect.bottom = 700

class Player2(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/zuus.png").convert(),(40,65))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centerx = 50
		self.rect.centery = HEIGHT * 2//3
		self.speed_x = 0
		self.hp = 100
		self.mana = 100
		

	def update(self):
		self.hp += 1/50
		self.mana += 1/50
		if self.mana < 0:
			self.mana = 0
		if self.mana > 100:
			self.mana = 100
		if self.hp < 0:
			self.hp = 0
		if self.hp > 100:
			self.hp = 100
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speed_x = -5
		if keystate[pygame.K_RIGHT]:
			self.speed_x = 5
		self.rect.x += self.speed_x
		if keystate[pygame.K_UP]:
			self.speed_y = -5
		if keystate[pygame.K_DOWN]:
			self.speed_y = 5
		self.rect.y += self.speed_y
		
		if self.rect.right > WIDTH + self.rect.x:
			self.rect.right = WIDTH + self.rect.x
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 10:
			self.rect.top = 10
		if self.rect.bottom > 700:
			self.rect.bottom = 700

class Mine1(pygame.sprite.Sprite):
	
	def __init__(self):
		super().__init__()
		
		self.image = pygame.transform.scale(pygame.image.load("img/mine11.png").convert(),(30,30))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(100, WIDTH-100)
		self.ngo_list = [110, 240, 370, 500]
		self.rect.y = random.randrange(10, HEIGHT-50)
		
    
	def update(self):
		pass

class Mine2(pygame.sprite.Sprite):
	
	def __init__(self):
		super().__init__()
		
		self.image = pygame.transform.scale(pygame.image.load("img/mine2.png").convert(),(30,30))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(100, WIDTH-100)
		self.ngo_list = [110, 240, 370, 500]
		self.rect.y = random.randrange(10 , HEIGHT-50)
		
    
	def update(self):
		pass


def show_go_screen():
	
	screen.fill(BLACK)#(background, [0,0])
	draw_text1(screen, "Mines", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "llega a la meta", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)
	#draw_text(screen, "Created by: Francisco Carvajal", 10,  60, 625)
	
	
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

background = pygame.image.load("img/fond.png").convert()

game_over = True
running = True
while running:
	if game_over:

		show_go_screen()
		screen.blit(background,(0,0))
		game_over = False
		
		all_sprites = pygame.sprite.Group()
		mine1_list = pygame.sprite.Group()
		mine2_list = pygame.sprite.Group()
		player1 = Player1()
		all_sprites.add(player1)
		player2 = Player2()
		all_sprites.add(player2)

		for i in range(100):
			mine1 = Mine1()
			all_sprites.add(mine1)
			mine1_list.add(mine1)
		
		for i in range(15):
			mine2 = Mine2()
			all_sprites.add(mine2)
			mine2_list.add(mine2)
		all_sprites.add(player1, player2)
		
		
		score = 0
		


	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		

	if player1.hp == 0:
		player1.rect.centerx = 50
		player1.rect.centery = HEIGHT * 1/3
		player1.hp = 100
	if player2.hp == 0:
		player2.rect.centerx = 50
		player2.rect.centery = HEIGHT * 2/3
		player2.hp = 100
	if player1.rect.centerx > WIDTH:
		game_over = True
	if player2.rect.centerx > WIDTH:
		game_over = True
	all_sprites.update()

	# Checar colisiones - jugador1 - mines1
	hits = pygame.sprite.spritecollide(player1, mine1_list, True)
	for hit in hits:
		
		player1.hp -= 40
		
	# Checar colisiones - jugador2 - mines1
	hits = pygame.sprite.spritecollide(player2, mine1_list, True)
	for hit in hits:
		
		player2.hp -= 40	

	# Checar colisiones - jugador1 - mines2
	hits = pygame.sprite.spritecollide(player1, mine2_list, True)
	for hit in hits:
		
		player1.hp -= 0
		
	# Checar colisiones - jugador2 - mines2
	hits = pygame.sprite.spritecollide(player2, mine2_list, True)
	for hit in hits:
		
		player2.hp -= 0	

	screen.blit(background, [0, 0])

	all_sprites.draw(screen)

	#Marcador
	
	#draw_text(screen, str(player.score), 25, WIDTH // 2, 10)
	
	# Escudo.
	draw_hp_bar(screen, 5, 5, player1.hp)
	draw_text2(screen, str(int(player1.hp)) + "/100", 10, 50, 6)
	draw_hp_bar(screen, 600, 5, player2.hp)
	draw_text2(screen, str(int(player2.hp))+ "/100", 10, 650, 6)
	draw_mana_bar(screen, 5, 15, player1.mana)
	draw_text1(screen, str(int(player1.mana))+ "/100", 10, 50, 16)
	draw_mana_bar(screen, 600, 15, player2.mana)
	draw_text1(screen, str(int(player2.mana))+ "/100", 10, 650, 16)

	pygame.display.flip()