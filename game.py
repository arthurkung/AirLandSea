import card
class Game:
    board_area = [0,1,2]
    player = [1,-1]

    turn = 0
    def __init__(self, hand_dict, region = ['Air','Land','Sea']):
        self.hand_dict = hand_dict
        self.region_dict = {i:region for i,region in zip(self.board_area,region)}
        self.init_board()

    def init_board(self):
        self.board = dict()
        for area in self.board_area:
            for player in self.player:
                self.board[(area,player)] = []

    def get_card_from_list(self,card_name,list):
        for card in list:
            if card.display()==card_name:
                return card
        return None

    def play_move(self, card_name, orientation, loc):
        # get player
        player = self.get_turn_player()
        # get hand list
        hand_list = self.hand_dict[player]
        # card to play
        cd = self.get_card_from_list(card_name, hand_list)
        if cd is None:
            print("card is not found from hand")
        # remove card from hand
        hand_list.remove(cd)
        # check any restricting abilities
        if self.check_active_abilities(card_name, orientation, loc) == True:
            return 0

        # insert hand to board
        card_list = self.board[loc]
        played_card = (card,orientation)
        card_list.append(played_card)
        # activate card ability
        if orientation == 1 and cd.ability_type='one-off':
            card.ability(self,input)

    def check_active_abilities(card_name, orientation, loc):
        result = ''
        for loc,played_card in self.board.items():
            cd, side = played_card
            if side == 1 and cd.ability_type == 'Continuous':
                result = cd.ability(card_name, orientation, loc)
        return result

    def get_turn_player(self):
        if turn%2 == 0:
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
        card_to_flip  = card_list[-1]
        cd, orig_side = card_to_flip
        new_side = orig_side * -1
        flipped_card = (cd,new_side)
        card_list.pop() # remove card to be flipped
        card_list.append(flipped_card) # add flipped card
        if new_side == 1:
            cd.ability(self)
        return 1

    def get_card(self,name):
        for loc,card_list in self.board.items():
            for play_card in card_list:
                cd, orientation = play_card
                if cd.display() == name:
                    # area,player = loc
                    return cd
        return None

hand = {1:[card.Cd_A1()],-1:[card.Cd_A1()]}
a = Game(hand)
a.board[(0,1)] = [(card.Cd_A1(),1),(card.Cd_A6(),-1)]
# a.display_hand()
# a.display_board()
c = a.get_card('A1')
c.ability(a)
