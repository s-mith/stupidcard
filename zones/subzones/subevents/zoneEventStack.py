class ZoneEventStack(ZoneEvent):
    def __init__(self, id, events):
        super().__init__(id, events)
        self.events = events
    def add_event(self, event):
        self.events.append(event)
        return event
    def remove_event(self, event):
        self.events.remove(event)
        return event
    def look_top(self):
        return self.events[0]
    def get_top(self):
        return self.events.pop()