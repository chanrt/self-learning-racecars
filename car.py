from math import cos, floor, pi, radians, sin, sqrt
from numba import njit
import pygame as pg

from neural_network import NeuralNetwork
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
        self.neural_network = NeuralNetwork([3, 4, 3])

        self.visited_sites = set()
        self.distance_travelled = 0
        self.alive = True

    def set_neural_network(self, neural_network):
        self.neural_network = neural_network

    def update(self):
        if self.alive:
            # sensor readings
            front_sensor, left_sensor, right_sensor = self.get_sensor_reading()
            front_sensor /= s.screen_width
            left_sensor /= s.screen_width
            right_sensor /= s.screen_width

            accelerator, left_prob, right_prob = self.neural_network.predict([front_sensor, left_sensor, right_sensor])
            displacement = accelerator * s.move_speed * s.dt

            # update car position
            self.x += cos(self.theta) * displacement
            self.y -= sin(self.theta) * displacement
            self.distance_travelled += displacement
            
            if left_prob > right_prob:
                self.theta += s.turn_speed * s.dt
            else:
                self.theta -= s.turn_speed * s.dt

            row = floor(self.y // s.grid_size)
            col = floor(self.x // s.grid_size)

            self.visited_sites.add((row, col))

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

        pg.draw.polygon(s.screen, pg.Color("red"), points, 2)