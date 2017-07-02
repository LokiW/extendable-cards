from extendable_cards.view.graphics import Rectangle, Point, Text
from tkinter import Button


class GameOutline(object):
    def __init__(self, window, dx, dy, w, h):
        self.top_y = dy
        self.bottom_y = dy+h
        self.right_x = dx+w
        self.left_x = dx

        self.discard_end_x = dx + (w/6.0)
        self.discard_top_y = self.bottom_y - (h/3.0)

        discard_p_b = Point(dx+1, self.bottom_y-1)
        discard_p_t = Point(self.discard_end_x, self.discard_top_y)
        discard_text_p = Point((2*dx + (w/6.0))/2, (self.bottom_y - (h / 6.0)))

        self.discard = Rectangle(discard_p_b, discard_p_t)
        self.discard.setFill("grey")

        self.discard_text = Text(discard_text_p, "DISCARD PILE")

        self.deck_begin_x = self.right_x - (w/6.0)

        deck_p_b = Point(self.right_x-1, self.bottom_y-1)
        deck_p_t = Point(self.deck_begin_x, self.bottom_y - (h / 3.0))
        deck_text_p = Point(self.right_x - (w / 12.0), self.bottom_y - (h / 6.0))

        self.deck = Rectangle(deck_p_b, deck_p_t)
        self.deck.setFill("grey")

        self.deck_text = Text(deck_text_p, "DECK")
        
        self.hand = []
        self.in_play = []
        self.selected = []

        self.win = window


    def display_outline(self):
        self.discard.draw(self.win)
        self.deck.draw(self.win)


    def display_outline_with_labels(self):
        self.display_outline()
        self.deck_text.draw(self.win)
        self.discard_text.draw(self.win)


    def undisplay_labels(self):
        self.deck_text.undraw()
        self.discard_text.undraw()

    
    def display_hand_area(self):
        self._display_card_list(self.hand, PlayArea.HAND)

    def undisplay_hand_area(self):
        for card in self.hand:
            card.undisplay()

    def display_play_area(self):
        self._display_card_list(self.in_play, PlayArea.IN_PLAY)

    def _display_card_list(self, cards, play_area):
        card_num = len(cards)
        if card_num == 0:
            return False
        cur_card = 0

        lx, by, rx, ty = self.get_area_points(play_area)

        y_unit = (by - ty) / 50.0

        card_height = by - ty - 2*y_unit
        card_width = card_height * (5.0/7.0)

        x_unit = ((rx - card_width) - lx)/card_num


        for card in cards:
            card.display_card(lx + (cur_card*x_unit), ty + y_unit, w=card_width, h=card_height)
            cur_card += 1


    def undisplay_play_area(self):
        for card in self.in_play:
            card.undisplay()

    def select_cards(self, cards, play_area):
        self.selected.append({'card': card_type(card), 'origin': play_area})

    def select_card(self, card, play_area):
        for card in cards:
            if play_area == PlayArea.HAND:
                for hc in self.hand[:]:
                    if hc.card.name == card.card.name:
                        self.selected.append({'card':hc, 'origin': play_area})
                        self.hand.remove(hc)
                        return
            elif play_area == PlayArea.IN_PLAY:
                for ipc in self.in_play[:]:
                    if ipc.card.name == card.card.name:
                        self.selected.append({'card':ipc, 'origin': play_area})
                        self.in_play.remove(ipc)
                        return
            elif play_area == PlayArea.DECK or play_area == PlayArea.DISCARD:
                self.selected.append({'card': card_type(card), 'origin': play_area})
            elif play_area == PlayArea.SELECTION:
                for sc, origin in self.selected:
                    if sc.card.name == card.card.name:
                        self.return_selections()
                        self.selected.append({'card': sc, 'origin': origin})
                        return
                

    def return_selections(self):
        self.undisplay_selection()
        for card in self.selected[:]:
            if card['origin'] == PlayArea.HAND:
                self.hand.append(card)
                self.selected.remove(card)
            elif card['origin'] == PlayArea.IN_PLAY:
                self.in_play.append(card)
                self.selected.remove(card)
            else:
                self.selected.remove(card)


    def display_selection(self):
        self._display_card_list([item['card'] for item in self.selected], PlayArea.SELECTION)

    def undisplay_selection(self):
        for card in self.selected:
            card.undisplay()

    def add_to_hand_area(self, card_view):
        self.hand.append(card_view)

    def add_to_play_area(self, card_view):
        self.in_play.append(card_view)

    def get_card_at_point(self, point, area):
        x = point.getX()
        y = point.getY()

        if area == PlayArea.HAND:
            last_seen = None
            for card in self.hand:
                lx = min(card.card.getP1().getX(), card.card.getP2().getX())
                if lx < x:
                    last_seen = card
                else:
                    return last_seen

            return last_seen


    def get_area(self, point):
        x = point.getX()
        y = point.getY()

        if y < self.discard_top_y:
            return PlayArea.IN_PLAY
        elif x < self.discard_end_x:
            return PlayArea.DISCARD
        elif x > self.deck_begin_x:
            return PlayArea.DECK
        elif len(self.selected) > 0:
            
            return PlayArea.HAND
        else:
            return PlayArea.HAND

    def get_area_points(self, area):
        if area == PlayArea.IN_PLAY:
            return (self.left_x, self.discard_top_y, self.right_x, self.top_y)

        elif area == PlayArea.DISCARD:
            return (self.left_x, self.bottom_y, self.discard_end_x, self.discard_top_y)

        elif area == PlayArea.HAND:
            return (self.discard_end_x, self.bottom_y, self.deck_begin_x, self.discard_top_y)

        elif area == PlayArea.DECK:
            return (self.deck_begin_x, self.bottom_y, self.right_x, self.discard_top_y)

        elif area == PlayArea.SELECTION:
            return (self.discard_end_x, self.bottom_y - (self.bottom_y - self.discard_top_y)*(2.0/3.0),
                    self.deck_begin_x, self.bottom_y - (self.bottom_y - self.discard_top_y)*(5.0/3.0))


class PlayArea(object):
    IN_PLAY = "play"
    DISCARD = "discard"
    DECK = "deck"
    HAND = "hand"
    SELECTION = "selection"
