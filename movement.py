from pyray import *
from raylib import *
from os.path import join

# Windows defind parameters.
set_config_flags(FLAG_WINDOW_HIGHDPI | FLAG_WINDOW_RESIZABLE)
init_window(1920, 1080, "Move")

# Only used in certain conditions, not ideal for frame consistent games.
# set_target_fps(60)

# Variables for import and definations.
spaceship = load_texture(join("assets", "spaceship.png"))
ship_pos = Vector2(0, 0)
ship_direction = Vector2(1, 1)
ship_speed = 100

while not window_should_close():

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
