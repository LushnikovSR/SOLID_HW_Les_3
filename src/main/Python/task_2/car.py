from vehicle import Vehicle


class Car(Vehicle):
    def get_max_speed(self):
        return self.max_speed * 0.8

    def get_type(self):
        return self.type
