import math
import random

import pyglet as pg

class CarObject(pg.sprite.Sprite):
    """A sprite with physical properties such as velocity"""

    def __init__(self, *args, **kwargs):
        super(CarObject, self).__init__(*args, **kwargs)

        self.speed = 100
        # In addition to position, we have velocity
        self.velocity_x, self.velocity_y = 0.0, 0.0
        self.velocity_magnitude = 0.0
        self.vel = 20

        # init the closest car coords
        self.closest_car = None

    def velocity(self, speed):
        self.velocity_x = speed * math.cos(-math.radians(self.rotation))
        self.velocity_y = speed * math.sin(-math.radians(self.rotation))
        self.velocity_magnitude = math.sqrt(self.velocity_x ** 2 + self.velocity_y ** 2)

    def update(self, dt):
        """This method should be called every frame."""
        self.velocity(self.speed)

        # Update position according to velocity and time
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        self.rotation += random.randint(-20, 20) * dt
