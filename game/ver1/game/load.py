import random

from . import resources, carobject


def cars(num_cars, speed, window, batch=None, group=None):
    """Generate asteroid objects with random positions and velocities,
    not close to the player"""
    cars_list = []
    for i in range(num_cars):
        # rotate random 90 degrees
        rot = random.randint(0, 3) * 90

        # position car based on rotation
        if rot == 0:
            car_x = 0
            car_y = window.width / 2
        elif rot == 90:
            car_x = window.width / 2
            car_y = window.width
        elif rot == 180:
            car_x = window.width
            car_y = window.width / 2
        else:  # rot == 270
            car_x = window.width / 2
            car_y = 0

        new_car = carobject.CarObject(img=resources.car_image,
                                      x=car_x, y=car_y, batch=batch, group=group)

        # initialize rotation
        new_car.rotation = rot
        cars_list.append(new_car)
    return cars_list


def closest_car(ray_origin, ray_direction, cars):
    closest_distance = float('inf')
    closest_car = None

    for car in cars:
