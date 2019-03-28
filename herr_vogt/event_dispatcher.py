class EventDispatcher:

    def __init__(self):
        self._listeners = {}

    def has_listener(self, type):
        if type in self._listeners:
            return True
        return False

    def add_listener(self, type, listener):
        if not self.has_listener(type):
            self._listeners[type] = listener
            return True
        return False

    def remove_listener(self, type):
        if self.has_listener(type):
            del self._listeners[type]
            return True
        return False

    def dispatch_event(self, type, *varg):
        if self.has_listener(type):
            self._listeners[type](*varg)

    def get_listeners(self):
        return self._listeners