from collections import deque

import pyglet as pg
import itertools

from game import behavior, load

# Set up a window
window = pg.window.Window(1000, 1000)

# Set up batches
main_batch = pg.graphics.Batch()
# background is guaranteed to be drawn before the foreground
background = pg.graphics.Group(order=0)
foreground = pg.graphics.Group(order=1)

# init lists to be drawn later
cars = []
# each lane will have a list of cars that are there
cars_per_lane = {"right_left_lane": [],
                 "right_right_lane": [],
                 "top_left_lane": [],
                 "top_right_lane": [],
                 "left_left_lane": [],
                 "left_right_lane": [],
                 "bottom_left_lane": [],
                 "bottom_right_lane": []}

# TODO: switch out for full background image
road = load.road(500, 500, batch=main_batch, group=background)

# TEST for lines
lines = deque(maxlen=30)


def spawn_cars(dt):
    spawn_cars_list = load.cars(1, batch=main_batch, group=foreground)
    for car in spawn_cars_list:
        cars_per_lane[car.lane_name].append(car)


@window.event
def on_draw():
    window.clear()
    main_batch.draw()


@window.event
def on_mouse_press(x, y, button, modifiers):
    for obj in cars:
        col_check = behavior.col_check(x, y, obj)
        if col_check and button == 1:  # stop or start car on left click
            if obj.run:
                print(f"car at {[x, y]} stopped")
                obj.run = False
            else:
                print(f"car at {[x, y]} continued")
                obj.run = True
        elif col_check and button == 4:  # print info about car on right click
            print(f"speed: {obj.speed}")


def update(dt):
    # unpack dict to get all items and put it into a single list
    # not that great implementation ik
    global cars
    cars = list(itertools.chain(*cars_per_lane.values()))
    all_closest_car = behavior.closest_car(cars_per_lane)

    # print(len(cars))
    for i, obj in enumerate(cars):
        obj.update(dt)

        if len(cars) > 1:
            try:
                min_ray, (closest_car_dist, closest_car_vel) = all_closest_car[obj]

                # for idm data
                obj.closest_car_ray = min_ray
                obj.closest_car_dist = closest_car_dist
                obj.closest_car_vel = closest_car_vel

                # raycast line test
                lines.append(
                    pg.shapes.Line(obj.closest_car_ray[0][0], obj.closest_car_ray[0][1], obj.closest_car_ray[1][0],
                                   obj.closest_car_ray[1][1], batch=main_batch, group=foreground,
                                   color=(255, 255, 255, 50)))
            except KeyError:
                pass

        # delete car if out of screen
        if (obj.x < (0 - obj.width / 2) or
                obj.x > (window.width + obj.width / 2) or
                obj.y < (0 - obj.height / 2) or
                obj.y > (window.height + obj.height / 2)):
            # pop from car list
            cars.pop(i)
            # remove from cars_per_lane dict
            for a in cars_per_lane.values():
                try:
                    a.remove(obj)
                except ValueError:
                    pass

            # actually delete the car
            obj.delete()


if __name__ == "__main__":
    # Update the game 120 times per second
    pg.clock.schedule_interval(update, 1 / 120.0)
    # Spawn cars every interval
    pg.clock.schedule_interval(spawn_cars, 0.5)

    pg.app.run()
