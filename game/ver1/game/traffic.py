class TrafficLight:
    def __init__(self, lane_name, x=0, y=0):
        self.x = x
        self.y = y
        self.rotation = 0
        self.velocity_magnitude = 0
        self.lane_name = lane_name
        self.width = 1
        self.height = 1

    def update(self, dt):
        pass
