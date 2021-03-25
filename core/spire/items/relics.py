

class Relic:
    '''
    Базовый класс описания реликвий
    '''
    
    #шанс получения наград по событиям
    fight_chance = { 
        "common": 0.5, 
        "uncommon": 0.33, 
        "rare": 0.17 
    }

    chest_chance = { 
        "small": { 
            "common": 0.75, 
            "uncommon": 0.25, 
            "rare": 0 
        }, 
        "medium": { 
            "common": 0.35, 
            "uncommon": 0.5, 
            "rare": 0.15
        }, 
        "large": { 
            "common": 0, 
            "uncommon": 0.75, 
            "rare": 0.25 
        }
    }

    def __init__(self):
        self.id = 0
        self.name = ""
        self.rarity = "common" # uncommon, rare
        self.mechanic = None
        self.collection = "general" # "starter", "class", "shop", "boss", "event", "special"
        self.class_type = "general" # "silent", "ironclad", "defect", "watcher"

    #TODO механика
    def set_mechanic(self, mechanic_class):
        pass

    def activate(self):
        pass

class RelicStorage:
    def __init__(self):
        self.storage = []
    
    def load(self):
        pass

class RelicGetter:
    def __init__(self):
        pass

    def set_char_type(self, character_type: str):
        self.character_type = character_type
        return self

    def get_all_relics(self):
        pass

    def get_neow_relic(self):
        pass

    def get_shop_relics(self):
        pass
    
    def get_relic(self):
        pass

    def get_boss_relics(self):
        pass


class RelicFilter:
    def __init__(self):
        pass

    def get_by_type(self, type):
        '''
        Возвращает отфильтрованный список реликвий по типу
        '''
        pass

    def get_by_collection(self, type):
        '''
        Возвращает отфильтрованный список реликвий по коллекции
        '''
        pass

class RelicsTracker:
    '''
    Класс трекера реликвий для генерации их по эвенту, награде,
    и учет предыдущих реликвий, которые были пропущены, чтобы 
    не было повторов по мере восхождения
    '''
    def __init__(self):
        self.all_relics = []
        self.tracked_relics = []

    def add_to_track(self, relics):
        pass