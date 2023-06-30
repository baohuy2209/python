import sys


import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """Overall class to managegame assets and behaviour ."""
    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien_Invasion")

        self.ship = Ship(self)
        self.bullet = pygame.sprite.Group()

    def rungame(self):
        """Start the main loop for the game ."""
        while True:

            # Watch for the keyboard and mouse events
            self._check_events()
            self.ship.update()
            self.bullet.update()
            for bullet in self.bullet.copy():
                if bullet.rect.bottom <= 0:
                    self.bullet.remove(bullet)
            self._update_screen()

    def _check_events(self):
        """Respond to keypress and mouse event"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
                if event.key == pygame.K_SPACE:
                    self._fire_bullet()
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullet.add(new_bullet)

    def _check_keydown_event(self, event):
        """ Respond to key release """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        if event.key == pygame.K_UP:
            self.ship.moving_up = True

    def _check_keyup_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullet.sprites():
            bullet.draw()
        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.rungame()