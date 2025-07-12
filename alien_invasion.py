import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w,self.settings.screen_h)
            )

        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file) #This is to display the background
        self.bg = pygame.transform.scale(self.bg, 
            (self.settings.screen_w, self.settings.screen_h)
            )

        self.running = True
        self.clock = pygame.time.Clock()
        #Initial Game loop ^^^

        self.ship = Ship(self)


    def run_game(self): 
        # Game Loop goes here
        while self.running:
            self._check_events()

            self._update_screen()      
            self.clock.tick(self.settings.FPS)

    def _update_screen(self):
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #This is how to exit out the game
                self.running = False
                pygame.quit()
                sys.exit()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()