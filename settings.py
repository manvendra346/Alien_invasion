class Settings:
    def __init__(self):

        self.speedup_scale = 1.1

        #screen setting
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (65, 74, 76)

        #ship settings
        self.ship_limit = 3
        #alien setting
        self.fleet_direction = 1
        self.fleet_drop_speed = 100

        #bullet settings
        self.bullet_height = 10
        self.bullet_width = 5
        self.bullet_color = (255,255,255)
        self.bullet_count = 5

        self.reset_dynamic_settings()

    def reset_dynamic_settings(self):
        self.bullet_speed = 2
        self.alien_speed = 1.0  
        self.ship_speed = 1
        self.kill_score = 50

    def change_speed(self):
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale