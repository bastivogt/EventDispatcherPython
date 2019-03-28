from counter import Counter

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