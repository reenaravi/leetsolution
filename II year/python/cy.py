from itertools import cycle
data = [5, 10, 15]
iter_count = 0
for item in cycle(data):
    print(item)
    iter_count += 1
    if iter_count == 9: # 3 items * 3 iterations = 9
        break
