from functools import wraps


def make_html(element):
    def decorator(func):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            return f'<{element}>{result}</{element}>'
        return inner
    return decorator


@make_html('p')
def get_text(text='I code with PyBites'):
    return text
