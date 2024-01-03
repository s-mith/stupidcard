class Card:
    def __init__(self, name, cost, effects, text, id, gameid, owner):
        self.name = name
        self.cost = cost
        self.effects = effects
        self.text = text
        self.id = id
        self.gameid = gameid
        self.owner = owner
    def execute_effects(self, gamemaster):
        # execute_effects 
        _effects = []
        for effect in self.effects:
            x = effect.execute(gamemaster)
            _effects.append(x) if x != None else None
        return _effects
    def is_creature(self):
        return False
    def is_spell(self):
        return False
    def set_owner(self, owner):
        self.owner = owner