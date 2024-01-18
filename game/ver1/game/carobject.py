import math
import random

import pyglet as pg


class CarObject(pg.sprite.Sprite):
    """A sprite with physical properties such as velocity"""

    def __init__(self, *args, **kwargs):
        super(CarObject, self).__init__(*args, **kwargs)

        self.speed = random.randint(80, 100)
        # In addition to position, we have velocity
        self.velocity_x, self.velocity_y = 0.0, 0.0
        self.velocity_magnitude = 0.0

        # init the closest car data
        self.closest_car_ray = None
        self.closest_car_dist = None
        self.closest_car_vel = None

    def velocity(self, speed):
        self.velocity_x = speed * math.cos(-math.radians(self.rotation))
        self.velocity_y = speed * math.sin(-math.radians(self.rotation))
        self.velocity_magnitude = math.sqrt(self.velocity_x ** 2 + self.velocity_y ** 2)

    def intelligent_driver_model(self, desired_velocity, minimum_spacing, desired_time_headway, maximum_acceleration,
                                 comfortable_braking_deceleration, delta=4):
        if self.closest_car_dist:
            net_dist = self.closest_car_dist
        else:
            net_dist = float('inf')

        if self.closest_car_vel:
            vel_diff = self.velocity_magnitude - self.closest_car_vel
        else:
            vel_diff = float('inf')

        # intelligent driver model formula
        dynamic_net_distance = minimum_spacing + self.velocity_magnitude * desired_time_headway + (
                (self.velocity_magnitude * vel_diff) / (
                2 * math.sqrt(maximum_acceleration * comfortable_braking_deceleration)))

        acceleration = maximum_acceleration * (
                1 - (self.velocity_magnitude / desired_velocity) ** delta - (dynamic_net_distance / net_dist) ** 2)

        print([desired_velocity, minimum_spacing, desired_time_headway, maximum_acceleration,
               comfortable_braking_deceleration, delta, net_dist, vel_diff, self.velocity_magnitude,
               dynamic_net_distance, acceleration])

        return acceleration

    def update(self, dt):
        """This method should be called every frame."""
        self.velocity(self.speed)

        self.intelligent_driver_model(10, 20, 1, 0.3, 0.3)
        # Update position according to velocity and time
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        self.rotation += random.randint(-20, 20) * dt
