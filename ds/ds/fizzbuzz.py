def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'Fizz Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    return num
    # for i in range(1, num + 1):
    #     result = ','.join(['Fizz Buzz'
    #               if num % 3 == 0 and num % 5 == 0
    #               else 'Fizz' if num % 3 == 0
    #             else 'Buzz' if num % 5 == 0
    #             else str(num)
    #               for num in range(1, num + 1)
    #               ])
    #     return result
