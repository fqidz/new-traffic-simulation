import pyglet as pg


def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2


# Tell pyglet where to find the resources
pg.resource.path = ['../resources']
pg.resource.reindex()

# Load the main resources and get them to draw centered
car_image = pg.resource.image("car2.png")
center_image(car_image)
