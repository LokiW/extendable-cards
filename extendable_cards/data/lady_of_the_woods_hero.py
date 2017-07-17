from extendable_cards.lib.sentinels import SentinelTag

"""
For this to work you need to download the card images from
http://meromorph.com/tangent/cauldron/heroes/ladyofthewood.php
and unzip them in extendable_cards/data/card_images then change
the generated folder Lady of the Wood to LadyoftheWood.
"""

def get_lady_of_the_woods_hero():
    cards = []
    #Grand Warlord Voss Hero Card
    cards.append({
        'name': "Lady of the Wood",
        'tags': [SentinelTag.TARGET, SentinelTag.HERO],
        'description': "",
        'max_health': 30,
        'f_image': 'data/card_images/LadyoftheWood/card0 char front-01.jpg',
        'b_image': 'data/card_images/LadyoftheWood/card0 char back-01.jpg'
    })

    #Survivors (Minions)
    meadow_rush = {
        'name': "Meadow Rush",
        'tags': [],
        'description': "",
        'f_image': 'data/card_images/LadyoftheWood/card12 meadow-qty4.jpg',
        'b_image': 'data/card_images/LadyoftheWood/card0 deck back-01.jpg'
    }
    cards.extend([meadow_rush, meadow_rush, meadow_rush, meadow_rush])

    spring_d = {
        'name': "Rainpetal Cloak",
        'tags': [],
        'description': "",
        'f_image': 'data/card_images/LadyoftheWood/card1 dress spring-qty2.jpg',
        'b_image': 'data/card_images/LadyoftheWood/card0 deck back-01.jpg'
    }
    cards.extend([spring_d, spring_d])

    summer_d = {
        'name': "Suncast Mantle",
        'tags': [],
        'description': "",
        'f_image': 'data/card_images/LadyoftheWood/card2 dress summer-qty2.jpg',
        'b_image': 'data/card_images/LadyoftheWood/card0 deck back-01.jpg'
    }
    cards.extend([summer_d, summer_d])

    fall_d = {
        'name': "Thundergrey Shawl",
        'tags': [],
        'description': "",
        'f_image': 'data/card_images/LadyoftheWood/card3 dress fall-qty2.jpg',
        'b_image': 'data/card_images/LadyoftheWood/card0 deck back-01.jpg'
    }
    cards.extend([fall_d, fall_d])

    winter_d = {
        'name': "Snowshade Gown",
        'tags': [],
        'description': "",
        'f_image': 'data/card_images/LadyoftheWood/card4 dress winter-qty2.jpg',
        'b_image': 'data/card_images/LadyoftheWood/card0 deck back-01.jpg'
    }
    cards.extend([winter_d, winter_d])

    spring = {
        'name': "Spring",
        'tags': [],
        'description': "",
        'f_image': 'data/card_images/LadyoftheWood/card5 spring-qty2.jpg',
        'b_image': 'data/card_images/LadyoftheWood/card0 deck back-01.jpg'
    }
    cards.extend([spring, spring])

    summer = {
        'name': "Summer",
        'tags': [],
        'description': "",
        'f_image': 'data/card_images/LadyoftheWood/card6 summer-qty2.jpg',
        'b_image': 'data/card_images/LadyoftheWood/card0 deck back-01.jpg'
    }
    cards.extend([summer, summer])

    fall = {
        'name': "Fall",
        'tags': [],
        'description': "",
        'f_image': 'data/card_images/LadyoftheWood/card7 fall-qty2.jpg',
        'b_image': 'data/card_images/LadyoftheWood/card0 deck back-01.jpg'
    }
    cards.extend([fall, fall])

    winter = {
        'name': "Winter",
        'tags': [],
        'description': "",
        'f_image': 'data/card_images/LadyoftheWood/card8 winter-qty2.jpg',
        'b_image': 'data/card_images/LadyoftheWood/card0 deck back-01.jpg'
    }
    cards.extend([winter, winter])

    rebirth = {
        'name': "Rebirth",
        'tags': [],
        'description': "",
        'f_image': 'data/card_images/LadyoftheWood/card9 rebirth-qty2.jpg',
        'b_image': 'data/card_images/LadyoftheWood/card0 deck back-01.jpg'
    }
    cards.extend([rebirth, rebirth])

    clearing = {
        'name': "Enchanted Clearing",
        'tags': [],
        'description': "",
        'f_image': 'data/card_images/LadyoftheWood/card10 clearing-qty2.jpg',
        'b_image': 'data/card_images/LadyoftheWood/card0 deck back-01.jpg'
    }
    cards.extend([clearing, clearing])

    serenity = {
        'name': "Serenity of Dawn",
        'tags': [],
        'description': "",
        'f_image': 'data/card_images/LadyoftheWood/card11 serenity-qty2.jpg',
        'b_image': 'data/card_images/LadyoftheWood/card0 deck back-01.jpg'
    }
    cards.extend([serenity, serenity])

    frost_petal = {
        'name': "Frost on the Petals",
        'tags': [],
        'description': "",
        'f_image': 'data/card_images/LadyoftheWood/card13 frostpetal-qty3.jpg',
        'b_image': 'data/card_images/LadyoftheWood/card0 deck back-01.jpg'
    }
    cards.extend([frost_petal, frost_petal, frost_petal])

    cloudfire = {
        'name': "Fire in the Clouds",
        'tags': [],
        'description': "",
        'f_image': 'data/card_images/LadyoftheWood/card14 cloudfire-qty3.jpg',
        'b_image': 'data/card_images/LadyoftheWood/card0 deck back-01.jpg'
    }
    cards.extend([cloudfire, cloudfire, cloudfire])

    nobility = {
        'name': "Nobility of Dusk",
        'tags': [],
        'description': "",
        'f_image': 'data/card_images/LadyoftheWood/card15 nobility-qty3.jpg',
        'b_image': 'data/card_images/LadyoftheWood/card0 deck back-01.jpg'
    }
    cards.extend([nobility, nobility, nobility])

    calm = {
        'name': "Calm Before the Storm",
        'tags': [],
        'description': "",
        'f_image': 'data/card_images/LadyoftheWood/card16 calm-qty3.jpg',
        'b_image': 'data/card_images/LadyoftheWood/card0 deck back-01.jpg'
    }
    cards.extend([calm, calm, calm])

    crown = {
        'name': "Crown of the Four Winds",
        'tags': [],
        'description': "",
        'f_image': 'data/card_images/LadyoftheWood/card17 crown-qty2.jpg',
        'b_image': 'data/card_images/LadyoftheWood/card0 deck back-01.jpg'
    }
    cards.extend([crown, crown])

    return cards
