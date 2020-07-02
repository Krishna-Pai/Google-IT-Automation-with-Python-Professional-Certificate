#Following code should be executed on Python shell

fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}
sorted(fruit.items())

import operator
sorted(fruit.items(), key=operator.itemgetter(0))

sorted(fruit.items(), key=operator.itemgetter(1))

sorted(fruit.items(), key = operator.itemgetter(1), reverse=True)