from logger import log_state, log_event
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collides_with(shot) == True:
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()

        for drawables in drawable:
            drawables.draw(screen)


        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
