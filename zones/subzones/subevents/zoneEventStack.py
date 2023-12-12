from zoneEvent import ZoneEvent
from event import Event

class ZoneEventStack(ZoneEvent):
    def __init__(self, id, events:list[Event]):
        super().__init__(id, events)
        self.events = events
    
    def add_event(self, event: Event):
        # check to make sure event is a event
        if isinstance(event, Event):
            self.events.append(event)
            return event
        else:
            print("Error: event is not a event")

    def remove_event(self, event: Event):
        # check to make sure event is a event
        if isinstance(event, Event):
            self.events.remove(event)
            return event
        else:
            print("Error: event is not a event")

    def get_top(self):
        return self.events.pop()
            

    