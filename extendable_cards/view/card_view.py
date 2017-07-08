from extendable_cards.view.view_utils import break_text, CardDisplayObject 
from extendable_cards.view.graphics import Rectangle, Point, Text
from extendable_cards.lib.cards import Card, CardOrganizer

import time


class CardView(Card):
    def __init__(self, name, graphwin):
        super(CardView, self).__init__(name)
        specs = {"center": self.name}
        config = [{'text': self.name, 'r':1, 'c':1, 's':'', 'w':3}]
        self.display = CardDisplayObject(config, graphwin)        
    
    def display_card(self, context):
        self.display.display_card(context)

    def is_displayed(self):
        return self.display.is_displayed()

    def undisplay(self):
        self.display.undisplay()

    def display_back(self, context):
        self.display.display_back(context)


class CardOrganizerDisplay(CardOrganizer):
    def __init__(self, cards, graphwin, context):
        super(CardOrganizerDisplay, self).__init__(cards)
        self.win = graphwin
        self.context = context
    
    def display(self, hidden=False):
        card_num = len(self.cards)
        if card_num == 0:
            return False
        cur_card = 0

        lx = self.context['lx']
        rx = self.context['rx']
        ty = self.context['ty']
        by = self.context['by']

        y_unit = (by - ty) / 50.0

        if 'card_height' not in self.context:
            self.context['card_height'] = by - ty - 2*y_unit
        
        if 'card_width' not in self.context:
            self.context['card_width'] = self.context['card_height'] * (5.0/7.0)

        x_unit = ((rx - self.context['card_width']) - lx)/card_num
        def draw_callback(cur_card, lx, ty, context, x_unit, y_unit, cards):
            if cur_card >= len(cards):
                return True

            card = cards[cur_card]

            cc = {'lx': lx + (cur_card*x_unit),
                  'ty': ty + y_unit}
            cc['rx'] = cc['lx'] + context['card_width']
            cc['by'] = cc['ty'] + context['card_height']
            if hidden:
                card.display_back(cc)
            else:
                card.display_card(cc)

            cur_card += 1
            self.win.after_idle(lambda: draw_callback(cur_card, lx, ty, context, x_unit, y_unit, cards))

        self.win.after_idle(lambda: draw_callback(cur_card, lx, ty, self.context, x_unit, y_unit, self.cards))


    def undisplay(self):
        for card in self.cards:
            if not card:
                print self.cards
                print len(self.cards)
            elif type(card) is str:
                print card + " is string"
                print self.cards
            card.undisplay()
    

    def update_context(self, context):
        self.context = context


