class Cd:
    def display(self):
        return self.region[0] + str(self.strength)
    def __str__(self):
        return self.display()
    def __repr__(self):
        return self.display()

class Cd_A1(Cd):
    region = 'Air'
    strength = 1
    def ability(self,game,card,target_loc):
        pass

class Cd_A6(Cd):
    region = 'Air'
    strength = 6
    def ability(self,game,input):
        pass

a=Cd_A6()
print(a.__str__())

