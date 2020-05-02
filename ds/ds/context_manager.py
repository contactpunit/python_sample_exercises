'''
Testing context manager
'''


class Hello:
    def __enter__(self):
        print('I am entering context manager')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('I am exiting context manager')


with Hello():
    print('I am in middle')
