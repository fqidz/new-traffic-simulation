import pyglet as pg

from game import load

# Set up a window
window = pg.window.Window(1000, 1000)
main_batch = pg.graphics.Batch()

# Initialize the car sprite
cars = load.cars(20, window, main_batch)


@window.event
def on_draw():
    window.clear()
    main_batch.draw()

def update(dt):
    for obj in cars:
        obj.update(dt)


if __name__ == "__main__":
    # Update the game 120 times per second
    pg.clock.schedule_interval(update, 1 / 120.0)

    # Tell pyglet to do its thing
    pg.app.run()
