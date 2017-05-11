import sys, pygame, os
from pygame.locals import *
import math
import random
import time

class Target(pygame.sprite.Sprite):
	def __init__(self, gs, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.gs = gs
		self.image = pygame.transform.scale(pygame.image.load("like_button.png"), (50, 50))
		self.rect = self.image.get_rect()
		self.rect.topleft = x, y
		
	
	def tick(self):
		gs.screen.blit(self.image, self.rect)
		
class Fade(pygame.sprite.Sprite):
	def __init__(self, gs, center):
		pygame.sprite.Sprite.__init__(self)
		self.gs = gs
		size = 50, 50
		self.image = pygame.transform.scale(pygame.image.load("liked_button.png"), size)
		self.rect = self.image.get_rect()
		self.rect.center = center
		self.count = 10
		
	def tick(self):
		self.image.set_alpha(self.count)
		self.count -= 1
		if(self.count <= 0):
			self.kill()
		gs.screen.blit(self.image, self.rect)
		
		
class Smoke(pygame.sprite.Sprite):
	def __init__(self, gs, center):
		pygame.sprite.Sprite.__init__(self)
		self.gs = gs
		self.images = []
		size = 75, 75
		self.image = pygame.transform.scale(pygame.image.load("smoke_plume_0001.png"), size)
		self.images.append(pygame.transform.scale(pygame.image.load("smoke_plume_0002.png"), size))
		self.images.append(pygame.transform.scale(pygame.image.load("smoke_plume_0003.png"), size))
		self.images.append(pygame.transform.scale(pygame.image.load("smoke_plume_0004.png"), size))
		self.images.append(pygame.transform.scale(pygame.image.load("smoke_plume_0005.png"), size))
		self.images.append(pygame.transform.scale(pygame.image.load("smoke_plume_0006.png"), size))
		self.images.append(pygame.transform.scale(pygame.image.load("smoke_plume_0007.png"), size))
		self.images.append(pygame.transform.scale(pygame.image.load("smoke_plume_0008.png"), size))
		self.images.append(pygame.transform.scale(pygame.image.load("smoke_plume_0009.png"), size))
		self.images.append(pygame.transform.scale(pygame.image.load("smoke_plume_0010.png"), size))
		self.rect = self.image.get_rect()
		self.rect.center = center
		self.count = 0
		
	def tick(self):
		if(self.count > 7):
			self.kill()
		self.image = self.images[self.count]
		self.gs.screen.blit(self.image, self.rect)
		self.count += 1
		
		
		
	
		
		
class GameSpace:
	def main(self):
		pygame.init()
		self.size = self.width, self.height = 800, 600
		self.black = 0,0,0
		self.screen = pygame.display.set_mode(self.size)
		self.clickCount = 0
		self.fb = pygame.sprite.Group()
		self.smokes = pygame.sprite.Group()
		self.screen.fill(self.black)
		self.myfont = pygame.font.Font(None, 35)
		self.run(random.randint(30, 120)/100)
		
		
		
	def run(self, ms):
		start = time.time()
		placed = 0
		self.clock = pygame.time.Clock()
		while 1:
			self.clock.tick(60)
			if(ms < time.time() - start and placed == 0):
				self.fb.add(Target(self, random.randint(0, 750), random.randint(0, 550)))
				placed = 1
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					for targ in self.fb:
						if targ.rect.collidepoint(event.pos):
							self.clickCount += 1
							#self.smokes.add(Smoke(self, targ.rect.center))
							self.smokes.add(Fade(self, targ.rect.center))
							targ.kill()
							#print ("Total clicked: ", self.clickCount)
							placed = 0
							start = time.time()
							ms = random.randint(30, 120)/100
				if event.type == pygame.KEYDOWN:
					if chr(event.key) == 'q':
						sys.exit()
			for targ in self.fb:
				targ.tick()
			for smoke in self.smokes:
				smoke.tick()
			label = self.myfont.render("Hits: {}".format(self.clickCount), 1, (255, 255, 255))
			self.screen.blit(label, (350, 100))
			pygame.display.flip()
			self.screen.fill(self.black)		
		
if __name__=='__main__':
	gs = GameSpace()
	gs.main()
	