

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

    def dispatch_event(self, type):
        if self.has_listener(type):
            self._listeners[type]()



class Counter(EventDispatcher):

    ON_START = "onStart"
    ON_CHANGE = "onChange"
    ON_FINISH = "onFinish"

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
        #print(self.ON_START)
        self.dispatch_event(self.ON_START)
        for i in range(self.start, self.end, self.step):
            #print("change")
            self.dispatch_event(self.ON_CHANGE)
        #print("finish")
        self.dispatch_event(self.ON_FINISH)


c = Counter()

def onStart():
    print("Counter onStart")

def onChange():
    print("Counter onChange")

def onFinish():
    print("Counter onFinish")

c.add_listener(Counter.ON_START, onStart)
c.add_listener(Counter.ON_CHANGE, onChange)
c.add_listener(Counter.ON_FINISH, onFinish)

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