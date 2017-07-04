from cards import Card


class SentinelCard(Card):
    def __init__(self, card):
        super(SentinelCard, self).__init__(card['name'])
        self.tags = card['tags']
        self.description = card['description']
        if 'quote' in card:
            self.quote = card['quote']
        else:
            self.quote = ""

        if SentinelTag.TARGET in self.tags:
            self.max_health = card['max_health']
            self.current_health = self.max_health

    def display_card(self):
        print name, 

    def undisplay(self):
        return False

    def get_tags_str(self):
        tag_str = ""
        for tag in self.tags:
            if not tag == SentinelTag.TARGET:
                tag_str += tag + ", "
        if len(tag_str) > 0:
            tag_str = tag_str[:len(tag_str)-2]

        return tag_str


class SentinelTag(object):
    ONGOING = 'Ongoing'
    EQUIPMENT = 'Equipment'
    ONE_SHOT = 'One Shot'
    TARGET = ''
    RELIC = 'Relic'
    CONSTRUCT = 'Construct'
    GOLEMN = 'Golemn'
    DEVICE = 'Device'
    BURST = 'Burst'
    MINION = 'Minion'
    HERO = 'Hero'
    SURVIVOR = 'Survivor'
    GENE_SERUM = 'Gene-Serum'
    

def load_heros_from_file(file):
    f = open(file, "r")

