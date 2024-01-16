import math

import pyglet as pg

from .collision import bounding_box


class CarObject(pg.sprite.Sprite):
    """A sprite with physical properties such as velocity"""

    def __init__(self, *args, **kwargs):
        super(CarObject, self).__init__(*args, **kwargs)

        self.speed = 100
        # In addition to position, we have velocity
        self.velocity_x, self.velocity_y = 0.0, 0.0
        self.vel = 20

        # init ray
        self.ray = None
        self.ray_x2 = 0
        self.ray_y2 = 0

        # bounding box
        self.bounding_box_lines = None

    def velocity(self, speed):
        self.velocity_x = speed * math.cos(-math.radians(self.rotation))
        self.velocity_y = speed * math.sin(-math.radians(self.rotation))

    def update(self, dt):
        """This method should be called every frame."""
        self.velocity(self.speed)
        self.check_collision()
        # get bounding box
        self.bounding_box_lines = bounding_box(self)

        # Update position according to velocity and time
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        self.rotation += 1 * dt
    
    def raycast(self):
        """Send out a ray in front of car"""
        # ray_x1 = self.x
        # ray_y1 = self.y
        self.ray_x2 = self.x + (200 * math.cos(-math.radians(self.rotation)))
        self.ray_y2 = self.y + (200 * math.sin(-math.radians(self.rotation)))

        self.ray = ((self.x, self.y), (self.ray_x2, self.ray_y2))

    def check_collision(self):
        self.raycast()
