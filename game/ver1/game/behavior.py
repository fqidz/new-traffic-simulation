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

            ray = ((x, y), (x2, y2))
            dist = math.dist((x, y), (x2, y2))

            cur_to_other[ray] = dist

        output[cur_car] = min(cur_to_other, key=cur_to_other.get)

    return output
