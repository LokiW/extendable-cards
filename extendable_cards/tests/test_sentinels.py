from extendable_cards.lib.sentinels import SentinelCard, SentinelTag

def test_sentinels_card():
    input_card = {
        'name': 'Test Card',
        'tags': [SentinelTag.EQUIPMENT],
        'description': "This is a test card from a test"
    }
    sc = SentinelCard(input_card)
    assert sc
