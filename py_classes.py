from pyray import *
from raylib import *
from os.path import join


class Player:
    def __init__(self, pos):
        self.pos = pos
        self.texture = load_texture(join("assets", "spaceship.png"))
        self.direction = Vector2()
        self.speed = 400

    def update(self):
        self.direction.x = int(is_key_down(KEY_D)) - int(is_key_down(KEY_A))
        self.direction.y = int(is_key_down(KEY_S)) - int(is_key_down(KEY_W))
        self.direction = Vector2Normalize(self.direction)

        dt = get_frame_time()
        self.pos.x += self.direction.x * self.speed * dt
        self.pos.y += self.direction.y * self.speed * dt

    def draw(self):
        draw_texture_v(self.texture, self.pos, WHITE)


init_window(1920, 1080, "Raylib - Classes.")
player = Player(Vector2(500, 200))

while not window_should_close():
    begin_drawing()
    clear_background(BLACK)
    player.update()
    player.draw()
    end_drawing()

close_window()
