import pyglet as pg

from game import load, resources

# Set up a window
window = pg.window.Window(1000, 1000)
main_batch = pg.graphics.Batch()


# Initialize the car sprite
cars = load.cars(20, window)


@window.event
def on_draw():
    window.clear()

    for car in cars:
        car.draw()


if __name__ == "__main__":
    # Tell pyglet to do its thing
    pg.app.run()
