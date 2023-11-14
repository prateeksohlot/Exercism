vowels = ('a', 'e', 'i', 'o', 'u', 'xr', 'yt') # 'xr' and 'yt' are special cases

def translate(text:str) -> str:
    # we join all the words together with a space in between
    return ' '.join(pig_latinize(word) for word in text.split())
    
def pig_latinize(word:str) -> str:

# Condition 1: If the first letter is a vowel, add 'ay' to the end
    # if word.startswith(vowels):
    #     return word + 'ay'

    
    # To solve Yellow edge case
    if word.startswith('y'):
        return word[1:] + word[0] + 'ay'

    # Condition 2: If the first letter is a consonant, move it to the end and add 'ay'    
    # Condition 4: If a word contains a "y" after a consonant cluster (e.g. "rhythm" -> "ythmrhay").
    
    while not word.startswith(vowels + ('y',)): # we add 'y' to the tuple of vowels
        word = word[1:] + word[0]

    # Condition 3:  If a word starts with a consonant sound followed by "qu", move it to the end of the word, and then add an "ay" sound to the end of the word.
    if word.startswith('u') and word.endswith('q'):
        word = word[1:] + word[0]
        
    return word + 'ay'
    

xxx = translate('therapy')
print(xxx)