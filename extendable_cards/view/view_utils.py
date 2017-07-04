from extendable_cards.lib.cards import Card
from extendable_cards.view.graphics import Rectangle, Point
from tkinter import Text, Frame
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

        lx = context['lx']
        ty = context['ty']
        rx = context['rx']
        by = context['by']

        w = rx - lx
        h = by - ty

        #Frame test
        self.frame = Frame(self.win, height=h, width=w)
        self.frame.config(borderwidth=4, padx=2, relief="groove")
        self.frame.grid_propagate(False)
        if 'fill_color' in self.texts:
            self.frame.config(background=self.texts['fill_color'])
        else:
            self.frame.config(background="white")
        #self.frame.place(x=lx, y=ty)
        
        self.display_texts = []
        for t in self.texts:
            self.display_texts.append(TextWrap(t, frame=self.frame))

        self.drawn = True


    def _add_text(self, x, y, context, text):
        mod_text = break_text(text, context['rx'] - context['lx'])
        text_height = mod_text.count('\n') 
        new_text = Text(self.frame, height=1, width=20) 
        new_text.config(wrap='word')
        new_text.insert('end', text)
        
        #if 'text_color' in self.texts:
        #    new_text.setTextColor(self.texts['text_color'])
        self.display_texts.append(TextWrap(new_text, x, y, self.frame))



    def display_card(self, context):
        """
        Takes a basic card, the top left's coordinates's dx, dy
        the height and width of the card an an image to display (not supported)
        draws card at given coordinates
        """

        if not self.drawn:
            self._setup_display_objects(context)
    
        if self.hidden:
            if 'fill_color' in self.texts:
                self.frame.config(background=self.texts['fill_color'])
            else:
                self.frame.config(background="white")
            
        self.move_display(context)
        if self.visible and self.hidden:
            for t in self.display_texts:
                t.draw(self.frame)
        elif not self.visible:
            self.frame.place(x=context['lx'], y=context['ty'])
            for t in self.display_texts:
                t.draw(self.frame)

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

        self.frame.place_forget()
        self.visible = False

    def display_back(self, context):
        if not self.drawn:
            self._setup_display_objects(context)

        if self.hidden and self.visible:
            return False

        if 'back_color' in self.texts:
            self.frame.config(background=self.texts['back_color'])
        else:
            self.frame.config(background="red")

        self.frame.place(x=context['lx'], y=context['ty'])

        self.visible = True
        self.hidden = True

    def move_display(self, context):
        cur_x = self.frame.winfo_x()
        cur_y = self.frame.winfo_y()

        dx = context['lx'] - cur_x
        dy = context['ty'] - cur_y
      
        self.frame.place(x=cur_x, y=cur_y)
        for t in self.display_texts:
            t.draw(self.frame)


class TextWrap(object):
    def __init__(self, configs, frame):
        self.frame = frame
        
        new_text = Text(self.frame, height=4, width=configs['w']) 
        new_text.config(wrap='word')
        new_text.insert('end', configs['text'])
        self.text = new_text

        self.r = configs['r']
        self.c = configs['c']
        self.w = configs['w']
        self.s = configs['s']
        if 'weight' in configs:
            self.weight = configs['weight']
        else:
            self.weight = 1


    def undraw(self):
        #self.text.place_forget()
        self.text.grid_remove()

    def draw(self, graphwin):
        #self.text.place(x=self.x, y=self.y)
        self.text.grid(row=self.r, column=self.c, sticky=self.s)
        self.text.grid_rowconfigure(index=self.r, weight=self.weight)

        return True

    def move(self, dx, dy):
        return False
        """
        self.x = r
        self.y = c
        self.y = w
        self.s = s
        #self.text.grid(row=r, column=c, weight=w, sticky=self.s)
        #self.text.place(x=self.x, y=self.y)
        """

