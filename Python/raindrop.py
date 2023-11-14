def convert(number):
    '''
    It converts a number to a string.
    if number is divisible by 3, returns 'Pling'
    if number is divisible by 5, returns 'Plang'
    if number is divisible by 7, returns 'Plong'
    if number is not divisible by 3, 5 or 7, returns the number as a string.
    
    :param number: int - the number to convert.
    :return: str - the converted number.
    '''
    result_string = ''

    if number % 3 == 0:
        result_string += 'Pling'
    if number % 5 == 0:
        result_string += 'Plang'
    if number % 7 == 0:
        result_string += 'Plong'
    
    return result_string or str(number)
