
def test_playing_card():
    test_suit = "suit"
    test_numbr = 5
    card = PlayingCard(suit, number)

    assert card.suit == test_suit
    assert card.number == test_numbr
    assert card.name == "5 suit"
