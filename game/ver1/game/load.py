import random

from . import resources, carobject


def cars(num_cars, window, batch=None, group=None):
    """Generate asteroid objects with random positions and velocities,
    not close to the player"""
    cars_list = []
    for i in range(num_cars):
        # rotate random 90 degrees
        rot = random.randint(0, 1) * 180

        # position car based on rotation
        if rot == 0:
            # left
            car_x = 0
            car_y = window.width / 2
        elif rot == 90:
            # up
            car_x = window.width / 2
            car_y = window.width
        elif rot == 180:
            # right
            car_x = window.width
            car_y = window.width / 2
        else:  # rot == 270
            # down
            car_x = window.width / 2
            car_y = 0

        new_car = carobject.CarObject(img=resources.car_image,
                                      x=car_x, y=car_y, batch=batch, group=group)

        # initialize rotation
        new_car.rotation = rot
        cars_list.append(new_car)
    return cars_list

