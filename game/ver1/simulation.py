import pyglet as pg
import math
from collections import deque

from game import load

# Set up a window
window = pg.window.Window(1000, 1000)

# Set up batches
main_batch = pg.graphics.Batch()
background = pg.graphics.Group(order=0)
foreground = pg.graphics.Group(order=1)

# Spawn car sprites
cars = load.cars(20, 50, window=window, batch=main_batch, group=foreground)

# cars line
cars_all_lines = deque(maxlen=len(cars))



@window.event
def on_draw():
    window.clear()
    main_batch.draw()


def update(dt):
    for obj in cars:
        obj.update(dt)
    for i, cur_car in enumerate(cars):
        # copy list of cars
        car_list_dup = cars.copy()
        # remove current car from list
        car_list_dup.pop(i)
        # init the dict for lines that this current car will have
        cur_car_lines = {}
        for other_cars in car_list_dup:
            # draw line from current car to all other cars
            line = pg.shapes.Line(cur_car.x, cur_car.y, other_cars.x, other_cars.y, width=1, batch=main_batch,
                                  group=foreground)
            line_length = math.dist((line.x, line.y), (line.x2, line.y2))

            cur_car_lines[line] = line_length
        # append shortest line
        cars_all_lines.append(min(cur_car_lines, key=cur_car_lines.get))


if __name__ == "__main__":
    # Update the game 120 times per second
    pg.clock.schedule_interval(update, 1 / 120.0)

    # Tell pyglet to do its thing
    pg.app.run()
