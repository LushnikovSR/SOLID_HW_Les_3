from vehicle import Vehicle


class Bus(Vehicle):
    def get_max_speed(self):
        return self.max_speed * 0.6

    def get_type(self):
        return self.type
