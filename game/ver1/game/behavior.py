import math

import pyglet as pg


# TODO: transfer this to an actual closest car distance function
def closest_car(car_list: list, output_list: list, batch, group):
    for cur_car in car_list:
        x = cur_car.x
        y = cur_car.y
        x2 = cur_car.x + (200 * math.cos(-math.radians(cur_car.rotation)))
        y2 = cur_car.y + (200 * math.sin(-math.radians(cur_car.rotation)))

        ray = pg.shapes.Line(x, y, x2, y2, batch=batch, group=group)

        output_list.append(ray)