import pyglet as pg


class PhysicalObject(pg.sprite.Sprite):
    """A sprite with physical properties such as velocity"""

    def __init__(self, window, *args, **kwargs):
        super(PhysicalObject, self).__init__(*args, **kwargs)

        # In addition to position, we have velocity
        self.velocity_x, self.velocity_y = 0.0, 0.0

        # Window to get width & height
        self.window = window

    def update(self, dt):
        """This method should be called every frame."""

        # Update position according to velocity and time
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        # Delete self if out of bounds
        self.check_bounds()

    def check_bounds(self):
        """Delete self if out of bounds"""
        min_x = -self.image.width / 2
        min_y = -self.image.height / 2
        max_x = self.window.width + self.image.width / 2
        max_y = self.window.height + self.image.height / 2

        if ((self.x < min_x) or
                (self.x > max_x) or
                (self.y < min_y) or
                (self.y > max_y)):
            self.delete()
