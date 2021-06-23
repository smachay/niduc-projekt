from Bulb import Bulb
from Building import Building
from Floor import Floor
import random

bulbs_per_floor = 50
number_of_floors = 3
# bulb1 = Bulb(70, 40000, 60000, 5, 0.000003)
# bulb2 = Bulb(36, 15000, 25000, 5.5, 0.000004)
# bulb3 = Bulb(22, 15000, 25000, 7, 0.000005)
# bulb4 = Bulb(23, 15000, 25000, 6, 0.000005)
# bulb5 = Bulb(100, 50000, 70000, 4.5, 0.000001)
# bulb6 = Bulb(84, 50000, 60000, 6, 0.000002)


for i in range(1000):
    print(i)
    building = Building(bulbs_per_floor, number_of_floors)
    price = 0
    lifespan_sum = 0
    for j in range(72000):
        for floor in building.floors:
            floor.check_bulbs_state()

    for floor in building.floors:
        for bulb in floor.bulbs:
            price += bulb.cost

    for t in Bulb.bulbs_lifespan:
        lifespan_sum += t

    avg = lifespan_sum/len(Bulb.bulbs_lifespan)
    file = open("test_50zl.txt", "a")
    file.write(str(price) + " " + str(avg) + "\n")

    Bulb.bulbs_lifespan = []




