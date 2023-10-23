"""Functions used in preparing Guido's gorgeous lasagna.  

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum
This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time:int):

    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    remaining = 40 - elapsed_bake_time      
    return remaining


def preparation_time_in_minutes(number_of_layers:int):
    """Calculate the preparation time.

    :param layers: int total of layers of lasagna
    :return: int total time of preparation of layers derived from 'PREPARATION_TIME'

    Function that takes the number of layers that will be prepared to lasagna and returns how many minutes it will take to get done
    """

    preparation_time = number_of_layers * 2
    return preparation_time 


def elapsed_time_in_minutes(number_of_layers:int, elapsed_bake_time:int)-> int:
    """Calculate the elapsed cooking time.

     Keyword arguments:
    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    Function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the lasagna.
    """

    total_elapsed_time = number_of_layers * 2 + elapsed_bake_time
    return total_elapsed_time   