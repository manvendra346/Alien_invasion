import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.color = self.settings.bullet_color

        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        """moving the bullet"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
