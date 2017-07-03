from extendable_cards.lib.cards import Card
from extendable_cards.view.graphics import Rectangle, Point, Text
import pdb


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


class CardDisplayObject(object):
    def __init__(self, texts, graphwin):
        self.win = graphwin
        self.texts = texts
        self.drawn = False
        self.visible = False
        self.hidden = False
    
    def _setup_display_objects(self, context):
        if self.drawn:
            return False

        dx = context['lx']
        dy = context['ty']
        rx = context['rx']
        by = context['by']

        w = rx - dx
        h = by - dy

        left_p = Point(dx,dy)
        right_p = Point(dx+w, dy+h)
        outline = Rectangle(left_p, right_p)
        if 'fill_color' in self.texts:
            outline.setFill(self.texts.fill_color)
        else:
            outline.setFill("white")
        self.outline = outline

        self.display_texts = []

        if 'center' in self.texts:
            center_p = Point(dx+w/2.0, dy+h/2.0)
            center_t = Text(center_p, self.texts['center'])
            if 'text_color' in self.texts:
                center_t.setTextColor(self.texts['text_color'])
            self.display_texts.append(center_t)

        if 'bottom_left' in self.texts:
            bottom_left_p = Point(dx+max(w/5.0, 0.5), dy+h-max(h/5.0, 0.5))
            bottom_left_t = Text(bottom_left_p, self.texts['bottom_left'])
            if 'text_color' in self.texts:
                bottom_left_t.setTextColor(self.texts['text_color'])
            self.display_texts.append(bottom_left_t)

        if 'top_right' in self.texts:
            top_right_p = Point(dx+w-max(w/5.0, 0.5), dy+max(h/5.0,0.5))
            top_right_t = Text(top_right_p, self.texts['top_right'])
            if 'text_color' in self.texts:
                top_right_t.setTextColor(self.texts['text_color'])
            self.display_texts.append(top_right_t)

        self.drawn = True



    def display_card(self, context):
        """
        Takes a basic card, the top left's coordinates's dx, dy
        the height and width of the card an an image to display (not supported)
        draws card at given coordinates
        """

        if not self.drawn:
            self._setup_display_objects(context)
        else:
            if self.hidden:
                if 'fill_color' in self.texts:
                    self.outline.setFill(self.texts['fill_color'])
                else:
                    self.outline.setFill("white")
                
            self.move_display(context)
            if self.visible and self.hidden:
                for t in self.display_texts:
                    t.draw(self.win)
            elif not self.visible:
                self.outline.draw(self.win)
                for t in self.display_texts:
                    t.draw(self.win)

            self.visible = True
            self.hidden = False


    def is_displayed(self):
        return self.visible


    def undisplay(self):
        if not self.visible:
            return False

        if not self.hidden:
            for t in self.display_texts:
                t.undraw()

        self.outline.undraw()
        self.visible = False

    def display_back(self, context):
        if not self.drawn:
            self._setup_display_objects(context)

        if self.hidden and self.visible:
            return False

        if 'back_color' in self.texts:
            self.outline.setFill(self.texts['back_color'])
        else:
            self.outline.setFill("red")

        self.outline.draw(self.win)

        self.visible = True
        self.hidden = True

    def move_display(self, context):
        cur_x = min(self.outline.getP1().getX(), self.outline.getP2().getX())
        cur_y = min(self.outline.getP1().getY(), self.outline.getP2().getY())

        dx = context['lx'] - cur_x
        dy = context['ty'] - cur_y
       
        self.outline.move(dx, dy)
        for t in self.display_texts:
            t.move(dx, dy)

