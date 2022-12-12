from header import *

class LifeBar:
	def __init__(self, pokeId, maxHP, pos, speed=2, height=15, width=130):
		self.pokeId = pokeId
		self.current_health = 0
		self.target_health = maxHP
		self.max_health = maxHP
		self.health_bar_length = width
		self.health_bar_height = height
		self.health_bar_border = 2
		self.posX, self.posY = pos
		self.health_ratio = self.max_health / self.health_bar_length
		self.health_change_speed = speed

	def get_damage(self,amount):
		if self.target_health > 0:
			self.target_health -= amount
		if self.target_health < 0:
			self.target_health = 0

	def get_health(self,amount):
		if self.target_health < self.max_health:
			self.target_health += amount
		if self.target_health > self.max_health:
			self.target_health = self.max_health

	def update(self, screen):
		self.advanced_health(screen)

	def advanced_health(self, screen):
		transition_width = 0
		transition_color = (255,0,0)

		if self.current_health < self.target_health:
			self.current_health += self.health_change_speed
			transition_width = int((self.target_health - self.current_health) / self.health_ratio)
			transition_color = (0,255,0)

		if self.current_health > self.target_health:
			self.current_health -= self.health_change_speed 
			transition_width = int((self.target_health - self.current_health) / self.health_ratio)
			transition_color = (255,255,0)

		health_bar_width = int(self.current_health / self.health_ratio)
		health_bar = pygame.Rect(self.posX,self.posY,
								health_bar_width,
								self.health_bar_height)

		transition_bar = pygame.Rect(health_bar.right,self.posY,
								transition_width,
								self.health_bar_height)
		
		pygame.draw.rect(screen,(255,0,0),health_bar)
		pygame.draw.rect(screen,transition_color,transition_bar)	
		
		pygame.draw.rect(screen,(255,255,255),
							(self.posX,self.posY,
								self.health_bar_length,
								self.health_bar_height),
							self.health_bar_border)	