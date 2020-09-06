from ClassesOfDuck import *

normal_duck = Duck(who_migrates="west")
mallard_duck = Mallard(who_migrates="south")
decoy_duck = Decoy()

for duck in [normal_duck, mallard_duck, decoy_duck]:
    duck.describe()
    duck.fly()
    duck.call()
