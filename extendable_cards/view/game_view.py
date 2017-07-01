from extendable_cards.view.graphics import Rectangle, Point, Text


class GameOutline(object):
    def __init__(self, window, dx, dy, w, h):
        self.top_y = dy
        self.bottom_y = dy+h
        self.right_x = dx+w
        self.left_x = dx

        discard_p_b = Point(dx+1, self.bottom_y-1)
        discard_p_t = Point(dx + (w / 6.0), self.bottom_y - (h / 3.0))
        discard_text_p = Point((2*dx + (w/6.0))/2, (self.bottom_y - (h / 6.0)))

        self.discard = Rectangle(discard_p_b, discard_p_t)
        self.discard.setFill("grey")

        self.discard_text = Text(discard_text_p, "DISCARD PILE")

        deck_p_b = Point(self.right_x-1, self.bottom_y-1)
        deck_p_t = Point(self.right_x - (w / 6.0), self.bottom_y - (h / 3.0))
        deck_text_p = Point(self.right_x - (w / 12.0), self.bottom_y - (h / 6.0))

        self.deck = Rectangle(deck_p_b, deck_p_t)
        self.deck.setFill("grey")

        self.deck_text = Text(deck_text_p, "DECK")
        
        self.hand = []
        self.in_play = []

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

        p1, p2 = self.get_area_points(play_area)
        lx = min(p1.getX(), p2.getX())
        rx = max(p1.getX(), p2.getX())
        ty = min(p1.getY(), p2.getY())
        by = max(p1.getY(), p2.getY())

        x_unit = (rx - lx) / 50.0
        y_unit = (by - ty) / 50.0

        card_width = min(((rx - lx) / card_num), (by - ty) * (5.0/7.0)) - 2*x_unit
        card_height = min( (by - ty), card_width * (7.0/5.0)) - 2*y_unit

        for card in cards:
            card.display_card(lx + (cur_card*card_width), ty + y_unit, w=(card_width-x_unit), h=card_height)
            cur_card += 1


    def undisplay_play_area(self):
        for card in self.in_play:
            card.undisplay()

    def add_to_hand_area(self, card_view):
        self.hand.append(card_view)

    def add_to_play_area(self, card_view):
        self.in_play.append(card_view)

    def get_area(self, point):
        x = point.getX()
        y = point.getY()

        dis_point_1 = self.discard.getP1()
        dis_point_2 = self.discard.getP2()

        deck_point_1 = self.deck.getP1()
        deck_point_2 = self.deck.getP2()

        dis_x = max(dis_point_1.getX(), dis_point_2.getX())
        dis_y = min(dis_point_1.getY(), dis_point_2.getY())

        deck_x = min(deck_point_1.getX(), deck_point_2.getX())

        if y < dis_y:
            return PlayArea.IN_PLAY
        elif x < dis_x:
            return PlayArea.DISCARD
        elif x > deck_x:
            return PlayArea.DECK
        else:
            return PlayArea.HAND

    def get_area_points(self, area):
        if area == PlayArea.IN_PLAY:
            return (self.discard.getP2(), Point(self.right_x, self.top_y))

        elif area == PlayArea.DISCARD:
            return (self.discard.getP1(), self.discard.getP2())

        elif area == PlayArea.HAND:
            return (self.discard.getP2(), self.deck.getP1())

        elif area == PlayArea.DECK:
            return (self.deck.getP1(), self.deck.getP2())


class PlayArea(object):
    IN_PLAY = "play"
    DISCARD = "discard"
    DECK = "deck"
    HAND = "hand"
