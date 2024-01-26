import itertools
import math

import pyglet as pg


def closest_car(car_list: dict):
    # TODO: redo how its checking for closest car
    # unpack dict to get all cars and put it into a single list
    cars = list(itertools.chain(*car_list.values()))
    car_rays = {}  # all the car rays

    for cur_car in cars:
        # get all cars on same lane
        other_cars = car_list[cur_car.lane_name].copy()

        # get all id in same lane, in order from greatest to smallest
        all_car_id = []
        for other_car in other_cars:
            all_car_id.append(other_car.id)

        for other_car in other_cars:
            chosen_id = float('inf')

            # checks if other car is the next car from the current car
            for car_id in all_car_id:
                all_car_id_copy = all_car_id.copy()  # copy id list
                if other_car.id != cur_car.id and car_id == other_car.id:
                    # i dont even understand
                    chosen_id = car_id
                    break
                else:
                    all_car_id_copy.pop(0)  # pop id and check again

            if chosen_id < cur_car.id:
                next_car = other_car

                # get pos for the front of current car
                x = cur_car.x + cur_car.width / 2 * math.cos(-math.radians(cur_car.rotation))
                y = cur_car.y + (cur_car.height + 2) * math.sin(-math.radians(cur_car.rotation))

                # get pos for the back of other car
                x2 = next_car.x - next_car.width / 2 * math.cos(-math.radians(next_car.rotation))
                y2 = next_car.y - (next_car.height + 2) * math.sin(-math.radians(next_car.rotation))

                # ray coords
                ray = ((x, y), (x2, y2))
                ray_dist = math.dist(ray[0], ray[1])

                car_rays[cur_car] = [ray, [ray_dist, next_car.velocity_magnitude]]

        # cur_to_other = {}  # rays from current car to other cars; will find the min ray here later
        # for next_car in other_cars:
        #     if cur_car is not next_car:
        #         # get pos for the front of current car
        #         x = cur_car.x + cur_car.width / 2 * math.cos(-math.radians(cur_car.rotation))
        #         y = cur_car.y + (cur_car.height + 2) * math.sin(-math.radians(cur_car.rotation))
        #
        #         # get pos for the back of other car
        #         x2 = next_car.x - next_car.width / 2 * math.cos(-math.radians(next_car.rotation))
        #         y2 = next_car.y - (next_car.height + 2) * math.sin(-math.radians(next_car.rotation))
        #
        #         # cast straight ray in front of cur car to use to get fov angle
        #         xp = (x + 200 * math.cos(-math.radians(cur_car.rotation)))
        #         yp = (y + 200 * math.sin(-math.radians(cur_car.rotation)))
        #
        #         # things to use for angle between func
        #         cur_car_pos = (x, y)
        #         cur_car_p = (xp, yp)
        #         other_car_pos = (x2, y2)
        #
        #         # ray coords
        #         ray = (cur_car_pos, other_car_pos)
        #         ray_dist = math.dist(ray[0], ray[1])
        #
        #         # only return ray if other car is in front fov of the cur car
        #         ang_between = angle_between(cur_car_pos, cur_car_p, other_car_pos)
        #         if -1 <= ang_between <= 1:
        #             cur_to_other[ray] = [ray_dist, next_car.velocity_magnitude]
        #         else:
        #             # else set ray to inf so ray will not get cast
        #             cur_to_other[((float('inf'), float('inf')), (float('inf'), float('inf')))] = [float('inf'),
        #                                                                                           float('inf')]
        #
        #         # get the ray for closest car
        #         min_ray = min(cur_to_other, key=cur_to_other.get)
        #
        #         # output the min ray and the corresponding speed of the next car
        #         car_rays[cur_car] = [min_ray, cur_to_other[min_ray]]

    return car_rays


def angle_between(o, p1, p2):
    v1 = (p1[0] - o[0], p1[1] - o[1])  # Vector from o to p1
    v2 = (p2[0] - o[0], p2[1] - o[1])  # Vector from o to p2
    dot_product = v1[0] * v2[0] + v1[1] * v2[1]
    magnitude_product = math.sqrt(
        (v1[0] ** 2 + v1[1] ** 2) * (v2[0] ** 2 + v2[1] ** 2))

    if dot_product > 0:
        # duct tape fix for acos having >1 input (math domain error)
        if 1 >= dot_product / magnitude_product:
            angle = math.acos(dot_product / magnitude_product)
        else:
            angle = math.radians(180)
    else:
        angle = math.radians(180)

    return math.degrees(angle)


# TODO: adjust for rotation
def col_check(x, y, obj: pg.sprite.Sprite):
    left = obj.x - obj.width / 2
    right = obj.x + obj.width / 2
    top = obj.y + obj.height / 2
    bottom = obj.y - obj.height / 2

    if (right > x > left and
            top > y > bottom):
        return True
    else:
        return False
