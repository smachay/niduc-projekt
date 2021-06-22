from Bulb import *
import random


class Floor:
    repairing_network_failure_time = 4

    def __init__(self, number_of_bulbs):
        self.bulbs = []
        self.network_failure = False
        self.number_of_bulbs = number_of_bulbs
        self.repairing_time_counter = 0
        self.failure_cost = 0

        for i in range(number_of_bulbs):
            self.bulbs.append(Bulb(75, 50000, 70000, 4.5, 0.000001))
            #self.bulbs.append(Bulb(23, 15000, 25000, 6, 0.000005))
            #self.bulbs.append(Bulb(50, 35000, 60000, 5, 0.000003))

    def check_bulbs_state(self):
        if self.network_failure is False:
            for bulb in self.bulbs:
                bulb.check_state()
                if bulb.network_failure is True:
                    self.failure()
                    bulb.network_failure = False
                    break
        else:
            if self.repairing_time_counter == self.repairing_network_failure_time:
                self.repairing_time_counter = 0
                self.network_failure = False
                # print("Zakonczono naprawe awarii")
                for bulb in self.bulbs:
                    bulb.change_bulb()
            else:
                # print("Trwa naprawa po wystąpieniu awarii")
                self.repairing_time_counter += 1

    def failure(self):
        self.network_failure = True
        for bulb in self.bulbs:
            bulb.state = State.DOWN
