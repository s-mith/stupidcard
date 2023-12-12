from effect import Effect
from zone import Zone

class ZoneEffect(Zone):
    def __init__(self, id, effects:list[Effect]):
        super().__init__(id)
        self.effects = effects

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

    def count(self):
        return len(self.effects) 