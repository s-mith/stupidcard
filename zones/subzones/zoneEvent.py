class ZoneEvent(Zone):
    def __init__(self, id, events):
        super().__init__(id)
        self.events = events
    def add_event(self, event):
        self.events.append(event)
    def remove_event(self, event):
        if isinstance(event):
            self.events.remove(event)
            return event
        else:
            print("Error: event is not a event")
    def count(self):
        return len(self.events) 