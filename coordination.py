from threading import Event

event: Event | None = None


def register_event(ev: Event):
    global event
    event = event


def get_event() -> Event:
    return event


def is_event_set() -> bool:
    if event is None:
        return False

    return event.is_set()
