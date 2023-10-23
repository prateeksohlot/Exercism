def square(number:int):
    """Calculate the number of grains of wheat on a square of the chessboard.
    """
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")
    else:
        return 2 ** (number - 1)


def total():
    """Calculate the total number of grains of wheat on the chessboard.
    """
    total = [2**(x-1) for x in range(1, 65)]

    return sum(total)