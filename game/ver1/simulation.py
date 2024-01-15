import pyglet as pg
import math

from game import load

# Set up a window
window = pg.window.Window(1000, 1000)

# Set up batches
main_batch = pg.graphics.Batch()
background = pg.graphics.Group(order=0)
foreground = pg.graphics.Group(order=1)

# Spawn car sprites
cars = load.cars(4, 50, window=window, batch=main_batch, group=foreground)

closest_distance = float('inf')
closest_car = None

shapes_test = []





@window.event
def on_draw():
    window.clear()
    main_batch.draw()


def update(dt):
    for obj in cars:
        obj.update(dt)
    for car in cars:
        front_x = car.x + ((car.height / 2) * math.cos(-math.radians(car.rotation)))
        front_y = car.y + ((car.width / 2) * math.sin(-math.radians(car.rotation)))
        shape = pg.shapes.Rectangle(front_x, front_y, 50, 2, batch=main_batch, group=foreground)
        shape.rotation = car.rotation
        ray_origin = 0
        ray_direction = 0
        shapes_test.append(shape)


if __name__ == "__main__":
    # Update the game 120 times per second
    pg.clock.schedule_interval(update, 1 / 120.0)

    # Tell pyglet to do its thing
    pg.app.run()
