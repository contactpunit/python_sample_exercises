def averager():
    count = 0
    total = 0
    avg = 0
    while True:
        num = yield avg
        total += num
        count += 1
        avg = total/count


a = averager()
print(a)
print(next(a))
print(a.send(20))
print(a.send(10))
print(a.send(12))
a.close()