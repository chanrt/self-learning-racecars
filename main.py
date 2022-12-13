from numpy import zeros

import pygame as pg

from settings import settings as s


def loop():
    pg.init()
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    s.set_screen(screen)

    track = zeros((s.num_rows, s.num_cols), dtype=bool)
    s.set_track(track)

    # block edges
    for i in range(s.num_rows):
        track[i, 0] = False
        track[i, s.num_cols - 1] = False
    for i in range(s.num_cols):
        track[0, i] = False
        track[s.num_rows - 1, i] = False

    # open start and finish
    track[1, s.num_cols // 2 - 1] = True
    track[1, s.num_cols // 2] = True

    left_mouse_down = False
    right_mouse_down = False

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

            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    left_mouse_down = True
                elif event.button == 3:
                    right_mouse_down = True

            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    left_mouse_down = False
                elif event.button == 3:
                    right_mouse_down = False

        if edit_mode and (left_mouse_down or right_mouse_down):
            pos = pg.mouse.get_pos()
            row = pos[1] // s.grid_size
            col = pos[0] // s.grid_size

            if not is_boundary_tile(row, col) and not is_special_tile(row, col):
                if left_mouse_down:
                    s.track[row, col] = True
                else:
                    s.track[row, col] = False

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
            elif row == 1 and col == s.num_cols // 2 - 1:
                color = s.start_color
            elif row == 1 and col == s.num_cols // 2:
                color = s.finish_color
            elif not s.track[row, col]:
                color = s.grass_color
            else:
                color = s.road_color
            
            pg.draw.rect(s.screen, color, (col * s.grid_size, row * s.grid_size, s.grid_size, s.grid_size))


def draw_grid():
    for i in range(0, s.screen_width, s.grid_size):
        pg.draw.line(s.screen, s.grid_color, (i, 0), (i, s.screen_height))

    for i in range(0, s.screen_height, s.grid_size):
        pg.draw.line(s.screen, s.grid_color, (0, i), (s.screen_width, i))


def is_boundary_tile(row, col):
    return row == 0 or row == s.num_rows - 1 or col == 0 or col == s.num_cols - 1


def is_special_tile(row, col):
    if row != 1:
        return False

    if col == s.num_cols // 2 - 1 or col == s.num_cols // 2:
        return True
    else:
        return False


if __name__ == '__main__':
    loop()