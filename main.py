from Bulb import Bulb
import random

bulb1 = Bulb("Wiz led", 84, 50000, 100000, 6, 0.000001)

for i in range(100000):

    bulb1.check_state()


