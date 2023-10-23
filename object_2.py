import pygame as pg
from matrix import *
import numpy as np


class Object2:
    def __init__(self, render):
        self.render = render
        self.vertices = np.array(
            [(0, 0, 0, 1), (0, 0, 1, 1), (1, 0, 0, 1), (0.5, 1, 0.5, 1)])
        self.faces = np.array([(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)])

    def draw(self):
        self.screen_projection()

    def movement(self):
        key = pg.key.get_pressed()
        if key[pg.K_c]:
            self.rotate_y(pg.time.get_ticks() % 0.005)
        if key[pg.K_v]:
            self.rotate_y(-(pg.time.get_ticks() % 0.005))

    def screen_projection(self):
        vertices = self.vertices @ self.render.camera.camera_matrix()
        vertices = vertices @ self.render.projection.projection_matrix
        vertices /= vertices[:, -1].reshape(-1, 1)
        vertices[(vertices > 2) | (vertices < -2)] = 0
        vertices = vertices @ self.render.projection.to_screen_matrix
        vertices = vertices[:, :2]

        for face in self.faces:
            polygon = vertices[face]
            if not np.any((polygon == self.render.h_width) | (polygon == self.render.h_height)):
                pg.draw.polygon(self.render.screen, pg.Color('green'), polygon, 3)
        for vertice in vertices:
            if not np.any((vertice == self.render.h_width) | (vertice == self.render.h_height)):
                pg.draw.circle(self.render.screen, pg.Color('white'), vertice, 3)

    def translate(self, pos):
        self.vertices = self.vertices @ translate(pos)

    def scale(self, sc):
        self.vertices = self.vertices @ scale(sc)

    def rotate_x(self, angle):
        self.vertices = self.vertices @ rotate_x(angle)

    def rotate_y(self, angle):
        self.vertices = self.vertices @ rotate_y(angle)

    def rotate_z(self, angle):
        self.vertices = self.vertices @ rotate_z(angle)
