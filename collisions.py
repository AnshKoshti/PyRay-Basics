from pyray import *
from raylib import *

set_config_flags(FLAG_WINDOW_RESIZABLE)
init_window(800, 600, "Raylib collisions.")

player_pos = Vector2(0, 0)
obstacle_pos = Vector2(500, 400)
player_radius = 50
obstacle_radius = 30

# Rectangle functtion.
r1 = Rectangle(0, 0, 100, 200)
r2 = Rectangle(800, 500, 200, 300)

while not window_should_close():

    # Input
    player_pos = get_mouse_position()
    r1.x = get_mouse_x()
    r1.y = get_mouse_y()

    # Collision.
    # print(
    #     check_collision_circles(
    #         player_pos, player_radius, obstacle_pos, obstacle_radius
    #     )
    # )
    print(check_collision_recs(r1, r2))

    # Overlaping rectangle check.
    overlap_rec = get_collision_rec(r1, r2)

    # Drawing.
    begin_drawing()
    clear_background(BLACK)
    # draw_circle_v(player_pos, player_radius, WHITE)
    draw_circle_v(obstacle_pos, obstacle_radius, RED)
    draw_rectangle_rec(r1, BLUE)
    draw_rectangle_rec(r2, GREEN)

    if overlap_rec:
        draw_rectangle_rec(overlap_rec, RED)
    end_drawing()

close_window()
