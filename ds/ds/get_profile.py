def get_profile(name, age, *args, **kwargs):
    if age.__class__.__name__ != 'int':
        raise ValueError()
    if len(args) > 5:
        raise ValueError()
    result = {'name': name, 'age': age}
    if args:
        result.update({'sports': sorted(args)})
    if kwargs:
        result.update({'awards': kwargs})
    return result


print(get_profile('punit', 42, 10, 12))
