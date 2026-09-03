from pyray import *
from raylib import *
from os.path import join

# Windows defind parameters.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
set_config_flags(FLAG_WINDOW_HIGHDPI | FLAG_WINDOW_RESIZABLE)

# initializing window.
init_window(SCREEN_HEIGHT, SCREEN_HEIGHT, "Move")

# Only used in certain conditions, not ideal for frame consistent games.
# set_target_fps(60)

# Variables for import and textures.
spaceship = load_texture(join("assets", "spaceship.png"))
ship_pos = Vector2(0, 0)
ship_direction = Vector2(1, 1)
ship_speed = 100

while not window_should_close():

    # Ship edge bounding.
    if ship_pos.x >= SCREEN_WIDTH:
        ship_direction.x = -1
    if ship_pos.y >= SCREEN_HEIGHT:
        ship_direction.y = -1
    if ship_pos.x <= 0:
        ship_direction.x = 1
    if ship_pos.y <= 0:
        ship_direction.y = 1

    # Movement update.
    dt = get_frame_time()
    ship_pos.x += ship_direction.x * ship_speed * dt
    ship_pos.y += ship_direction.y * ship_speed * dt

    # Drawing functions.
    begin_drawing()
    clear_background(BLACK)
    draw_texture_v(spaceship, ship_pos, WHITE)
    draw_fps(0, 0)
    end_drawing()

close_window()
