from functools import wraps

known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']


def login_required(func):
    @wraps(func)
    def inner(user):
        if user not in known_users:
            return 'please create an account'
        elif user not in loggedin_users:
            return 'please login'
        return func(user)
    return inner


@login_required
def welcome(user):
    '''Return a welcome message if logged in'''
    return f'welcome back {user}'
