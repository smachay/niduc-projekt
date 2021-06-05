class Building:
    def __init__(self, bulbs, floors):
        self.bulbs = bulbs
        self.floors = floors
        self.change_costs = 0
        self.bulbs_cost = 0
        for bulb in bulbs:
            self.bulbs_cost += bulb.cost
        self.bulbs_cost *= floors

    def check_bulbs_state(self):
        for bulb in self.bulbs:
            bulb.check_state()

    def get_broken_bulbs(self):
        broken_bulbs = []
        for bulb in self.bulbs:
            if bulb.state is False:
                broken_bulbs.append(bulb)
        return broken_bulbs

    def change_broken_bulbs(self):
        broken_bulbs = self.get_broken_bulbs()
        for bulb in self.bulbs:
            if bulb in broken_bulbs:
                bulb.change_bulb()
                self.change_costs += bulb.cost