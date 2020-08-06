class Cd:
    def display(self):
        return self.region[0] + str(self.strength)
    def __str__(self):
        return self.display()
    def __repr__(self):
        return self.display()
    def ability(self,game):
        pass

    def find_self_area(self,game):
        self_name = self.display()
        for area in game.board_area:
            for player in game.player:
                played_card_list = game.board[(area,player)]
                if game.get_card_from_played_card(played_card_list,self_name) is not None:
                    return area


    def get_region_input(self,region_option):
        region_input = None
        while region_input is None and region_input != 'stop':
            region_input = input("Please give region of flip: ")
            if region_input in region_option:
                return region_input
            else:
                print('region not valid')
        return None

    def flip_neighbour(self,game):
        self_area=self.find_self_area(game)
        neighbour_area = self.get_neighbour_area(S5_area)
        neighbour_region = [game.region_dict[area] for area in neighbour_area]
        region_input = self.get_region_input(neighbour_region)
        area_to_flip = game.convert_region_to_area(region_input)
        player = input("Please give player of flip: ")
        game.flip_card(area, player)


class Cd_A1(Cd):
    region = 'Air'
    strength = 1

    def ability(self,game):
        card_name = ''
        cd = None
        while cd is None:
            card_name = input("Please give card name to move: ")
            cd = game.get_card_from_board(card_name)
            if card_name == 'stop':
                return 0
            if cd is None:
                print('invalid card name')

        print("We are going to move card: {}".format(card_name))
        region_name = input("Which Region to move to: ")

class Cd_A2(Cd):
    region = 'Air'
    strength = 2
    ability_is_alive = None
    def ability(self,game):
        if self.ability_is_alive is None:
            self.ability_is_alive = True
        elif self.ability_is_alive == True:
            self.ability_is_alive = False


class Cd_A3(Cd):
    region = 'Air'
    strength = 3
    def ability(self,game):
        self.flip_neighbour(game)


class Cd_A4(Cd):
    region = 'Air'
    strength = 4

class Cd_A5(Cd):
    region = 'Air'
    strength = 5

class Cd_A6(Cd):
    region = 'Air'
    strength = 6


class Cd_S6(Cd):
    region = 'Sea'
    strength = 6

class Cd_L6(Cd):
    region = 'Land'
    strength = 6

