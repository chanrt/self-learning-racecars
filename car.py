from math import cos, pi, sin
import pygame as pg

from settings import settings as s


class Car:
    def __init__(self):
        self.x = (s.num_cols // 2 - 1 + 0.5) * s.grid_size
        self.y = (1 + 0.5) * s.grid_size
        self.theta = pi

    def update(self):
        speed = 1
        self.x += speed * cos(self.theta)
        self.y -= speed * sin(self.theta)

    def render(self):
        points = []
        angle = self.theta + s.car_rect_angle + s.angle_correction
        points.append((self.x + cos(angle) * s.car_length / 2 + sin(angle) * s.car_thickness / 2, self.y + cos(angle) * s.car_thickness / 2 - sin(angle) * s.car_length / 2))

        angle = self.theta + pi - s.car_rect_angle + s.angle_correction
        points.append((self.x + cos(angle) * s.car_length / 2 + sin(angle) * s.car_thickness / 2, self.y + cos(angle) * s.car_thickness / 2 - sin(angle) * s.car_length / 2))

        angle = self.theta + pi + s.car_rect_angle + s.angle_correction
        points.append((self.x + cos(angle) * s.car_length / 2 + sin(angle) * s.car_thickness / 2, self.y + cos(angle) * s.car_thickness / 2 - sin(angle) * s.car_length / 2))

        angle = self.theta - s.car_rect_angle + s.angle_correction
        points.append((self.x + cos(angle) * s.car_length / 2 + sin(angle) * s.car_thickness / 2, self.y + cos(angle) * s.car_thickness / 2 - sin(angle) * s.car_length / 2))

        pg.draw.polygon(s.screen, pg.Color("red"), points)