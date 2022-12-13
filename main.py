from numpy import zeros

import pygame as pg

from settings import settings as s


def loop():
    pg.init()
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    s.set_screen(screen)

    track = zeros((s.num_rows, s.num_cols), dtype=int)
    s.set_track(track)

    for i in range(s.num_rows):
        track[i, 0] = 1
        track[i, s.num_cols - 1] = 1
    for i in range(s.num_cols):
        track[0, i] = 1
        track[s.num_rows - 1, i] = 1

    edit_mode = True

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    return

        screen.fill(s.grass_color)

        draw_track()

        if edit_mode:
            draw_grid()        

        pg.display.update()


def draw_track():
    for row in range(s.num_rows):
        for col in range(s.num_cols):
            if row == 0 or row == s.num_rows - 1 or col == 0 or col == s.num_cols - 1:
                color = s.boundary_color
            elif s.track[row, col] == 0:
                color = s.grass_color
            else:
                color = s.road_color
            
            pg.draw.rect(s.screen, color, (col * s.grid_size, row * s.grid_size, s.grid_size, s.grid_size))


def draw_grid():
    for i in range(0, s.screen_width, s.grid_size):
        pg.draw.line(s.screen, s.grid_color, (i, 0), (i, s.screen_height))

    for i in range(0, s.screen_height, s.grid_size):
        pg.draw.line(s.screen, s.grid_color, (0, i), (s.screen_width, i))


if __name__ == '__main__':
    loop()