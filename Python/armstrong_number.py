#Approach 1
def is_armstrong_number(number:int)->bool:

    ''' Checks if a number is an Armstrong number.

    An Armstrong number is a number that is the sum of 
    its own digits each raised to the power of the number of digits.

    '''
    
    number = str(number)
    length = len(number)

    total = [int(i)**length for i in number]

    # Check if the sum of the digits raised to the power of the length is equal to the number.
    if sum(total) == int(number):
        return True
    else:
        return False

#Approach 2

def is_armstrong_number(number:int)->bool:
    
    ''' Checks if a number is an Armstrong number.

    An Armstrong number is a number that is the sum of 
    its own digits each raised to the power of the number of digits.

    '''

    return sum([int(i)**len(str(number)) for i in str(number)]) == number