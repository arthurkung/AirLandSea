import card
class Game:
    board_area = [0,1,2]
    player = [1,-1]

    turn = 0
    def __init__(self, hand_dict, region = ['Air','Land','Sea']):
        self.hand_dict = hand_dict.copy()
        self.region_dict = {i:region for i,region in zip(self.board_area,region)}
        self.init_board()

    def convert_region_to_area(self, region_name):
        for area, region in self.region_dict.items():
            if region == region_name:
                return area
        return None

    def init_board(self):
        self.board = dict()
        for area in self.board_area:
            for player in self.player:
                self.board[(area,player)] = []

    def get_card_from_list(self,card_name,list):
        for cd in list:
            if cd.display()==card_name:
                return cd
        return None

    def play_move(self, card_name, orientation, area):

        if area not in self.board_area:
            area = self.convert_region_to_area(area)
        if area not in self.board_area:
            print('Area is invalid')
            return 'Area is invalid'

        player = self.get_turn_player()
        loc = (area, player)
        # get hand list
        hand_list = self.hand_dict[player]
        # card to play
        cd = self.get_card_from_list(card_name, hand_list)
        if cd is None:
            print("card is not found from hand")

        if not self.play_card_is_valid(cd,orientation,loc,player):
            print("Move is invalid")
            return 'Move is invalid'

        # remove card from hand
        hand_list.remove(cd)

        self.turn = self.turn + 1
        # check if it is discarded by active abilities
        if self.discard_by_active_abilities(card_name, orientation, loc) == True:
            return 'Card is discarded'

        # insert hand to board
        card_list = self.board[loc]
        played_card = (cd,orientation)
        card_list.append(played_card)
        # activate card ability
        if orientation == 1:
            cd.ability(self)

    def play_card_is_valid(self,cd,orientation,loc,player):
        area,loc_player = loc
        if loc_player != player:
            return False
        if orientation == -1:
            return True
        if cd.region == self.region_dict[area]:
            return True
        if self.is_A4_active(player) == True and cd.strength <=3:
            return True
        if self.is_A2_active(player) == True:
            return True
        return False

    def is_A4_active(self, player):
        for area in self.board_area:
            played_card_list = self.board[(area,player)]
            if self.get_active_card_from_played_card(played_card_list,'A4') is not None:
                return True
        return False

    def is_A5_active(self):
        for area in self.board_area:
            for player in self.player:
                played_card_list = self.board[(area,player)]
                if self.get_active_card_from_played_card(played_card_list,'A5') is not None:
                    return True
        return False

    def is_A2_active(self, player):
        for area in self.board_area:
            played_card_list = self.board[(area,player)]
            cd = self.get_active_card_from_played_card(played_card_list,'A2')
            if cd is not None and cd.ability_is_alive == True:
                return True
            else:
                return False
        return False


    def get_card_from_played_card(self, played_card_list, card_name):
        for played_card in played_card_list:
            cd,orientation = played_card
            if cd.display() == card_name:
                return played_card
        return None

    def get_active_card_from_played_card(self, played_card_list, card_name):
        played_card = self.get_card_from_played_card(played_card_list, card_name)
        if played_card is None:
            return None
        cd,orientation = played_card
        if orientation == 1:
            return cd
        else:
            return None

    def get_neighbour_area(self,area):
        neighbour = [x for x in self.board_area if abs(x-area)==1]
        return neighbour

    def count_cards_in_board_area(self, area):
        count = 0
        for player in self.player:
            count = count + len(self.board[(area,player)])
        return count

    def discard_by_active_abilities(self,card_name, orientation, loc):
        # is discarded by A5
        if orientation == -1 and self.is_A5_active() == True:
            return True

        # is discarded by S5
        S5_card = self.get_card_from_board('S5')

        if S5_card is not None:
            S5_area = S5_card.find_self_area(self)
            played_area = loc[0]
            S5_neighbour = self.get_neighbour_area(S5_area)
            if played_area in S5_neighbour:
                if count_cards_in_board_area(played_area)>=3:
                    return True

        return False

    def get_turn_player(self):
        if self.turn%2 == 0:
            return 1
        else:
            return -1

    def display_hand(self):
        for player, hand_list in self.hand_dict.items():
            s = 'player'+str(player)+': '
            s = s + hand_list.__str__()
            print(s)


    def display_board(self):
        for area, player in self.board.keys():
            s = self.region_dict[area] + ' p' +str(player)+': '
            card_list = self.board[(area,player)]
            s = s+card_list.__str__()
            print(s)

    def flip_card(self, area, player):
        card_list = self.board[(area,player)]
        if len(card_list) == 0:
            return 'there is no card there'
        card_to_flip  = card_list[-1]
        cd, orig_side = card_to_flip
        new_side = orig_side * -1
        flipped_card = (cd,new_side)
        card_list.pop() # remove card to be flipped
        card_list.append(flipped_card) # add flipped card
        if new_side == 1:
            cd.ability(self)
        return 1

    def get_card_from_board(self,name):
        for loc,card_list in self.board.items():
            for play_card in card_list:
                cd, orientation = play_card
                if cd.display() == name:
                    # area,player = loc
                    return cd
        return None

hand = {1:[card.Cd_A6(),card.Cd_A4(),card.Cd_A2(),card.Cd_L2()],-1:[card.Cd_A5(),card.Cd_A1(),card.Cd_A3()]}
# a = Game(hand)
# a.play_move( 'A6', -1, 1)
# a.play_move( 'A5', 1, 0)
# a.play_move( 'L2', 1, 1)
# a.play_move( 'A5', 1, 0)
# a.play_move( 'A4', -1, 0)
# a.display_hand()
# a.display_board()

# c = a.get_card_from_board('A6')
# d = c.find_self_area(a)
# print(d)
# c.ability(a)
