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
cars = load.cars(8, 50, window=window, batch=main_batch, group=foreground)



@window.event
def on_draw():
    window.clear()
    main_batch.draw()


def update(dt):
    for obj in cars:
        obj.update(dt)
        print(obj.ray)


if __name__ == "__main__":
    # Update the game 120 times per second
    pg.clock.schedule_interval(update, 1 / 120.0)

    # Tell pyglet to do its thing
    pg.app.run()
