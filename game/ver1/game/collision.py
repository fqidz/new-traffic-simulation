import pyglet as pg
import math


def bounding_box(obj: pg.sprite.Sprite):
    # because obj.x is at the center

    top_left_x = obj.x + (-obj.width / 2 * math.cos(-math.radians(obj.rotation)))
    top_left_y = obj.y + (-obj.width / 2 * math.sin(-math.radians(obj.rotation)))

    top_right_x = 0
    top_right_y = 0

    bot_right_x = 0
    bot_right_y = 0

    bot_left_x = 0
    bot_left_y = 0


    # return clockwise
    return ((top_left_x, top_left_y), (top_right_x, top_right_y), (bot_right_x, bot_right_y), (bot_left_x, bot_left_y))


def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return False

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return (x, y)
