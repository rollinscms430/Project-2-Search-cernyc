#NSK, 2017

from collections import defaultdict

''' 
    Loading dictopnary with words from file using rstrip() which returns a copy of the string in which all chars have been stripped from the end of the string.
'''
def load_words(filename='words.txt'):
    with open(filename) as f:
        tuples = []
        for word in f:
            tuples.append(word.strip())
    return tuples

'''
    Generating anagrams from the list of words in the dictionary
'''

def get_anagrams(source):
    dd = defaultdict(list)
    for word in source:
        key = "".join(sorted(word))
        dd[key].append(word)
    return dd

''' 
    Prints the anagrams pairings. 
'''

def print_anagrams(word_source):
    dd = get_anagrams(word_source)
    for key, anagrams in dd.iteritems():
        if len(anagrams) > 1:
            print(anagrams)

word_source = load_words()
print_anagrams(word_source)

