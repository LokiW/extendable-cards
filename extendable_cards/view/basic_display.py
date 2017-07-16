from extendable_cards.view.graphics import GraphWin
from extendable_cards.view.card_view import CardView
from extendable_cards.view.playing_card_view import PlayingCardView
from extendable_cards.lib.cards import Card
from extendable_cards.lib.playing_cards import PlayingCard
from PIL import Image, ImageTk

from tkinter import Frame, Text, Label

def display():
    win = GraphWin()
    win.setCoords(0,0,10,10)

    """
    frame = Frame(win, width=100, height=100)
    frame.config(borderwidth=2, relief='groove')
    frame.place(x=50,y=1)
    
    text = Text(frame, height=1, width=20)
    text.insert('end', "TEST TEXT")

    text2 = Text(frame, height=1, width=20)
    text2.insert('end', "TESTTESTTESTTESTTESTETEST")

    text.grid(row=0, column=0)
    text2.grid(row=2, column=0)
    frame.config(width=100, height=100)

    while 1:
        mouse_point = win.getMouse()
        frame.place(x=mouse_point.getX(), y=mouse_point.getY())
    #text.pack()
    """

    image = Image.open("data/card_images/Lady of the Wood/card0 char back-01.jpg")
    size = win.width, win.height
    image.thumbnail(size, Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)

    label = Label(win, image=photo)
    label.image = photo # keep a reference!
    label.place(x=3,y=3)

    while 1:
        mouse_point = win.getMouse()
        label.place(x=mouse_point.getX(), y=mouse_point.getY())

    win.getMouse()
    win.close()


if __name__ == "__main__":
    display()
