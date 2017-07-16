from extendable_cards.lib.cards import Card
from extendable_cards.view.view_utils import CardDisplayObject
from tkinter import Label
from PIL import Image, ImageTk
import pdb


class ImageDisplayObject(CardDisplayObject):
    def __init__(self, texts, graphwin, f_image, b_image):
        super(ImageDisplayObject, self).__init__(texts, graphwin)
        self.f_image = f_image

        self.b_image = b_image

    def _setup_display_objects(self, context):
        if self.drawn:
            return False

        self.last_context = context

        lx = context['lx']
        ty = context['ty']
        rx = context['rx']
        by = context['by']

        w = rx - lx
        h = by - ty

        size = w, h
        fi = Image.open(self.f_image)
        bi = Image.open(self.b_image)

        fi.thumbnail(size, Image.ANTIALIAS)
        self.f_photo = ImageTk.PhotoImage(fi)

        bi.thumbnail(size, Image.ANTIALIAS)
        self.b_photo = ImageTk.PhotoImage(bi)

        self.f_label = Label(self.win, height=h, width=w, relief='groove', image=self.f_photo)
        self.f_label.image = self.f_photo
        self.f_label.bind('<Button-1>', self._enlarge)

        self.b_label = Label(self.win, height=h, width=w, relief='groove', image=self.b_photo)
        self.b_label.image = self.b_photo
        self.b_label.bind('<Button-1>', self._enlarge)

        self.drawn = True


    def display_card(self, context):
        """
        Takes a basic card, the top left's coordinates's dx, dy
        the height and width of the card an an image to display (not supported)
        draws card at given coordinates
        """

        if not self.drawn:
            self._setup_display_objects(context)
    
        if self.hidden and self.visible:
            self.b_label.place_forget()
            self.visible = False
            
        if not self.visible:
            self.f_label.place(x=context['lx'], y=context['ty'])
            self.f_label.lift()

        self.visible = True
        self.hidden = False
        self.last_context = context


    def is_displayed(self):
        return self.visible


    def undisplay(self):
        if not self.drawn or not self.visible:
            return False

        if self.hidden:
            self.b_label.place_forget()
        else:
            self.f_label.place_forget()

        self.visible = False

    def display_back(self, context):
        if not self.drawn:
            self._setup_display_objects(context)

        if not self.hidden and self.visible:
            self.f_label.place_forget()

        self.b_label.place(x=context['lx'], y=context['ty'])
        self.b_label.lift()

        self.visible = True
        self.hidden = True
        self.last_context = context

    def move_display(self, context):
        if self.hidden:
            self.display_back(context)
        else:
            self.display_card(context)

    def _enlarge(self, event):
        if self.enlarged:
            self._shrink()
        else:
            w = (self.last_context['rx'] - self.last_context['lx']) * 2
            h = (self.last_context['by'] - self.last_context['ty']) * 2

            lx = self.last_context['lx']/2
            ty = self.last_context['ty']/2

            self._resize_image(w, h)

            if self.hidden:
                self.b_label.place(x=lx, y=ty)
                self.b_label.lift()
            else:
                self.f_label.place(x=lx, y=ty)
                self.f_label.lift()
            
            self.enlarged = True

    def _shrink(self):
        w = self.last_context['rx'] - self.last_context['lx']
        h = self.last_context['by'] - self.last_context['ty']

        self._resize_image(w, h)

        if self.visible:
            self.undisplay()
            if self.hidden:
                self.display_back(self.last_context)
            else:
                self.display_card(self.last_context)

        self.enlarged = False


    def _resize_image(self, w, h):
            size = w, h

            fi = Image.open(self.f_image)
            bi = Image.open(self.b_image)

            bi.thumbnail(size, Image.ANTIALIAS)
            self.b_photo = ImageTk.PhotoImage(bi)

            self.b_label.config(width=w, height=h, image=self.b_photo)
            self.b_label.image = self.b_photo

            fi.thumbnail(size, Image.ANTIALIAS)
            self.f_photo = ImageTk.PhotoImage(fi)

            self.f_label.config(width=w, height=h, image=self.f_photo)
            self.f_label.image = self.f_photo


