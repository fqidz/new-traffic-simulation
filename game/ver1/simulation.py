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


def spawn_cars(dt):
    spawn_cars_list = load.cars(4, window=window, batch=main_batch, group=foreground)
    for car in spawn_cars_list:
        cars.append(car)


@window.event
def on_draw():
    window.clear()
    main_batch.draw()


def update(dt):
    all_closest_car = behavior.closest_car(cars)
    for i, obj in enumerate(cars):
        obj.update(dt)
        print(len(cars))

        # for idm data
        if len(cars) > 1:
            min_ray, (closest_car_dist, closest_car_vel) = all_closest_car[obj]

            obj.closest_car_ray = min_ray
            obj.closest_car_dist = closest_car_dist
            obj.closest_car_vel = closest_car_vel

        # delete car if out of screen
        if obj.x < 0 or obj.x > window.width or obj.y < 0 or obj.y > window.height:
            cars.pop(i)
            obj.delete()


if __name__ == "__main__":
    # Update the game 120 times per second
    pg.clock.schedule_interval(update, 1 / 120.0)
    pg.clock.schedule_interval(spawn_cars, 5)

    # Tell pyglet to do its thing
    pg.app.run()
