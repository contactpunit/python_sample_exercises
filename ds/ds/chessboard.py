WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    for num in range(size):
        for index in range(size):
            if num % 2 == 0:
                if index % 2 == 0:
                    print(WHITE, end='')
                else:
                    print(BLACK, end='')
            else:
                if index % 2 == 0:
                    print(BLACK, end='')
                else:
                    print(WHITE, end='')
        print()


create_chessboard()
