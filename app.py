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
