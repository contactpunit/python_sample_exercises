def sum_numbers(numbers=None):
    """Returns sum of list of numbers provided.
     If no argument is provided, return sum of numbers 1..100"""
    if numbers is None:
        return sum(range(1, 101))
    else:
        return sum(numbers)
