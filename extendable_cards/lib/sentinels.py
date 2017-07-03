from enum import Enum
from cards import Card, Deck


class SentinelCard(Card):
    def __init__(self, name, description, tags=[], quote=None, max_health=None):
        super(SentinelCard, self).__init__(name)
        self.tags = tags
        self.text = description
        self.quote = quote
        self.max_health = max_health
        self.current_health = max_health

    def display_card(self):
        

    def undisplay(self):
        return False

    def get_tags_str(self):
        tag_str = ""
        for tag in self.tags:
            if not tag == SentinelTag.TARGET:
                tag_str += tag ", "
        if len(tag_str) > 0:
            tag_str = tag_str[:len(tag_str)-2]

        return tag_str

class Hero(Card):
    def __init__(self, name, max_health, base_power, deck):
        super(Hero, self).__init__(name)
        self.max_health = max_health
        self.current_health = max_health
        self.base_power = base_power
        self.deck = deck


class SentinelTag(object):
    ONGOING = 'Ongoing'
    EQUIPMENT = 'Equipment'
    ONE_SHOT = 'One Shot'
    TARGET = ''
    RELIC = 'Relic'
    CONSTRUCT = 'Construct'
    GOLEMN = 'Golemn'
    DEVICE = 'Device'
    BURST = 'Burst'
    MINION = 'Minion'
    HERO = 'Hero'
    SURVIVOR = 'Survivor'
    GENE_SERUM = 'Gene-Serum'
    

def load_heros_from_file(file):
    f = open(file, "r")

