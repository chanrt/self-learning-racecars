from math import ceil

import pygame as pg


class Settings:
    def __init__(self):
        self.grid_size = 75
        
        self.road_color = pg.Color("#807e78")
        self.grass_color = pg.Color("#006400")
        self.boundary_color = pg.Color("black")
        self.grid_color = pg.Color("white")

    def set_screen(self, screen):
        self.screen = screen
        self.screen_width, self.screen_height = screen.get_size()

        self.num_rows = ceil(self.screen_height / self.grid_size)
        self.num_cols = ceil(self.screen_width / self.grid_size)

    def set_track(self, track):
        self.track = track


settings = Settings()