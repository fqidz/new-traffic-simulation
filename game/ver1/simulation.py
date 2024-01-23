from collections import deque

import pyglet as pg

from game import behavior, load

# Set up a window
window = pg.window.Window(1000, 1000)

# Set up batches
main_batch = pg.graphics.Batch()
background = pg.graphics.Group(order=0)
foreground = pg.graphics.Group(order=1)

# Spawn car sprites
cars = []

# TEST
lines = deque(maxlen=50)


def spawn_cars(dt):
    spawn_cars_list = load.cars(1, window=window, batch=main_batch, group=foreground)
    for car in spawn_cars_list:
        cars.append(car)


@window.event
def on_draw():
    window.clear()
    main_batch.draw()


@window.event
def on_mouse_press(x, y, button, modifiers):
    # printing some message
    for obj in cars:
        col_check = behavior.col_check(x, y, obj)
        if col_check:
            if obj.run:
                print(f"car at {[x, y]} stopped")
                obj.run = False
            elif not obj.run:
                print(f"car at {[x, y]} continued")
                obj.run = True


def update(dt):
    all_closest_car = behavior.closest_car(cars)
    for i, obj in enumerate(cars):
        obj.update(dt)

        # for idm data
        if len(cars) > 1:
            min_ray, (closest_car_dist, closest_car_vel) = all_closest_car[obj]

            obj.closest_car_ray = min_ray
            obj.closest_car_dist = closest_car_dist
            obj.closest_car_vel = closest_car_vel

            # lines.append(pg.shapes.Line(obj.closest_car_ray[0][0], obj.closest_car_ray[0][1],
            # obj.closest_car_ray[1][0],
            #                             obj.closest_car_ray[1][1], batch=main_batch, group=foreground))

        # delete car if out of screen
        if (obj.x < (0 - obj.width / 2) or
                obj.x > (window.width + obj.width / 2) or
                obj.y < (0 - obj.height / 2) or
                obj.y > (window.height + obj.height / 2)):
            cars.pop(i)
            obj.delete()


if __name__ == "__main__":
    # Update the game 120 times per second
    pg.clock.schedule_interval(update, 1 / 120.0)
    # Spawn cars every interval
    pg.clock.schedule_interval(spawn_cars, 0.5)

    pg.app.run()
