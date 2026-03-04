import pygame
import constants
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
import sys
from shot import Shot




def main():
    pygame.init()

    clock = pygame.time.Clock()

    dt = 0

    updatable = pygame.sprite.Group()

    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()

    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)

    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    player= Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)

    asteroidfield = AsteroidField()


    
    while(1):

        dt = clock.tick(60) / 1000

        

        points = player.triangle()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        

        screen.fill("black")

        for obj in updatable:
            obj.update(dt)
            

        for ast in asteroids:
            if ast.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            
            for shot in shots:
                if ast.collides_with(shot):
                    log_event("asteroid_shot")
                    ast.split()
                    shot.kill()






        for obj in drawable:
            obj.draw(screen)



        pygame.display.flip()
        log_state()

        
        

        

        

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
