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


    def play_move(self, card_name, orientation, loc, input):
        # remove card from hand
        card = card_name
        self.hand_dict.remove(card)
        # insert hand to board
        card_list = self.board[loc]
        played_card = [card,orientation]
        card_list.append(played_card)
        # activate card ability
        card.ability(self,input)

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


hand = {1:[card.Cd_A1()],-1:[card.Cd_A1()]}
a = Game(hand)
a.board[(0,1)] = [card.Cd_A1(),card.Cd_A6()]
a.display_hand()
a.display_board()
