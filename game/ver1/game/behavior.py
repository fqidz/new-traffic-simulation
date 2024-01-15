import math
from collections import deque

import pyglet as pg


# TODO: transfer this to an actual closest car distance function
def closest_car(car_list, batch, group):
    cars_all_lines = deque(maxlen=len(car_list))
    for i, cur_car in enumerate(car_list):
        # copy list of cars
        car_list_dup = car_list.copy()
        # remove current car from list
        car_list_dup.pop(i)
        # init the dict for lines that this current car will have
        cur_car_lines = {}
        for other_cars in car_list_dup:
            # draw line from current car to all other cars
            line = pg.shapes.Line(cur_car.x, cur_car.y, other_cars.x, other_cars.y, width=1, batch=batch,
                                  group=group)
            line_length = math.dist((line.x, line.y), (line.x2, line.y2))

            cur_car_lines[line] = line_length
        # append shortest line
        cars_all_lines.append(min(cur_car_lines, key=cur_car_lines.get))

    return cars_all_lines
