from Bulb import Bulb
from Building import Building
import random

default_change_time = 2
bulbs_per_floor = 50
number_of_floors = 1
bulb1 = Bulb(84, 50000, 100000, 6, 0.000001)
building = Building(bulb1, bulbs_per_floor, number_of_floors)

#for i in range(100000):

