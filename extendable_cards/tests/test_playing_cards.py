from extendable_cards.lib.playing_cards import PlayingCard

def test_playing_card():
    test_suit = "suit"
    test_number = 5
    card = PlayingCard(test_suit, test_number)

    assert card.suit == test_suit
    assert card.number == test_number
    assert card.name == "5 suit"
