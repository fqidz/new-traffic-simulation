from collections import deque

import pyglet as pg

from game import load, behavior

# Set up a window
window = pg.window.Window(1000, 1000)

# Set up batches
main_batch = pg.graphics.Batch()
background = pg.graphics.Group(order=0)
foreground = pg.graphics.Group(order=1)

# Spawn car sprites
cars = load.cars(4, window=window, batch=main_batch, group=foreground)
# TEST: raycast lines
lines = deque(maxlen=len(cars))


@window.event
def on_draw():
    window.clear()
    main_batch.draw()


def update(dt):
    all_closest_car = behavior.closest_car(cars)
    
    # all_closest_car = closest_car(cars)
    # for car, data in all_closest_car.items():
    #     min_ray, (ray_dist, velocity_magnitude) = data
    #     print(f"For car {car}, the smallest ray_dist is {ray_dist} and the corresponding velocity_magnitude is {velocity_magnitude}")
    for obj in cars:
        obj.update(dt)
        obj.closest_car = all_closest_car[obj]

        lines.append(
            pg.shapes.Line(obj.closest_car[0][0], obj.closest_car[0][1], obj.closest_car[1][0], obj.closest_car[1][1],
                           batch=main_batch, group=foreground))


if __name__ == "__main__":
    # Update the game 120 times per second
    pg.clock.schedule_interval(update, 1 / 120.0)

    # Tell pyglet to do its thing
    pg.app.run()
