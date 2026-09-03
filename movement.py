from pyray import *
from raylib import *
from os.path import join

# Windows defind parameters.
set_config_flags(FLAG_WINDOW_HIGHDPI | FLAG_WINDOW_RESIZABLE)
init_window(1920, 1080, "Move")

# Variables for import and definations.
spaceship = load_texture(join("assets", "spaceship.png"))
pos_x = 0
pos_y = 0

while not window_should_close():

    # Drawing functions.
    begin_drawing()
    clear_background(BLACK)
    draw_texture(spaceship, pos_x, pos_y, WHITE)
    end_drawing()

close_window()
