import pyglet as pg


def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2


# Tell pyglet where to find the resources
pg.resource.path = ['../resources']
pg.resource.reindex()

# Load the main resources
car_image = pg.resource.image("car3.png")
center_image(car_image)

road_image = pg.resource.image("road.png")
center_image(road_image)
