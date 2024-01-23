import pyglet as pg


def road(window: pg.window.Window):
    lane_width = 3 * 10
    lane_mid = lane_width / 2

    right_mid = (window.width, window.height / 2)
    top_mid = (window.width / 2, window.height)
    left_mid = (0, window.height / 2)
    bottom_mid = (window.width / 2, 0)

    # coords for middle of each lane
    right_left_lane = (right_mid[0], right_mid[1] + lane_mid)
    right_right_lane = (right_mid[0], right_mid[1] + lane_width + lane_mid)
    top_left_lane = (top_mid[0] - lane_mid, top_mid[1])
    top_right_lane = (top_mid[0] - lane_width - lane_mid, top_mid[1])
    left_left_lane = (left_mid[0], left_mid[1] - lane_mid)
    left_right_lane = (left_mid[0], left_mid[1] - lane_width - lane_mid)
    bottom_left_lane = (bottom_mid[0] + lane_mid, bottom_mid[1])
    bottom_right_lane = (bottom_mid[0] + lane_width + lane_mid, bottom_mid[1])

    return {"right_left_lane": right_left_lane, "right_right_lane": right_right_lane, "top_left_lane": top_left_lane,
            "top_right_lane": top_right_lane, "left_left_lane": left_left_lane, "left_right_lane": left_right_lane,
            "bottom_left_lane": bottom_left_lane, "bottom_right_lane": bottom_right_lane}
