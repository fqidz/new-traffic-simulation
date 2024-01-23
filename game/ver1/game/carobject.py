import math
import random

import pyglet as pg

# Real life dimensions / Proportions
# 1 m    =  10 px
# 10 px  =  1 m
#
# AVERAGE CAR DIMENSIONS   | 1:10 Ratio
# Length: 4.48m ............ (45.0 px) 44.8 px
# Width:  1.76m ............ (18.0 px) 17.6 px
#
# BAHRAIN ROAD DIMENSIONS
# Lane Width:    3.00m  .... 30.0 px
# 4 Lanes Width: 12.00m .... 120.0 px

RATIO = 10
INF = float('inf')
NAN = float('Nan')

class CarObject(pg.sprite.Sprite):
    """A sprite with physical properties such as velocity"""

    def __init__(self, *args, **kwargs):
        super(CarObject, self).__init__(*args, **kwargs)

        self.run = True
        self.lane = None

        # 8 m/s +- 2 m/s
        # multiplied by RATIO to translate it to px
        self.speed = 8 * RATIO + (random.random() * (2 * RATIO))

        # init velocity
        self.velocity_x, self.velocity_y = 0.0, 0.0
        self.velocity_magnitude = 0.0

        # init the closest car data
        self.closest_car_ray = None
        self.closest_car_dist = None
        self.closest_car_vel = None

    def velocity(self, speed):
        # Update velocity according to speed and current rotation
        self.velocity_x = speed * math.cos(-math.radians(self.rotation))
        self.velocity_y = speed * math.sin(-math.radians(self.rotation))
        self.velocity_magnitude = math.sqrt(self.velocity_x ** 2 + self.velocity_y ** 2)

    # TODO: Normalize pixel values to m/s^2, meters, and shit (SI units)
    def intelligent_driver_model(self, desired_velocity, minimum_spacing, desired_time_headway, maximum_acceleration,
                                 comfortable_braking_deceleration):
        """Takes in SI units (m/s, m) and outputs acceleration with SI units (m/s^2, m)
        based off of: https://youtu.be/4RxqKvi8Nys?t=3803"""

        # convert pixel values into SI units
        own_vel_mag = self.velocity_magnitude / RATIO

        if self.closest_car_dist and not math.isinf(self.closest_car_dist):
            closest_car_gap = self.closest_car_dist / RATIO
        else:
            closest_car_gap = 1000 / RATIO

        if self.closest_car_vel and not math.isinf(self.closest_car_vel):
            vel_diff = self.velocity_magnitude - self.closest_car_vel
            vel_diff = vel_diff / RATIO
        else:
            vel_diff = 0

        # dynamic desired gap
        desired_gap = minimum_spacing + own_vel_mag * desired_time_headway + (
                (own_vel_mag * vel_diff) /
                (2 * math.sqrt(maximum_acceleration * comfortable_braking_deceleration)))

        # intelligent driver model formula
        acceleration = (maximum_acceleration *
                        (1 - (own_vel_mag / desired_velocity) ** 4 - (desired_gap / closest_car_gap) ** 2))

        # print([closest_car_gap, vel_diff, own_vel_mag, desired_gap, acceleration])

        # handles when car doesn't have a closest car
        if (not math.isnan(acceleration) and
                acceleration != INF and
                acceleration != INF):
            # limit acceleration to 20
            if acceleration > 20:
                return 20
            elif acceleration < -20:
                return -20
            else:
                return acceleration

    def update(self, dt):
        """This method should be called every frame."""
        # calculate velocity every update
        self.velocity(self.speed)

        # input is in m/s and meters
        accel = self.intelligent_driver_model(8.0, 6.0, 0.5, 3.0, 3.0)

        # TODO: prevent cars from going backwards
        if accel:
            if self.run:
                # convert SI units to pixels and divide by framerate
                self.speed += (accel * RATIO) / 60.0
            else:
                self.speed *= 0.99

        # Update position according to velocity and time
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        # # Update rotation randomly according to time
        # self.rotation += random.randint(-20, 20) * dt
