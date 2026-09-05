from pyray import *
from raylib import *
from os.path import join

# Windows defind parameters.
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
set_config_flags(FLAG_WINDOW_HIGHDPI | FLAG_WINDOW_RESIZABLE)

# initializing window and closing key for window.
init_window(SCREEN_HEIGHT, SCREEN_HEIGHT, "Player Input.")
set_exit_key(KEY_ESCAPE)

# Variables for import and textures.
spaceship = load_texture(join("assets", "spaceship.png"))
ship_pos = Vector2(0, 0)
ship_direction = Vector2(0, 0)
ship_speed = 500

while not window_should_close():

    # Input section.
    # Mouse input in which ship follows the player mouse.
    # ship_pos = get_mouse_position()

    # # State of the mouse button.
    # if is_mouse_button_released(0):
    #     print("Mouse button is pressed.")

    # Keyboard input.
    ship_direction.x = int(is_key_down(KEY_D)) - int(is_key_down(KEY_A))
    ship_direction.y = int(is_key_down(KEY_S)) - int(is_key_down(KEY_W))
    ship_direction = Vector2Normalize(ship_direction)

    # Movement update.
    dt = get_frame_time()
    ship_pos.x += ship_direction.x * ship_speed * dt
    ship_pos.y += ship_direction.y * ship_speed * dt

    # Drawing functions.
    begin_drawing()
    clear_background(BLACK)
    draw_texture_v(spaceship, ship_pos, WHITE)
    end_drawing()

close_window()
