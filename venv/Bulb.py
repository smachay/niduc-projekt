import random


class Bulb:
    def __init__(self,model,price,min_lifespan,max_lifespan,power,default_failure_chance):
        self.model = model
        self.price = price
        self.min_lifespan = min_lifespan
        self.max_lifespan = max_lifespan
        self.default_failure_chance = default_failure_chance
        self.failure_chance = default_failure_chance
        #power in wats
        self.power = power
        #state=True means that bulb is working
        self.state = True
        #the final cost of buying and exploitation
        self.cost = price;
        self.lifespan = 0

    def change_bulb(self):
        self.lifespan = 0
        self.cost+=(self.price + 10)
        self.state = True
        self.failure_chance = self.default_failure_chance
        print("Wymieniono żarówkę")

    def chceck_state(self):
        if random.random() <= self.failure_chance and self.state == True:
            if random.random() <= 0.01:
                self.state = False
                print("Nastąpiła awaria całej sieci:"+str(self.lifespan))
            else:
                print("Żarówka się wypaliła:"+str(self.lifespan))
                self.change_bulb()

        elif self.state == True:
            self.lifespan+=1
            #0.61zł is an average price of one kWh in Poland
            self.cost = self.cost + self.power * 0.001 * 0.61

            if self.lifespan >= self.min_lifespan and self.lifespan<self.max_lifespan:
                self.failure_chance+=0.0001
            elif self.lifespan>=self.max_lifespan:
                self.change_bulb()






