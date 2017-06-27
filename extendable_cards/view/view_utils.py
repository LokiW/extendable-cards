from extendable_cards.lib.cards import Card
from extendable_cards.view.graphics import Rectangle, Point, Text

import pdb

def draw_basic_card(card, dx, dy, h, w, graphwin, image=None):
    """
    Takes a basic card, the top left's coordinates's dx, dy
    the height and width of the card an an image to display (not supported)
    draws card at given coordinates
    """
    left_p = Point(dx,dy)
    right_p = Point(dx+w, dy+h)
    outline = Rectangle(left_p, right_p)

    wraped_text = break_text(card.name, w)
    text_height = wraped_text.count('\n')*0.5
    text_p = Point(dx+w/2, dy+text_height)
    card_t = Text(text_p, wraped_text)
    card_t.setSize(9)

    corner_p = Point(dx, dy)
    one_p = Point(dx+1, dy+1)
    one_r = Rectangle(corner_p, one_p)

    outline.draw(graphwin)
    card_t.draw(graphwin)
    one_r.draw(graphwin)
    return outline


def break_text_naive(text, width):
    """
    Break up text assuming text size 9 based on width.
    Breaks text up mid word, to meet width as best as possible.
    """
    char_per_line = width * 4
    char_in_text = len(text)
    last = 0
    display_text = ""
    for s in range(0, char_in_text/char_per_line):
        line_end = (s+1) * char_per_line
        display_text = display_text + "\n" + text[last : line_end]
        last = line_end

    if len(text) > last:
        display_text = display_text + "\n" + text[last : ]

    return display_text

def break_text(text, width):
    """
    Break up text assuming text size 9 based on width.
    Tries to break text to keep words if possible
    """
    char_per_line = width * 4

    display_text = ""
    cur_line = 0
    words = text.split(' ')
    for word in words:
        if char_per_line - cur_line == 0:
            display_text += '\n'
            cur_line = 0
        
        #If word fits in line then add it
        if len(word) + cur_line < char_per_line:
            display_text += word + " "
            cur_line += len(word) + 1
        
        #If word doesn't fit and we are going to have to break it up
        elif len(word) > char_per_line:
            delim = char_per_line-cur_line
            display_text += word[0:delim]
            for s in range(0, (len(word) - (char_per_line - cur_line))/char_per_line):
                next_delim = delim + (s+1)*char_per_line
                display_text += '\n' +  word[delim:next_delim]
                delim = next_delim
            
            if len(word) > delim:
                display_text += '\n' + word[delim : ]
                cur_line += len(word) - delim

        #If word doesn't fit but we can just add it to next line
        else:
            display_text += '\n' + word
            cur_line = len(word)

    return display_text

