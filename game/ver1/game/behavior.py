import math


def closest_car(car_list: list):
    output = {}
    for i, cur_car in enumerate(car_list):
        other_cars = car_list.copy()
        other_cars.pop(i)
        cur_to_other = {}
        for next_car in other_cars:
            x = cur_car.x
            y = cur_car.y
            x2 = next_car.x
            y2 = next_car.y

            # get line in front of cur car
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
            if -30 <= ang_between <= 30:
                cur_to_other[ray] = ray_dist
            else:
                cur_to_other[((float('inf'), float('inf')), (float('inf'), float('inf')))] = float('inf')

            # output the ray for closest car
            output[cur_car] = min(cur_to_other, key=cur_to_other.get)

    return output


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
