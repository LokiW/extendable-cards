from enum import Enum
from cards import Card, Deck


class SentinelCard(Card):
    def __init__(self, name, tags, description, quote=None):
        super(SentinelCard, self).__init__(name)
        self.tags = tags
        self.text = description
        self.quote = quote


class SentinelDeck(Deck):
    def __init__(self, cards):
        super(SentinelDeck, self).__init__(name)
        self.play_area = []

    def play_card(card_name):
        for c in self.hand[:]:
            if c.name == card_name:
                self.play_area.append(c)
                self.hand.remove(c)
                return True
        return False

    def discard_from_play(card_name):
        for c in self.play_area[:]:
            if c.name == card_name:
                self.discard.append(c)
                self.play_area.remove(c)
                return True
        return False
   

class Hero:
    def __init__(self, name, max_health, base_power, deck):
        self.name = name
        self.max_health = max_health
        self.current_health = current_health
        self.base_power = base_power
        self.deck = deck


def load_heros_from_file(file):
    f = open(file, "r")

