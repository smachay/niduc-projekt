class Floor:
    def __init__(self, number_of_bulbs, bulb):
        self.bulbs = []
        self.network_failure = False
        for i in range(number_of_bulbs):
            self.bulbs.append(bulb)

