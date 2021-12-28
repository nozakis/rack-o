import random


class Deck:
    def __init__(self, size=60):
        self.cards = list(range(1, size + 1))
        random.shuffle(self.cards)
        self.discards = []

    def deal(self, players):
        for i in range(10):
            for player in players:
                player.rack.append(self.cards.pop())

        self.discards.append(self.cards.pop())

    def discard(self, card):
        self.discards.append(card)

    def draw_card(self):
        card = self.cards.pop()

        if len(self.cards) == 0:
            print('Deck is empty, resetting')
            self.cards = self.discards[:]
            self.cards.reverse()
            self.discards = [self.cards.pop()]

        return card

    def draw_discard(self):
        return self.discards.pop()
