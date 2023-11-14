def find_anagrams(word, candidates):
    '''
    This functions finds all anagrams of a given word in a list of candidates.

    param word: string - the word to find anagrams for.
    param candidates: list - a list of strings to search for anagrams in.
    return: list - a list of anagrams from the candidates list.
    '''    
    anagrams = []

    for candidate in candidates:
        if sorted(word.lower()) == sorted(candidate.lower()) and word.lower() != candidate.lower():
            anagrams.append(candidate)
    return anagrams
