from counter import Counter

c = Counter()


def on_start(source):
    print(Counter.ON_COUNTER_START + " count: " + str(source.count))
    #source.remove_listener(Counter.ON_COUNTER_CHANGE)


def on_change(source):
    print(Counter.ON_COUNTER_CHANGE + " count: " + str(source.count))


def on_finish(source):
    print(Counter.ON_COUNTER_FINISH + " count: " + str(source.count))


c.add_listener(Counter.ON_COUNTER_START, on_start)
c.add_listener(Counter.ON_COUNTER_CHANGE, on_change)
c.add_listener(Counter.ON_COUNTER_FINISH, on_finish)

c.run()
