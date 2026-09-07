from pyray import *
from raylib import *

set_config_flags(FLAG_WINDOW_RESIZABLE)
init_window(1920, 1080, "Raylib collisions.")

player_pos = Vector2(0, 0)
obstacle_pos = Vector2(500, 400)
player_radius = 50
obstacle_radius = 30

while not window_should_close():

    # Input
    player_pos = get_mouse_position()

    # Collision.
    print(
        check_collision_circles(
            player_pos, player_radius, obstacle_pos, obstacle_radius
        )
    )

    # Drawing.
    begin_drawing()
    clear_background(BLACK)
    draw_circle_v(player_pos, player_radius, WHITE)
    draw_circle_v(obstacle_pos, obstacle_radius, RED)
    end_drawing()

close_window()
