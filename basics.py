from pyray import *
from raylib import *

init_window(800, 600, "Base")

while not window_should_close():
    begin_drawing()
    clear_background(BLACK)

    # Basic shape drawing.
    draw_pixel(100, 150, RED)
    draw_pixel_v(Vector2(200, 250), WHITE)
    draw_circle(300, 350, 10, GREEN)
    draw_circle_v(Vector2(400, 450), 30, BLUE)
    draw_line(100, 200, 300, 400, YELLOW)
    draw_line_ex(Vector2(150, 250), Vector2(350, 450), 10, ORANGE)

    end_drawing()
close_window()
