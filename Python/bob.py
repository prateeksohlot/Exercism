
def response(hey_bob):
    '''Bob's response to a given input.
    
    Parameters:
    :return "Sure" to This is his response if you ask him a question, such as "How are you?" The convention used for questions is that it ends with a question mark.
    :return "Whoa, chill out!" if you yell at him.
    :return "Calm down, I know what I'm doing!" if you yell a question at him.
    :return "Fine. Be that way!" to Bob's lack of response.
    :return "Whatever." to anything else.
    
    '''
    hey_bob = hey_bob.strip()
    if hey_bob.isupper() and hey_bob.endswith('?'):
        return "Calm down, I know what I'm doing!"
    if hey_bob.isupper():
        return "Whoa, chill out!"
    if hey_bob.endswith('?'):
        return "Sure."
    if hey_bob == '':
        return "Fine. Be that way!"
    
    return "Whatever."