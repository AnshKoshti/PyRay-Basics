from pyray import *
from raylib import *
from os.path import join


class Player:
    def __init__(self, pos):
        self.pos = pos
        self.texture = load_texture(join("assets", "spaceship.png"))


init_window(1920, 1080, "Raylib - Classes.")
player = Player((500, 200))


while not window_should_close():
    begin_drawing()
    clear_background(BLACK)
    draw_texture_v(player.texture, player.pos, WHITE)
    end_drawing()

close_window()
