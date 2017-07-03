from extendable_cards.view.view_utils import break_text, CardDisplayObject
from extendable_cards.view.card_view import CardView
from extendable_cards.view.graphics import Rectangle, Point, Text
from extendable_cards.lib.sentinels import SentinelCard


class SentinelCardView(SentinelCard):
    def __init__(self, graphwin, name, description, tags=[], quote=None, max_health=None):
        super(SentinelCardView, self).__init__(name, description, tags, quote, max_health)
        self.win = graphwin
        
        specs = {"center": self.get_tags_str(),
                "bottom_left": suitnum,
                "bottom_right": suitnum,
                "top_right": suitnum,
                "top_left": suitnum}
        self.display = CardDisplayObject(specs, graphwin)        
    
    def display_card(self, context):
        self.display.display_card(context)

    def is_displayed(self):
        return self.display.is_displayed()

    def undisplay(self):
        self.display.undisplay()

    def display_back(self, context):
        self.display.display_back(context)
