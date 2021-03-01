class basic:
    def __init__(self, plan):
        self._cost = None 
        self.plan = plan

    def set_cost(self, value):
        self._cost = value

    def get_cost(self):
        return self._cost

    def __str__(self):
        return f"{self.plan}"



class adif(basic):
    def __init__(self, plan, coverage):
        super().__init__(plan)
        self.coverage = coverage 

    def set_cost_adif(self, value):
        self._cost = value

    def get_cost_adif(self):
        return self._cost
    
    def __str__(self):
        return f"{self.plan}, {self.coverage}"

class c(adif):
    def __init__(self, plan, coverage, additional):
        super().__init__(plan, coverage)
        self.additional = additional

    def set_cost_c(self, value):
        self._cost = value

    def get_cost_c(self):
        return self._cost
    
    def __str__(self):
        return f"{self.plan}, {self.coverage}, {self.additional}"

b1 = basic("basic")
a1 = adif("adif", "dentistry")
c1 = c("c", "dentistry", "therapy")

b1.set_cost(20)
a1.set_cost_adif(30)
c1.set_cost_c(40)
print(b1.get_cost())
print(a1.get_cost_adif())
print(c1.get_cost_c())
print(b1)
print(a1)
print(c1)




