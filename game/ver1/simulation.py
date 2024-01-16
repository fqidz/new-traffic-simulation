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
cars = load.cars(1, window=window, batch=main_batch, group=foreground)
# TEST: raycast lines
lines = deque(maxlen=len(cars))
bounding_boxes = deque(maxlen=len(cars))


@window.event
def on_draw():
    window.clear()
    main_batch.draw()


def update(dt):
    for obj in cars:
        obj.update(dt)
        # TEST: raycast lines
        line = pg.shapes.Line(obj.ray[0][0], obj.ray[0][1], obj.ray[1][0], obj.ray[1][1], batch=main_batch,
                              group=foreground)
        lines.append(line)

        # TEST: bounding box draw
        # for i, coord in enumerate(obj.bounding_box_lines[:-1]):
        bounding_boxes.append(pg.shapes.Line(obj.bounding_box_lines[0][0], obj.bounding_box_lines[0][1],
                                             obj.bounding_box_lines[0 + 1][0], obj.bounding_box_lines[0 + 1][0],
                                             batch=main_batch, group=foreground))
        print((obj.x, obj.y))
        print(obj.bounding_box_lines)


if __name__ == "__main__":
    # Update the game 120 times per second
    pg.clock.schedule_interval(update, 1 / 120.0)

    # Tell pyglet to do its thing
    pg.app.run()
