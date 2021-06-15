from Floor import Floor

class Building:
    def __init__(self, bulb, number_of_bulbs, number_of_floors):
        self.floors = []
        for i in range(number_of_floors):
            self.floors.append(Floor(number_of_bulbs, bulb))
        self.change_costs = 0
        self.bulbs_cost = number_of_floors * number_of_bulbs * bulb.cost

    def check_bulbs_state(self):
        for floor in self.floors:
            for bulb in floor.bulbs:
                bulb.check_state()
                if bulb.network_failure is True:
                    floor.network_failure = True
                    floor.failure()
                    break

    def change_broken_bulbs(self):
        for floor in self.floors:
            for bulb in floor:
                if bulb.state is False:
                    bulb.change_bulb()
                    self.change_costs += bulb.cost
