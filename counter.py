from herr_vogt import event_dispatcher


class Counter(event_dispatcher.EventDispatcher):

    ON_COUNTER_START = "on_counter_start"
    ON_COUNTER_CHANGE = "on_counter_change"
    ON_COUNTER_FINISH = "on_counter_finish"

    def __init__(self, start=0, end=10, step=1):
        super().__init__()
        self.start = start
        self.end = end
        self.step = step

        self.count = 0

    def reset(self, start=0, end=10, step=1):
        self.start = start
        self.end = end
        self.step = step

        self.count = 0

    def run(self):
        self.dispatch_event(self.ON_COUNTER_START, self)
        for i in range(self.start, self.end, self.step):
            self.count = i
            self.dispatch_event(self.ON_COUNTER_CHANGE, self)
        self.dispatch_event(self.ON_COUNTER_FINISH, self)
