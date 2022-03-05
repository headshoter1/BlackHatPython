class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_length(self):
        return (self.x**2 + self.y**2) ** 0.5

    def set_coord(self, x, y):
        self.x = x
        self.y = y

