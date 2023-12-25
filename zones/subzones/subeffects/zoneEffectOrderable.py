class ZoneEffectOrderable(ZoneEffect):
    def __init__(self, id, effects):
        super().__init__(id, effects)
    def add_effect(self, effect):
        
        self.effects.append(effect)
        return effect

    def remove_effect(self, effect):

        self.effects.remove(effect)
        return effect

    def reorder_effects(self, order):
        self.effects = [self.effects[i] for i in order]