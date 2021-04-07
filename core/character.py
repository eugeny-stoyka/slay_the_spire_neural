

class Character:
    def __init__(self):
        self.max_health     = 0
        self.current_health = 0
        
        self.cards   = []
        self.relics  = []
        self.potions = []

        self.keys = {
            "red": None,
            "blue": None,
            "green": None
        }

class Ironclad(Character):
    def __init__(self):
        pass

class Silent(Character):
    def __init__(self):
        pass

class Defect(Character):
    def __init__(self):
        self.orbs = {
            "slots": [],
            "length": 3
        }
        pass
        
class Watcher(Character):
    def __init__(self):
        pass