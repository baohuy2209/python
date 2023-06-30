import pygame


class Ship:
    """A class to manage the ship """
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position. """
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('th.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Start a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """ Update the ship position based on the movement flag """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0 :
            self.rect.x -= self.settings.ship_speed
        if self.moving_up:
            self.rect.y -= 1
        if self.moving_down:
            self.rect.y += 1

        # Update rect object from self.x
        #self.rect.x = self.x
        #self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location """
        self.screen.blit(self.image,self.rect)