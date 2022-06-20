import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from aliens import Alien
from button import Button
from time import sleep
from game_stats import GameStats

class AlienInvasion :
    def __init__(self):
        pygame.init() #necessary settings for for auto initialization
        #background and screen
        self.bg = pygame.image.load("images/background_2.jpg")
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.screen_height = self.screen.get_rect().height#full screena nd getting widt and height
        self.screen_width = self.screen.get_rect().width
        self.screen_rect = self.screen.get_rect()
        #setting and stats
        self.settings = Settings()
        self.stats = GameStats(self)
        self.play_button = Button(self, "Play")
        #ship and bullet
        self.ship = Ship(self)  
        self.bullets = pygame.sprite.Group()
        #alien fleet
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        pygame.display.set_caption("ALIEN INVASION")
    
    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullet()
                self._update_aliens()
            self._update_screen() 

    def _check_fleet_edge(self):
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self._change_fleet_direction() 
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        """update whole fleet"""
        self._check_fleet_edge()             
        self.aliens.update() 
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_fleet_bottom()

    def _check_fleet_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.screen_rect.bottom:
                self._ship_hit()
                break

    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.bullets.empty()
            self.aliens.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
    
    def _update_bullet(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
        self._check_bullet_alien_collison() 

    def _check_bullet_alien_collison(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_mouse_play_click(mouse_pos)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q :
                        sys.exit()
                self._check_keydown(event)
                self._check_keyup(event)                
                          
    def _check_keyup(self,event):
        if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = False

    def _check_keydown(self,event):
        if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                    if event.key == pygame.K_SPACE:
                        self._fire_bullet()            

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_count:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        available_width = self.settings.screen_width - (2*alien_width)
        number_of_aliens = available_width//(2*alien_width)
        available_height = self.settings.screen_height - self.ship.rect.height - 3*alien_width
        number_of_rows = available_height//(2*alien_height)

        for row_number in range(number_of_rows):
            for alien_number in range(number_of_aliens-1):
                self._create_alien(alien_number,row_number)
            
    def _create_alien(self,alien_number,row_number):
        alien = Alien(self)
        alien.x = alien.rect.width + 2*alien_number*alien.rect.width
        alien.rect.y = alien.rect.height + 2*row_number*alien.rect.height
        alien.rect.x = alien.x
        self.aliens.add(alien)

    def _check_mouse_play_click(self,mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
            self.stats.reset_stats()
            self.aliens.empty()
            self.stats.game_active = True
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)


    def _update_screen(self):
        # self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.bg,(0,0))
        self.ship.blitme()
        self.aliens.draw(self.screen)# built in sprite method to draw 
        for bullet in self.bullets.sprites():
            bullet.draw()
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()
         

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()


