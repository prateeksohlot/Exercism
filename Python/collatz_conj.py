def steps(number):
    if number < 1 or type(number) != int:
        raise ValueError("Only positive integers are allowed")
    
    counter = 0
    while number != 1:
        counter += 1       
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
    return counter