from zoneEffect import ZoneEffect
from effect import Effect

class ZoneEffectOrderable(ZoneEffect):
    def __init__(self, id, effects:list[Effect]):
        super().__init__(id, effects)

    def add_effect(self, effect: Effect):
        # check to make sure effect is a effect
        if isinstance(effect, Effect):
            self.effects.append(effect)
            return effect
        else:
            print("Error: effect is not a effect")

    def remove_effect(self, effect: Effect):
        # check to make sure effect is a effect
        if isinstance(effect, Effect):
            self.effects.remove(effect)
            return effect
        else:
            print("Error: effect is not a effect")

    def reorder_effects(self, order:list[int]):
        self.effects = [self.effects[i] for i in order]