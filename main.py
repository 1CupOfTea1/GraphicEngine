from object_1 import *
from object_2 import *
from camera import *
from projection import *
import pygame_widgets
from pygame_widgets.slider import Slider
import pygame as pg
import numpy as np


class SoftwareRender:
    def __init__(self):
        pg.init()
        self.resolution = self.width, self.height = 1600, 900
        self.h_width, self.h_height = self.width // 2, self.height // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.resolution)
        self.clock = pg.time.Clock()
        self.create_objects()
        self.toggle_object = 1
        self.toggle_object2 = 1
        self.starttime = 0
        self.starttime2 = 0
        self.flag = True
        self.flag2 = True

    def toggle_objects(self):
        key = pg.key.get_pressed()
        if key[pg.K_1] and self.flag:
            self.starttime = pg.time.get_ticks()
            self.toggle_object *= -1
            self.flag = False

        if key[pg.K_2] and self.flag2:
            self.starttime2 = pg.time.get_ticks()
            self.toggle_object2 *= -1
            self.flag2 = False

        if self.flag == False and pg.time.get_ticks() - self.starttime >= 100:
            self.flag = True

        if self.flag2 == False and pg.time.get_ticks() - self.starttime2 >= 100:
            self.flag2 = True

    def create_objects(self):
        self.camera = Camera(self, [0.5, 1, -4])
        self.projection = Projection(self)
        self.object = Object1(self)
        self.object2 = Object2(self)
        self.object.translate([0.2, 0.4, 0.2])
        self.object.rotate_y(math.pi / 6)
        self.object2.translate([0.4, 0.8, 0.4])
        self.object2.rotate_y(math.pi / 6)

    def draw(self):
        self.screen.fill(pg.Color('#4a4848'))
        if self.toggle_object == 1:
            self.object.draw()
        if self.toggle_object2 == 1:
            self.object2.draw()

    def run(self):
        while True:
            self.toggle_objects()
            self.draw()
            self.object.movement()
            self.object2.movement()
            self.camera.control()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)

if __name__ == '__main__':
    app = SoftwareRender()
    app.run()

