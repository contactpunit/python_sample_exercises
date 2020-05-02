import numbers


# def running_mean(sequence):
#     """Calculate the running mean of the sequence passed in,
#        returns a sequence of same length with the averages.
#        You can assume all items in sequence are numeric."""
#     start = meanval(0)
#     next(start)
#     for num in sequence:
#         start.send(num)
#     try:
#         start.send(None)
#     except StopIteration as e:
#         return e.value
#
#
# def meanval(num):
#     """Implementation using coroutine"""
#     results = []
#     count = 0
#     total = 0
#     avg = 0
#     while True:
#         num = yield
#         if num is None:
#             break
#         total += num
#         count += 1
#         avg = total / count
#         results.append(avg)
#     return results

def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    total = 0
    avg = 0
    count = 0
    for num in sequence:
        total += num
        count += 1
        avg = total / count
        yield round(avg, 2)
