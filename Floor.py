class Floor:
    def __init__(self, number_of_bulbs, bulb):
        self.bulbs = []
        self.network_failure = False
        self.failure_time = 2
        for i in range(number_of_bulbs):
            self.bulbs.append(bulb)

    def failure(self):
        for bulb in self.bulbs:
            bulb.state = False
