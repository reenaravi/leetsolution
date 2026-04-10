from itertools import cycle, islice
data = ['a', 'b']
result = list(islice(cycle(data), 6))
print(result)
