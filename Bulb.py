import random
from enum import Enum


class State(Enum):
    DOWN = 0
    UP = 1
    BEING_REPAIRED = 2


class Bulb:
    def __init__(self, price, min_lifespan, max_lifespan, power, default_failure_chance):
        self.price = price
        self.min_lifespan = min_lifespan
        self.max_lifespan = max_lifespan
        self.default_failure_chance = default_failure_chance
        self.failure_chance = default_failure_chance
        self.default_change_time = 2
        self.change_time_counter = 0
        #power in wats
        self.power = power
        #state=True means that bulb is working
        self.state = State.UP
        self.network_failure = False
        #the final cost of buying and exploitation
        self.cost = price
        self.lifespan = 0

    def change_bulb(self):
        self.lifespan = 0
        self.cost += self.price
        self.state = State.UP
        self.failure_chance = self.default_failure_chance
        print("Wymieniono żarówkę")

    def check_state(self):
        if random.random() <= self.failure_chance and self.state == State.UP:
            if random.random() <= 0.01:
                self.state = State.DOWN
                self.network_failure = True
                print("Nastąpiła awaria całej sieci:"+str(self.lifespan))
            else:
                print("Żarówka się wypaliła:"+str(self.lifespan))
                self.state = State.DOWN

        elif self.state == State.UP:
            self.lifespan += 1
            #0.61zł is an average price of one kWh in Poland
            self.cost = self.cost + self.power * 0.001 * 0.61

            if self.min_lifespan <= self.lifespan < self.max_lifespan:
                self.failure_chance += 0.0001
            elif self.lifespan >= self.max_lifespan:
                self.state = State.DOWN

        elif self.state == State.DOWN:
            self.state = State.BEING_REPAIRED
            self.cost += 200

        elif self.state == State.BEING_REPAIRED:
            self.change_time_counter += 1
            if self.change_time_counter == self.default_change_time:
                self.state = State.UP







