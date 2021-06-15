from Bulb import Bulb
from Building import Building
from Floor import Floor
import random

bulbs_per_floor = 50
number_of_floors = 3
# bulb1 = Bulb(70, 50000, 60000, 5, 0.000003)
# bulb2 = Bulb(36, 15000, 25000, 5.5, 0.000004)
# bulb3 = Bulb(22, 15000, 25000, 7, 0.000005)
# bulb4 = Bulb(23, 15000, 25000, 4, 0.000006)
# bulb5 = Bulb(100, 60000, 70000, 4.5, 0.000001)
#bulb6 = Bulb(84, 50000, 60000, 6, 0.000002)
#building = Building(bulbs_per_floor, number_of_floors)
price = 0
floor = Floor(150)

for i in range(65000):
    floor.check_bulbs_state()

for b in floor.bulbs:
    price += b.cost

print("\n",price)



