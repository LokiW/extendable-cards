from extendable_cards.lib.sentinels import SentinelTag

def get_grand_warlord_voss_hero():
    cards = []
    #Grand Warlord Voss Hero Card
    cards.append({
        'name': "Rainek The Disgraced",
        'tags': [SentinelTag.TARGET, SentinelTag.HERO],
        'description': "Command\nPower: Choose one of attack, assist, analyse or defend, activate all texts of the chosen type.",
        'max_health': 30
    })

    #Survivors (Minions)
    cards.append({
        'name': "The Last Feethsmar",
        'tags': [SentinelTag.TARGET, SentinelTag.SURVIVOR],
        'description': "This target is immune to cold damage.\nAt the start of Rainek's turn, the Last Feethsmar deals each nonhero target 1 cold damage.\nAttack: Deal 1 target 2 cold damage.\nAssist: Deal 1 target 1 cold damage. If they take damage this way, reduce damage delt by that target by 1 until the start of your next turn.\nAnalyse: Deal 1 non-villain target, other then itself, 3 cold damage.\nDefend:Activate an attack text.",
        'max_health': 9
    })

    cards.append({
        'name': "The Last Ruoenf",
        'tags': [SentinelTag.TARGET, SentinelTag.SURVIVOR],
        'description': "This target is immune to melee damage.\nReduce damage to this target by 1.\nAttack: Deal 1 target 1 melee damage.\nAssist:Reduce damage to 1 other target by 1.\nAnalyse: One player may draw 1 card now.\nDefend: Redirect all damage that would be dealt to a hero target to The last Ruenf.",
        'max_health': 12
    })

    cards.append({
        'name': "The Gene-Bound Infantry",
        'tags': [SentinelTag.TARGET, SentinelTag.SURVIVOR],
        'description': "This target is immune to lightning damage.\nAt the end of Rainek's turn, heal 3 targets for 1 hp each.\nAttack:Deal each target 1 lightning damage.\nAssist: You may destroy 1 ongoing or environment card.\nAnalyse: Activate a defend text.\nDefend: Reduce damage to The Gene-Bound Infantry target by 1.",
        'max_health': 8
    })

    cards.append({
        'name': "Gene-Bound Thorathian Tamar",
        'tags': [SentinelTag.TARGET, SentinelTag.SURVIVOR],
        'description': "This target is immune to psychic damage.\nAt the end of Rainek's turn, activate an attack, assist, analyse or defend text.\nAttack: Deal 1 target 1 damage. Activate a different attack text.\nAssist: Activate an attack, assist, analyse or defend text.\nAnalyse: Look at the top card of any deck, put that card either in play, on the top or bottom of that deck or discard it.\nDefend: Reduce all damage by 1.",
        'max_health': 10,
        'quote': "The valiant sometimes taste death twice. -Tamar"
    })

    #One Shots Survivor Retreival Cards
    forced_redeployment = {
        'name': "Forced Redeployment",
        'tags': [SentinelTag.ONE_SHOT],
        'description': "Take all Survivors from your discard and put them into play."
    }
    cards.extend([forced_redeployment, forced_redeployment])

    reinforcements = {
        'name': "Reinforcements",
        'tags': [SentinelTag.ONE_SHOT],
        'description': "Search your deck for a Survivor and put it into your hand. Shuffle your deck."
    }
    cards.extend([reinforcements, reinforcements, reinforcements, reinforcements])

    #Equipment
    boost_collar = {
        'name': "Boost Injection Collar",
        'tags': [SentinelTag.EQUIPMENT],
        'description': "Put this card next to a target. Increase damage dealt by that target by 1. At the start of their turn, that target deals themself 1 cold damage.",
    }
    cards.extend([boost_collar, boost_collar])

    crushing_sheild = {
        'name': "Crushing Sheild",
        'tags': [SentinelTag.EQUIPMENT],
        'description': "Put this card next to a target. The first time that target would take 2 or less damage each turn, they may redirect that damage to the target of their choice. At the start of their turn, that target deals themselves 3 melee damage."
    }
    cards.extend([crushing_sheild, crushing_sheild])

    storm_bracelets = {
        'name': "Storm Eye Bracelets",
        'tags': [SentinelTag.EQUIPMENT],
        'description': "Put this card next to a target. Increase healing done by that target by 1. At the start of their turn, that target deals themselves 2 lightning damage."
    }
    cards.extend([storm_bracelets, storm_bracelets])

    action_helm = {
        'name': "Helm of Action",
        'tags': [SentinelTag.EQUIPMENT],
        'description': "Put this card next to a target. At the start of theri turn, that target may deal themselves 2 psychic damage to activate one of their attack, assist, analyse or defend texts."
    }
    cards.extend([action_helm, action_helm])

    energy_gauntlets = {
        'name': "Energy Gauntlets",
        'tags': [SentinelTag.EQUIPMENT],
        'description': "Put this card next to a hero character card.\nPower: Deal yourself and one other target 1 fire and 1 energy damage. Use a power now."
    }
    cards.extend([energy_gauntlets, energy_gauntlets])

    #Ongoings
    eye_serum = {
        'name': "Enhanced Eyes",
        'tags': [SentinelTag.ONGOING, SentinelTag.GENE_SERUM],
        'description': "Put this card next to a target.\nAttack: This target deals 1 target one energy damage.",
        'quote': "Ah, sweet! Lazer eyes! -Setback"
    }
    cards.extend([eye_serum, eye_serum])

    leg_serum = {
        'name': "Speed Enhancement",
        'tags': [SentinelTag.ONGOING, SentinelTag.GENE_SERUM],
        'description': "Put this card next to a hero.\nAnalyse: This hero draws 1 card now."
    }
    cards.extend([leg_serum, leg_serum])

    disposition_serum = {
        'name': "Disposition Enhancement",
        'tags': [SentinelTag.ONGOING, SentinelTag.GENE_SERUM],
        'description': "Put this card next to a hero.\nAssist: This hero may discard up to 2 cards. One hero may draw x cards, where x is the number of cards discarded this way."
    }
    cards.extend([disposition_serum, disposition_serum])

    skin_serum = {
        'name': "Flesh Enhancement",
        'tags': [SentinelTag.ONGOING, SentinelTag.GENE_SERUM],
        'description': "Put this card next to a target.\nDefend: Reduce damage dealt to this target by 1 until the start of Rainek's next turn."
    }
    cards.extend([skin_serum, skin_serum])

    focused_command = {
        'name': "Focused Command",
        'tags': [SentinelTag.ONGOING],
        'description': "Power: Active all the attack, assist, analyse and defend text on one card."
    }
    cards.extend([focused_command, focused_command])

    #One Shots
    attack_order = {
        'name': "Pinpoint Attack Order",
        'tags': [SentinelTag.ONE_SHOT],
        'description': "One target of your choice deals one other target 2 melee damage. If the last Ruoenf deals this damage, then it is irreducable."
    }
    cards.extend([attack_order, attack_order])

    focus_order = {
        'name': "Focus Order",
        'tags': [SentinelTag.ONE_SHOT],
        'description': "Select a target, increase damage dealt by that target by 1 until the end of your next turn."
    }
    cards.extend([focus_order, focus_order])

    blocking_order = {
        'name': "Blocking Attack Order",
        'tags': [SentinelTag.ONE_SHOT],
        'description': "One target of your choice deals one other target 2 melee damage. If the Gene-Bound Infantry does this damage, then you may put one non-indestructable, non-character chard back on top of it's associated deck."
    }
    cards.extend([blocking_order, blocking_order])

    organized_strike = {
        'name': "Organized Strike",
        'tags': [SentinelTag.ONE_SHOT],
        'description': "Rainek deals 1 target x+1 melee damage where x is the number of Survivors in play."
    }
    cards.extend([organized_strike, organized_strike])

    warrior_strike = {
        'name': "Warrior's Strike",
        'tags': [SentinelTag.ONE_SHOT],
        'description': "Rainek deals 1 target 3 melee damage."
    }
    cards.extend([warrior_strike, warrior_strike])
    return cards
