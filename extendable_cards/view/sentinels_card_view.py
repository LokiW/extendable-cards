from extendable_cards.view.view_utils import break_text, CardDisplayObject
from extendable_cards.view.card_view import CardView
from extendable_cards.view.graphics import Rectangle, Point, Text
from extendable_cards.lib.sentinels import SentinelCard, SentinelTag
from extendable_cards.data.grand_warlord_voss_hero import get_grand_warlord_voss_hero

class SentinelCardView(SentinelCard):
    def __init__(self, graphwin, card):
        super(SentinelCardView, self).__init__(card)
        self.win = graphwin
        
        specs = {"center_left": self.get_tags_str(),
                "top_left": self.name,
                "bottom_left": self.description
                }
   
        configs = []
        name_h = break_text(self.name, 15).count('\n') + 1
        configs.append({'text': self.name, 'ts': 12, 'r':0, 'c':0, 's':'W', 'h':name_h, 'w':15})
        tag_h = break_text(self.get_tags_str(), 20).count('\n') + 1 
        configs.append({'text': self.get_tags_str(), 'ts':9, 'r':1, 'c':0, 's':'W', 'h':tag_h, 'w':20})
        desc_h = break_text(self.description, 30).count('\n') + 1
        configs.append({'text': self.description, 'ts':9, 'r':2, 'c':0, 's':'S', 'h':desc_h+2, 'w':20, 'rw': 5, 'cw':3})
        if SentinelTag.TARGET in self.tags:
            configs.append({'text': self.current_health, 'r':0, 'c':1, 's':'W', 'h':1, 'w':7, 'cw': 5})

        self.display = CardDisplayObject(configs, graphwin)        
    
    def display_card(self, context):
        self.display.display_card(context)

    def is_displayed(self):
        return self.display.is_displayed()

    def undisplay(self):
        self.display.undisplay()

    def display_back(self, context):
        self.display.display_back(context)


def get_grand_warlord_voss_hero_view(graphwin):
    cards = get_grand_warlord_voss_hero()
    view_cards = []
    for card in cards:
        view_cards.append(SentinelCardView(graphwin, card))
    return view_cards
