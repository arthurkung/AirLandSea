
class Game:
    board_area = [0,1,2]
    player_orientation = [1,-1]

    turn = 0
    def __init__(self, hand_dict, region = ['Air','Land','Sea']):
        self.hand_dict = hand_dict
        self.region_dict = {i:region for i,region in zip(board_area,region)}

    def init_board(self):
        self.board = dict()
        for area, player in zip(self.board_area,self.player_orientation):
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
