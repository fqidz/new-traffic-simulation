import math
import itertools

import pyglet as pg


def closest_car(car_list: dict):
    # TODO: better detection, maybe
    # unpack dict to get all cars and put it into a single list
    cars = list(itertools.chain(*car_list.values()))
    car_rays = {}  # all the car rays

    for cur_car in cars:
        other_cars = car_list[cur_car.lane_name].copy()
        other_cars.remove(cur_car)

        cur_to_other = {}  # rays from current car to other cars; will find the min ray here later
        for next_car in other_cars:
            if cur_car is not next_car:
                # get pos for the front of current car
                x = cur_car.x + cur_car.width / 2 * math.cos(-math.radians(cur_car.rotation))
                y = cur_car.y + (cur_car.height + 2) * math.sin(-math.radians(cur_car.rotation))

                # get pos for the back of other car
                x2 = next_car.x - next_car.width / 2 * math.cos(-math.radians(next_car.rotation))
                y2 = next_car.y - (next_car.height + 2) * math.sin(-math.radians(next_car.rotation))

                # cast straight ray in front of cur car to use to get fov angle
                xp = (x + 200 * math.cos(-math.radians(cur_car.rotation)))
                yp = (y + 200 * math.sin(-math.radians(cur_car.rotation)))

                # things to use for angle between func
                cur_car_pos = (x, y)
                cur_car_p = (xp, yp)
                other_car_pos = (x2, y2)

                # ray coords
                ray = (cur_car_pos, other_car_pos)
                ray_dist = math.dist(ray[0], ray[1])

                # only return ray if other car is in front fov of the cur car
                ang_between = angle_between(cur_car_pos, cur_car_p, other_car_pos)
                if -90 <= ang_between <= 90:
                    cur_to_other[ray] = [ray_dist, next_car.velocity_magnitude]
                else:
                    # else set ray to inf so ray will not get cast
                    cur_to_other[((float('inf'), float('inf')), (float('inf'), float('inf')))] = [float('inf'),
                                                                                                  float('inf')]

                # get the ray for closest car
                min_ray = min(cur_to_other, key=cur_to_other.get)

                # output the min ray and the corresponding speed of the next car
                car_rays[cur_car] = [min_ray, cur_to_other[min_ray]]

    return car_rays


def angle_between(o, p1, p2):
    v1 = (p1[0] - o[0], p1[1] - o[1])  # Vector from o to p1
    v2 = (p2[0] - o[0], p2[1] - o[1])  # Vector from o to p2
    dot_product = v1[0] * v2[0] + v1[1] * v2[1]
    magnitude_product = math.sqrt(
        (v1[0] ** 2 + v1[1] ** 2) * (v2[0] ** 2 + v2[1] ** 2))

    # catch math domain error (dot_product being >1; not allowed with acos)
    try:
        if 1 >= dot_product / magnitude_product:
            angle = math.acos(dot_product / magnitude_product)
        else:
            angle = math.radians(180)
    except ValueError:
        angle = math.radians(180)

    return math.degrees(angle)


# TODO: adjust for rotation
def col_check(x, y, obj: pg.sprite.Sprite):
    left = obj.x - obj.width / 2  # - (obj.height / 2 * math.cos(math.radians(obj.rotation)))
    right = obj.x + obj.width / 2  # + (obj.height / 2 * math.cos(math.radians(obj.rotation)))
    top = obj.y + obj.height / 2  # + (obj.width / 2 * math.sin(math.radians(obj.rotation)))
    bottom = obj.y - obj.height / 2  # - (obj.width / 2 * math.sin(math.radians(obj.rotation)))

    if (right > x > left and
            top > y > bottom):
        return True
    else:
        return False