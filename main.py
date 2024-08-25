# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import *
from shot import *

def main():
	pygame.init()
	
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Asteroid.containers = (updatable, drawable, asteroids)
	AsteroidField.containers = (updatable,)
	field = AsteroidField()

	Shot.containers = (updatable, drawable, shots)

	Player.containers = (updatable, drawable)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	
	
	#print("Starting asteroids!")
	#print(f"Screen width: {SCREEN_WIDTH}")
	#print(f"Screen height: {SCREEN_HEIGHT}")

	clock = pygame.time.Clock()
	dt = 0

	

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		
		for item in updatable:
			item.update(dt)

		for item in asteroids:
			if item.collision(player):
				print("Game over!")
				sys.exit()
			
			for bullet in shots:
				if item.collision(bullet):
					bullet.kill()
					item.split()
					#print("SHOT")
		

		for item in drawable:
			item.draw(screen)


		pygame.display.flip()
		
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()
