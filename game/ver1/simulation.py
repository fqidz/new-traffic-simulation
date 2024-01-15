import math
from collections import deque

import pyglet as pg

from game import load

# Set up a window
window = pg.window.Window(1000, 1000)

# Set up batches
main_batch = pg.graphics.Batch()
background = pg.graphics.Group(order=0)
foreground = pg.graphics.Group(order=1)

# Spawn car sprites
cars = load.cars(8, 50, window=window, batch=main_batch, group=foreground)

closest_distance = float('inf')
closest_car = None

cars_lines = deque(maxlen=len(cars))


@window.event
def on_draw():
    window.clear()
    main_batch.draw()


def update(dt):
    for obj in cars:
        obj.update(dt)
    for i, car in enumerate(cars):
        # copy list of cars
        cars_dup = cars.copy()
        # remove current car
        cars_dup.pop(i)
        # init the lines that this current car will have
        car_lines = []
        for other_cars in cars_dup:
            # draw line from current car to all other cars
            line = pg.shapes.Line(car.x, car.y, other_cars.x, other_cars.y, width=1, batch=main_batch,
                                  group=foreground)
            line_length = math.dist((line.x, line.y), (line.x2, line.y2))
            car_lines.append([line, line_length])
        cars_lines.append(car_lines)
    print(cars_lines)
    # TODO: only get line that is shortest


if __name__ == "__main__":
    # Update the game 120 times per second
    pg.clock.schedule_interval(update, 1 / 120.0)

    # Tell pyglet to do its thing
    pg.app.run()
