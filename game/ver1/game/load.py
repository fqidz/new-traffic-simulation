import random
import pyglet as pg
import time

from . import resources, carobject, roads


def road(x, y, batch=None, group=None):
    road_list = []
    vert_road = pg.sprite.Sprite(img=resources.road_image, x=x, y=y, batch=batch, group=group)
    horz_road = pg.sprite.Sprite(img=resources.road_image, x=x, y=y, batch=batch, group=group)

    horz_road.rotation = 90

    road_list.append(vert_road)
    road_list.append(horz_road)

    return road_list


def cars(num_cars, batch=None, group=None):
    """Generate car objects with random lane spawn"""
    cars_list = []
    for i in range(num_cars):
        # choose random lane
        car_lane_name, car_lane_loc = random.choice(list(roads.spawn_nodes.items()))
        car_x = car_lane_loc[0]
        car_y = car_lane_loc[1]

        # rotate car based on lane chosen
        if car_lane_name == "right_left_lane" or car_lane_name == "right_right_lane":
            rot = 180
        elif car_lane_name == "top_left_lane" or car_lane_name == "top_right_lane":
            rot = 90
        elif car_lane_name == "left_left_lane" or car_lane_name == "left_right_lane":
            rot = 0
        else:  # car_lane_name == "bottom_left_lane" or car_lane_name == "bottom_right_lane":
            rot = -90

        new_car = carobject.CarObject(img=resources.car_image,
                                      x=car_x, y=car_y, batch=batch, group=group)

        # save lane info to car
        new_car.lane_name = car_lane_name
        new_car.lane_loc = car_lane_loc
        # initialize rotation
        new_car.rotation = rot

        cars_list.append(new_car)
    return cars_list
