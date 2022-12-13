from math import atan, ceil, radians

import pygame as pg


class Settings:
    def __init__(self):
        self.fps = 60
        self.dt = 1.0 / self.fps

        # number of cars in each generation
        self.num_cars = 100

        # the length of each grid (in pixels)
        self.grid_size = 75

        # thickness of the car with respect to grid size
        self.car_thickness_ratio = 0.2

        # length of the car with respect to it's thickness
        self.car_length_ratio = 2

        # angle of the lateral sensors (in radians)
        self.sensor_angle = radians(45)

        # speed of the car (in pixels per second)
        self.move_speed = 100

        # steer rate of the car (in radians per second)
        self.turn_speed = radians(45)

        # step size of ray tracing (in pixels)
        self.ray_step = 1

        # genetic algo parameters
        self.mutation_rate = 0.05
        self.mutation_range = 0.5

        # colors
        self.road_color = pg.Color("#807e78")
        self.grass_color = pg.Color("#006400")
        self.boundary_color = pg.Color("black")
        self.start_color = pg.Color("yellow")
        self.finish_color = pg.Color("blue")
        self.grid_color = pg.Color("white")

        # calculated quantities
        self.car_thickness = self.grid_size * self.car_thickness_ratio
        self.car_length = self.car_thickness * self.car_length_ratio
        self.car_rect_angle = abs(atan(self.car_thickness / self.car_length))
        self.angle_correction = self.car_rect_angle

    def set_screen(self, screen):
        self.screen = screen
        self.screen_width, self.screen_height = screen.get_size()

        self.num_rows = ceil(self.screen_height / self.grid_size)
        self.num_cols = ceil(self.screen_width / self.grid_size)

    def set_track(self, track):
        self.track = track

    def set_dt(self, dt):
        self.dt = dt


settings = Settings()