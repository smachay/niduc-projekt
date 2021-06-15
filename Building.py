from Floor import Floor


class Building:
    def __init__(self, bulb, number_of_bulbs, number_of_floors):
        self.floors = []
        for i in range(number_of_floors):
            self.floors.append(Floor(number_of_bulbs, bulb))
