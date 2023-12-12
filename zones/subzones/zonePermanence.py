from permanence import Permanence
from zone import Zone
class ZonePermanence(Zone):
    def __init__(self, id):
        super().__init__(id)
        self.permanences:list[Permanence] = []

    def add_permanence(self, permanence: Permanence):
        # check to make sure permanence is a permanence
        if isinstance(permanence, Permanence):
            self.permanences.append(permanence)
            return permanence
        else:
            print("Error: permanence is not a permanence")

    def remove_permanence(self, permanence: Permanence):
        # check to make sure permanence is a permanence
        if isinstance(permanence, Permanence):
            self.permanences.remove(permanence)
            return permanence
        else:
            print("Error: permanence is not a permanence")

    def count(self):
        return len(self.permanences)


    
    