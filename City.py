from math import hypot
from threading import Lock

class City:
    next_id = 0
    id_lock = Lock()

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.id = self.generate_id()

    def generate_id(self):
        with City.id_lock:
            new_id = City.next_id
            City.next_id += 1
        return new_id

    def distance_to(self, city_b):
        return hypot(self.x - city_b.x, self.y - city_b.y)

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_id(self, _id):
        self.id = _id

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_id(self):
        return self.id

    def __str__(self):
        return str(self.id) + "|"
