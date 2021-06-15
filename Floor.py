from Bulb import *


class Floor:
    repairing_network_failure_time = 10
    failure_repairing_cost = 400
    def __init__(self, number_of_bulbs, bulb):
        self.bulbs = []
        self.network_failure = False
        self.number_of_bulbs = number_of_bulbs
        self.working_bulbs = number_of_bulbs
        self.broken_bulbs = 0
        self.being_changed_bulbs = 0
        self.repairing_time_counter = 0
        self.failure_cost = 0

        for i in range(number_of_bulbs):
            self.bulbs.append(bulb)

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
                    break
            self.working_bulbs = 0
            self.broken_bulbs = 0
            self.being_changed_bulbs = 0
        else:
            if self.repairing_time_counter == self.repairing_network_failure_time:
                self.repairing_time_counter = 0
                self.failure_cost += self.failure_repairing_cost
            else:
                print("Trwa naprawa po wystąpieniu awarii")
                self.repairing_time_counter += 1

    def failure(self):
        self.network_failure = True
        for bulb in self.bulbs:
            bulb.state = State.DOWN
