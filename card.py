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
    def ability(self,game):
        card_name = ''
        cd = None
        while cd is None:
            card_name = input("Please give card name to move: ")
            cd = game.get_card(card_name)
            if card_name == 'stop':
                return 0
            if cd is None:
                print('invalid card name')

        print("We are going to move card: {}".format(card_name))
        region_name = input("Which Region to move to: ")


class Cd_A6(Cd):
    region = 'Air'
    strength = 6
    def ability(self,game):
        pass

a=Cd_A6()
print(a.__str__())

