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

 
