import pygame.font
from pygame.sprite import Group
from ship import Ship

class ScoreBoard:
     def __init__(self,ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.stats = ai_game.stats
        self.settings = ai_game.settings

        self.text_color = (173,176,181)
        self.font = pygame.font.SysFont(None, 48)
        self.sh_font = pygame.font.SysFont(None, 30)

        self.prep_score()
        self.prep_ships()

     def prep_score(self):
        rounded_score = round(self.stats.score,-1)
        score = "{:,}".format(rounded_score)
        self.score_img = self.font.render(score,True,self.text_color)
        self.score_img_rect = self.score_img.get_rect()
        self.score_img_rect.right = self.screen_rect.right -20
        self.score_img_rect.top = 20

        rounded_high_score = round(self.stats.high_score,-1)
        high_score = "{:,}".format(rounded_high_score)
        self.hs_img = self.sh_font.render(high_score,True,(70,70,70))
        self.hs_rect = self.hs_img.get_rect()
        self.hs_rect.right = self.screen_rect.right -20
        self.hs_rect.top = 75

     def show_score(self):
        self.screen.blit(self.score_img,self.score_img_rect)
        self.screen.blit(self.hs_img,self.hs_rect)
        self.ships.draw(self.screen)

     def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.ai_game.stats.ships_left):
          ship = Ship(self.ai_game)
          ship.rect.x = 10 +ship_number*ship.rect.width*1.2
          ship.rect.y = 10  
          self.ships.add(ship)

