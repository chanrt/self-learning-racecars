from math import cos, floor, pi, sin, sqrt
from numba import njit
import pygame as pg

from settings import settings as s


@njit
def raycast(x0, y0, theta, track, grid_size):
    x, y = x0, y0
    dx, dy = cos(theta), sin(theta)

    while True:
        x += dx
        y -= dy

        row = floor(y / grid_size)
        col = floor(x / grid_size)

        if not track[row, col]:
            break

    distance = sqrt((x - x0) ** 2 + (y - y0) ** 2)
    return distance


class Car:
    def __init__(self):
        self.x = (s.num_cols // 2 - 1 + 0.5) * s.grid_size
        self.y = (1 + 0.5) * s.grid_size
        self.theta = pi

        self.alive = True

    def update(self):
        if self.alive:
            # move forward
            speed = 1
            self.x += speed * cos(self.theta)
            self.y -= speed * sin(self.theta)

            # sensor readings
            front_sensor, left_sensor, right_sensor = self.get_sensor_reading()
            print(front_sensor, left_sensor, right_sensor)

            row = floor(self.y // s.grid_size)
            col = floor(self.x // s.grid_size)

            if not s.track[row, col]:
                self.alive = False

    def get_sensor_reading(self):
        front_sensor = raycast(self.x, self.y, self.theta, s.track, s.grid_size)
        left_sensor = raycast(self.x, self.y, self.theta + s.sensor_angle, s.track, s.grid_size)
        right_sensor = raycast(self.x, self.y, self.theta - s.sensor_angle, s.track, s.grid_size)

        return front_sensor, left_sensor, right_sensor

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