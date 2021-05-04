class Player:
    def __init__(self, name):
        self.name = name
        self.rack = []
        self.game_score = 0
        self.round_score = 0

    '''
    Plays a turn and returns a true/false value to indicate whether or not the player has won during this round
    '''
    def play(self, deck):
        print(f"{self.name}'s turn")
        self.print_rack() # show the player their rack
        print(f'Discard pile: {deck.discards[-1]}') # show the player the discard pile
        draw_action = int(input('Choose 1 to draw the card from the discard pile, choose 2 to draw a new card.\n'))
        while(draw_action != 1 and draw_action !=2):
            draw_action = int(input('Invalid Input!! Please choose 1 to draw the card from the discard pile, choose 2 to draw a new card.\n'))
        if draw_action == 1:
            card = deck.draw_discard()
        elif draw_action == 2:
            card = deck.draw_card()
        print(f'You drew {card}')
        #calling rack card places the card in the correct position in the rack
        discard = self.rack_card(card)
        deck.discards.append(discard)
        #redisplay rack to player after changes
        print('Your updated rack:\n')
        self.print_rack()
        self.round_score = self.score_rack()
        if self.round_score == 75:
            return True

        return False

    def rack_card(self, card):
        position = int(input('Choose slots 1-10 to place card in your rack, or choose 0 to discard. \n'))
        discard = card
        if position > 0:
            position -= 1 # account for the fact that lists are 0-indexed
            discard = self.rack[position]
            self.rack[position] = card

        print(f'You just discarded {discard}')
        return discard

    '''
    Calculates score where each sequential number in the array starting at position 1 = +5 points and a full sequential rack = 50 + 25 for winning
    '''
    def score_rack(self):
        score = 5
        win = True
        for i in range(len(self.rack) - 1):
            if self.rack[i + 1] > self.rack[i]:
                score += 5
            else:
                win = False
                break
        # bonus 25 pts for having all 10 cards in a row
        if win:
            score += 25

        return score

    '''
    Pretty prints the rack.
    '''
    def print_rack(self):
        print('Your rack:')
        self.print_rack_top_bottom()
        # self.print_rack_front_back()

    def print_rack_top_bottom(self):
        for i in reversed(range(len(self.rack))):
            Player.print_card(self.rack[i], i)

    def print_rack_front_back(self):
        for i in range(len(self.rack)):
            Player.print_card(self.rack[i], i)

    def print_card(card, index):
        printed_card = f'{index + 1} '
        if len(printed_card) < 3:
            printed_card += ' '
        for i in range(card - 1):
            printed_card += '-'
        printed_card += str(card)
        print(printed_card)
