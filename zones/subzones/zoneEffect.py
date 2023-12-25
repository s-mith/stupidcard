class ZoneEffect(Zone):
    def __init__(self, id, effects):
        super().__init__(id)
        self.effects = effects
    def add_effect(self, effect):

        self.effects.append(effect)
        return effect

    def remove_effect(self, effect):

        self.effects.remove(effect)
        return effect

    def count(self):
        return len(self.effects) 