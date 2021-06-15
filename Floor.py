from Bulb import *
import random


class Floor:
    repairing_network_failure_time = 4
    failure_repairing_cost = 200

    def __init__(self, number_of_bulbs):
        self.bulbs = []
        self.network_failure = False
        self.number_of_bulbs = number_of_bulbs
        self.working_bulbs = number_of_bulbs
        self.broken_bulbs = 0
        self.being_changed_bulbs = 0
        self.repairing_time_counter = 0
        self.failure_cost = 0

        for i in range(number_of_bulbs):
            self.bulbs.append(Bulb(84, 50000, 60000, 6, 0.000002))

    def check_bulbs_state(self):
        if self.network_failure is False:
            for bulb in self.bulbs:
                bulb.check_state()
                if bulb.state == State.UP:
                    self.working_bulbs += 1
                elif bulb.state == State.DOWN:
                    self.broken_bulbs += 1
                else:
                    self.being_changed_bulbs += 1
                if bulb.network_failure is True:
                    self.failure()
                    bulb.network_failure = False
                    break
            # self.working_bulbs = 0
            # self.broken_bulbs = 0
            # self.being_changed_bulbs = 0
        else:
            if self.repairing_time_counter == self.repairing_network_failure_time:
                self.repairing_time_counter = 0
                self.failure_cost += self.failure_repairing_cost
                self.network_failure = False
                print("Zakonczono naprawe awarii")
                for bulb in self.bulbs:
                    bulb.change_bulb()
            else:
                print("Trwa naprawa po wystąpieniu awarii")
                self.repairing_time_counter += 1
                print(self.repairing_time_counter)

    def failure(self):
        self.network_failure = True
        for bulb in self.bulbs:
            bulb.state = State.DOWN

    def print_states(self):
        file = open("file.txt", "a")
        file.write("Dzialajace " + str(self.working_bulbs) + "\n")
