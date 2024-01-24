import pyglet as pg

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
# 3 meters * 10 px
LANE_WIDTH = 3 * 10

lane_mid = LANE_WIDTH / 2

right_mid = (WINDOW_WIDTH, WINDOW_HEIGHT / 2)
top_mid = (WINDOW_WIDTH / 2, WINDOW_HEIGHT)
left_mid = (0, WINDOW_HEIGHT / 2)
bottom_mid = (WINDOW_WIDTH / 2, 0)

# coords for middle of each lane
right_left_lane = (right_mid[0], right_mid[1] + lane_mid)
right_right_lane = (right_mid[0], right_mid[1] + LANE_WIDTH + lane_mid)
top_left_lane = (top_mid[0] - lane_mid, top_mid[1])
top_right_lane = (top_mid[0] - LANE_WIDTH - lane_mid, top_mid[1])
left_left_lane = (left_mid[0], left_mid[1] - lane_mid)
left_right_lane = (left_mid[0], left_mid[1] - LANE_WIDTH - lane_mid)
bottom_left_lane = (bottom_mid[0] + lane_mid, bottom_mid[1])
bottom_right_lane = (bottom_mid[0] + LANE_WIDTH + lane_mid, bottom_mid[1])

spawn_nodes = {"right_left_lane": right_left_lane,
               "right_right_lane": right_right_lane,
               "top_left_lane": top_left_lane,
               "top_right_lane": top_right_lane,
               "left_left_lane": left_left_lane,
               "left_right_lane": left_right_lane,
               "bottom_left_lane": bottom_left_lane,
               "bottom_right_lane": bottom_right_lane}

vert_lane_pos = ((bottom_left_lane[0] - LANE_WIDTH / 2) - LANE_WIDTH * 2, bottom_left_lane[1])
vert_lane_size = {"width": LANE_WIDTH * 4, "height": WINDOW_HEIGHT}
horz_lane_pos = (left_right_lane[0], left_right_lane[1] - LANE_WIDTH / 2)
horz_lane_size = {"width": WINDOW_HEIGHT, "height": LANE_WIDTH * 4}