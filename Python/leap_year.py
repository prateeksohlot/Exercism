# Checks Where a given year is a leap year or not.

# Approach 1
def leap_year(year:int)->bool:
    ''' Checks if a given year is a leap year or not.
    
    :param year: int - the year to check
    :return: bool - is the year a leap year?

    Years that are divisible by 4 and 400 are leap years.
    Years that are divisible by 4 and 100 are not leap years.    
    '''

    #check if the year is divisible by 4
    if year % 4 == 0:
        #check if the year is divisible by 400
        if year % 400 == 0:
            return True
        #check if the year is divisible by 100
        elif year % 100 == 0:
            return False
        else:
            return True
    else:
        return False
    
# Approach 2
def is_leap_year(year:int)->bool:
    ''' Checks if a given year is a leap year or not.
    
    :param year: int - the year to check
    :return: bool - is the year a leap year?

    Years that are divisible by 4 and 400 are leap years.
    Years that are divisible by 4 and 100 are not leap years.    
    '''
    
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)