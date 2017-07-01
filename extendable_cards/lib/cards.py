import random

class Card(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

class Deck(object):
    def __init__(self, cards):
        if cards is None:
            self.cards = []
        else:
            self.cards = cards

        self.hand = []
        self.discard = []

    def deck_empty(self):
        if len(self.cards) > 0:
            return False
        return True

    def discard_empty(self):
        if len(self.discard) > 0:
            return False
        return True

    def add_card(self, card):
        self.cards.append(card)

   
    def get_card(self, name):
        for card in self.cards:
            if name == card.name:
                return card

        return None

    def shuffle(self):
        random.shuffle(self.cards)


    def draw(self, num):
        drawn = self.cards[0:num]
        self.hand.extend(drawn)
        del self.cards[0:num]
        return drawn


    def discard_from_hand(self, name):
        for c in self.hand[:]:
            if c.name == name:
                self.discard.append(c)
                self.hand.remove(c)
                return True

        return False

    def discard_from_deck(self, num):
        self.discard.extend(self.cards[0:num])
        del self.cards[0:num]

    def remove_from_deck(self, name):
        """
        removes card from deck entirely, not to hand or discard
        """
        for c in self.cards[:]:
            if c.name == name:
                self.cards.remove(c)
                return True
        return False

    def bring_back_to_hand(self, name):
        """
        takes given card from discard, puts in hand
        """
        for c in self.discard[:]:
            if c.name == name:
                self.hand.append(c)
                self.discard.remove(c)
                return True
        return False

    def bring_back_to_deck(self, name):
        """
        take given card from discard, puts on bottom of deck
        """
        for c in self.discard[:]:
            if c.name == name:
                self.cards.append(c)
                self.discard.remove(c)
                return True
        return False

    def __str__(self):
        output = "{"
        for card in self.cards:
            output += "{0}, ".format(card)

        return output[:len(output) - 2] + "}"
 
    def __repr__(self):
        return self.__str__()
