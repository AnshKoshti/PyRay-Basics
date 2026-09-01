from pyray import *
from raylib import *
from os.path import join

set_config_flags(FLAG_WINDOW_HIGHDPI | FLAG_WINDOW_RESIZABLE)
init_window(800, 600, "Base")


# Importing things.
spaceship_texture = load_texture(join("assets", "spaceship.png"))
spaceship_image = load_image(join("assets", "spaceship.png"))

image_color_grayscale(spaceship_image)
new_texture = load_texture_from_image(spaceship_image)

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

    # Display images.
    draw_texture(spaceship_texture, 0, 0, WHITE)
    draw_texture_v(new_texture, Vector2(100, 0), WHITE)

    end_drawing()
close_window()
