from pico2d import *
import game_world
import game_framework
import random

class Ball:
    image = None

    def __init__(self, x = None, y = None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(100, 1180)
        self.y = y if y else random.randint(100, 924)

    def draw(self):
        # self.image.draw(self.x, self.y)
        
        sx, sy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
        # sx, sy = self.bg.cw // 2, self.bg.ch // 2
        self.image.draw(sx, sy)
        draw_rectangle(sx-10,sy-10,sx+10,sy+10)

    def update(self):
        pass

    def set_background(self, bg):
        self.bg = bg
       
        
    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        match group:
            case 'boy:ball':
                game_world.remove_object(self)
                pass
            