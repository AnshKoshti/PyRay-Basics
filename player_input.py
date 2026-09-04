from pyray import *
from raylib import *
from os.path import join

# Windows defind parameters.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
set_config_flags(FLAG_WINDOW_HIGHDPI | FLAG_WINDOW_RESIZABLE)

# initializing window.
init_window(SCREEN_HEIGHT, SCREEN_HEIGHT, "Player Input.")

# Variables for import and textures.
spaceship = load_texture(join("assets", "spaceship.png"))
ship_pos = Vector2(0, 0)
ship_direction = Vector2(0, 0)
ship_speed = 100

while not window_should_close():

    # Drawing functions.
    begin_drawing()
    clear_background(BLACK)
    draw_texture_v(spaceship, ship_pos, WHITE)
    end_drawing()

close_window()
