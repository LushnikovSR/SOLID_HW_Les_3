from vehicle import Vehicle


class SpeedCalculation:
    def calculate_allowed_speed(self, vehicle: Vehicle):
        return vehicle.get_max_speed()
