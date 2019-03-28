

class EventDispatcher():


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






class Counter(EventDispatcher):

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







c = Counter()

def onStart(source):
    print(Counter.ON_COUNTER_START + " count: " + str(source.count))
    #source.remove_listener(Counter.ON_COUNTER_CHANGE)

def onChange(source):
    print(Counter.ON_COUNTER_CHANGE + " count: " + str(source.count))

def onFinish(source):
    print(Counter.ON_COUNTER_FINISH + " count: " + str(source.count))

c.add_listener(Counter.ON_COUNTER_START, onStart)
c.add_listener(Counter.ON_COUNTER_CHANGE, onChange)
c.add_listener(Counter.ON_COUNTER_FINISH, onFinish)

c.run()





# list = {
#     "onStart": 1,
#     "onChange": 2,
#     "onFinish": 3
# }
#
# for item in list:
#     print(item + " : " + str(list.get(item)))
#
# def in_list(type):
#     if type in list:
#         return True
#     return False
#
# def add_list(type, val):
#     if not in_list(type):
#         list[type] = val
#         return True
#     return False
#
# def del_list(type):
#     if in_list(type):
#         del list[type]
#         return True
#     return False
#
# add_list("onComplete", 4)
# del_list("onComplete")
#
# print(list)
#
#
#
# #print(in_list("onStarte"))