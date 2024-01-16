# import math

# import pyglet as pg

# class Line(pg.shapes.Line):

#     def __init__(self, car, *args, **kwargs):
#         super(Line, self).__init__(*args, **kwargs)

#         self.car = car

#         self.x = self.car.x
#         self.y = self.car.y

#         self.x2 = self.car.x + (200 * math.cos(-math.radians(self.car.rotation)))
#         self.y2 = self.car.y + (200 * math.sin(-math.radians(self.car.rotation)))



# # def closest_car(car_list: list, output_list: dict, batch, group):
# #     for cur_car in car_list:
# #         x = cur_car.x
# #         y = cur_car.y
# #         x2 = cur_car.x + (200 * math.cos(-math.radians(cur_car.rotation)))
# #         y2 = cur_car.y + (200 * math.sin(-math.radians(cur_car.rotation)))

# #         ray = pg.shapes.Line(x, y, x2, y2, batch=batch, group=group)

# #         output_list[cur_car] = ray