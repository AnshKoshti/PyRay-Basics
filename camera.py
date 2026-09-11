from pyray import *
from raylib import *
from random import randint, choice

# Simple window configs for SDL_3.
SetConfigFlags(FLAG_VSYNC_HINT | FLAG_WINDOW_HIGHDPI | FLAG_WINDOW_RESIZABLE)
init_window(1920, 1080, "Raylib camera.")

# Player variables.
pos = Vector2()
radius = 50
direction = Vector2()
speed = 200

# Circles list setup.
circles = [
    (
        Vector2(randint(-2000, 2000), randint(-1000, 1000)),
        randint(50, 200),
        choice([RED, GREEN, BLUE, YELLOW, ORANGE]),
    )
    for i in range(100)
]

# Camera setup.
camera = Camera2D()
camera.zoom = 1
camera.target = pos
camera.offset = Vector2(1920 / 2, 1080 / 2)

while not window_should_close():

    # Input.
    direction.x = int(is_key_down(KEY_RIGHT)) - int(is_key_down(KEY_LEFT))
    direction.y = int(is_key_down(KEY_DOWN)) - int(is_key_down(KEY_UP))
    direction = vector2_normalize(direction)

    # Movement.
    dt = get_frame_time()
    pos.x += direction.x * speed * dt
    pos.y += direction.y * speed * dt

    # Camera target.
    camera.target = pos

    # Drawing.
    begin_drawing()
    begin_mode_2d(camera)
    clear_background(WHITE)
    for circle in circles:
        draw_circle_v(*circle)
    draw_circle_v(pos, radius, BLACK)
    end_mode_2d()
    end_drawing()

close_window()
