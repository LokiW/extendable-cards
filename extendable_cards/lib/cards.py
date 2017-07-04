import random

class Card(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def display_card(self, context=None):
        print '[' + self.name + ']',


class CardOrganizer(object):
    def __init__(self, cards=None, context=None):
        if cards:
            self.cards = cards
        else:
            self.cards = []

        if context:
            self.context = context
        else:
            self.context = {}

    def is_empty(self):
        return len(cards) == 0


    def shuffle(self):
        random.shuffle(self.cards)

    def add_card(self, card):
        self.cards.append(card)

    def add_cards(self, cards):
        self.cards.extend(cards)

    def get_card(self, name):
        for card in self.cards:
            if name == card.name:
                return card

        return None

    def add_card_top(slef, card):
        self.cards.insert(0, card)

    def get_top_cards(self, num):
        return self.cards[:num]

    def remove_top_cards(self, num):
        removed = self.cards[:num]
        del self.cards[:num]
        return removed

    def remove_card(self, name):
        for card in self.cards[:]:
            if name == card.name:
                self.cards.remove(card)
                return card

    def display(self, hidden=False):
        if not hidden:
            if 'label' in self.context:
                print self.context['label'] + ": ",

            for card in self.cards:
                card.display_card()

            print '\n'


    def undisplay(self):
        return False

    def __str__(self):
        output = "{"
        for card in self.cards:
            output += "{0}, ".format(card)

        return output[:len(output) - 2] + "}"

    def __repr__(self):
        return self.__str__()


class CardController(object):
    def __init__(self, deck=None, hand=None, discard=None, in_play=None, selected=None):
        self.deck = deck if deck else CardOrganizer(context={'label':'deck'})
        self.hand = hand if hand else CardOrganizer(context={'label':'hand'})
        self.discard = discard if discard else CardOrganizer(context={'label':'discard'})
        self.in_play = in_play if in_play else CardOrganizer(context={'label':'in play'})
        self.selected = selected if selected else CardOrganizer(context={'label':'selected'})

    def draw(self, num):
        drawn = self.deck.remove_top_cards(num)
        self.hand.add_cards(drawn)

    def play_from_hand(self, name):
        card = self.hand.remove_card(name)
        self.in_play.add_card(card)

    def play_from_deck(self, name):
        card = self.deck.remove_card(name)
        self.in_play.add_card(card)

    def play_top_from_deck(self, num):
        cards = self.deck.remove_top_cards(num)
        self.in_play.add_cards(cards)

    def discard_from_play(self, name):
        card = self.in_play.remove_card(name)
        self.discard.add_card(card)

    def discard_from_hand(self, name):
        card = self.hand.remove_card(name)
        self.discard.add_card(card)

    def discard_from_deck(self, num):
        discarded = self.deck.remove_top_cards(num)
        self.discard.add_cards(discarded)

    def remove_from_deck(self, name):
        """
        removes card from deck entirely, not to hand, discard or other
        """
        self.deck.remove_top_cards(name)

    def bring_back_to_hand(self, name):
        """
        takes given card from discard, puts in hand
        """
        revived = self.discard.remove_card(name)
        self.hand.add_card(revived)

    def bring_back_to_deck(self, name):
        """
        take given card from discard, puts on bottom of deck
        """
        revived = self.discard.remove_card(name)
        self.deck.add_card(revived)

    def bring_back_to_deck_top(self, name):
        """
        take given card from discard, put on top of the deck
        """
        revived = self.discard.remove_card(name)
        self.deck.add_card_top(revived)

    def return_from_play_to_hand(self, name):
        """
        take given card from play, put back into hand
        """
        revived = self.in_play.remove_card(name)
        self.hand.add_card(revived)

    def return_from_play_to_deck_top(self, name):
        revived = self.in_play.remove_card(name)
        self.deck.add_card_top(name)


    def __str__(self):
        output = "{deck: " + str(self.deck)
        output += "\nhand: " + str(self.hand)
        output += "\ndiscard: " + str(self.discard)
        output += "\nplayed: " + str(self.in_play)
        output += "\nselected: " + str(self.selected)
        output += "}"
        return output
 
    def __repr__(self):
        return self.__str__()



