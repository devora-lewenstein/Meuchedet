class Basic:
    def __init__(self, _cost=20):
        self._cost = _cost 
        self.plan = "basic"
        self.doctors = "Free"
        
    def set_adif_cost(self):
        self._cost = 20

    def get_basic_cost(self):
        return self._cost

    def __str__(self):
        return f"{self.plan}"



class Adif(Basic):
    def __init__(self, _cost=30):
        super().__init__(_cost)
        self.plan = "adif"
        self.dental = "50%"

    def set_adif_cost(self):
        self._cost = 30

    def get_cost_adif(self):
        return self._cost
    
    def __str__(self):
        return f"{self.plan}"

class C(Adif):
    def __init__(self, _cost=40):
        super().__init__(_cost)
        self.plan = "C"
        self.dental = "Free"
        self.therapy= "50%"

    def set_c_cost(self):
        self._cost = 40

    def get_cost_c(self):
        return self._cost
    
    def __str__(self):
        return f"{self.plan}, {self.dental}, {self.therapy}"

# b1 = basic("basic")
# a1 = adif("adif", "dentistry")
# c1 = c("c", "dentistry", "therapy")

# print(b1.get_cost())
# print(a1.get_cost_adif())
# print(c1.get_cost_c())
# print(b1)
# print(a1)
# print(c1)




