import math
import random

import pyglet as pg

# TODO: Fix proportions/scale/ratio to be same as real life
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


class CarObject(pg.sprite.Sprite):
    """A sprite with physical properties such as velocity"""

    def __init__(self, *args, **kwargs):
        super(CarObject, self).__init__(*args, **kwargs)
        
        # 8 m/s +- 2 m/s; times 10 to translate it to px
        self.speed = 8 * 10 + (random.random() * (2 * 10))

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

    # TODO: Normalize pixel values to m/s^2, meters, and shit
    def intelligent_driver_model(self, desired_velocity, minimum_spacing, desired_time_headway, maximum_acceleration,
                                 comfortable_braking_deceleration, ):
        """Takes in international standard units (m/s, m) and outputs same (m/s^2, m)"""
        
        if self.closest_car_dist:
            closest_car_gap = self.closest_car_dist / 10
        else:
            closest_car_gap = float('inf')

        if self.closest_car_vel:
            vel_diff = self.velocity_magnitude - self.closest_car_vel
            vel_diff = vel_diff / 10
        else:
            vel_diff = float('inf')

        own_vel_mag = self.velocity_magnitude / 10

        desired_gap = minimum_spacing + own_vel_mag * desired_time_headway + (
                (own_vel_mag * vel_diff) /
                (2 * math.sqrt(maximum_acceleration * comfortable_braking_deceleration)))

        # intelligent driver model formula
        acceleration = (maximum_acceleration *
                        (1 - (own_vel_mag / desired_velocity) ** 4 - (desired_gap / closest_car_gap) ** 2))

        print([desired_velocity, minimum_spacing, desired_time_headway, maximum_acceleration,
               comfortable_braking_deceleration, closest_car_gap, vel_diff, own_vel_mag,
               desired_gap, acceleration])

        if not math.isnan(acceleration) and acceleration != float('inf') and acceleration != float('-inf'):
            return acceleration

    def update(self, dt):
        """This method should be called every frame."""
        self.velocity(self.speed)
        accel = self.intelligent_driver_model(8.0, 6.0, 1.0, 3.0, 1.5)
        if accel and (accel is not float('inf') or accel is not float('-inf')):
            # translate from meters to pixel; also divide by 60 fps
            self.speed += (accel * 10) / 60.0
        # else:
        #     if self.velocity_magnitude <= 8.0 * 10:
        #         self.speed = 100
        #     else:
        #         self.speed += (1.5 * 10) / 60.0

        # Update position according to velocity and time
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        self.rotation += random.randint(-20, 20) * dt
