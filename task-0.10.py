def compare_words(a,b):
    word1 = set(a)
    word2 = set(b)
    remove = {' '}
    list = (word1 & word2) - remove
    alist = ' , '.join(list)
    return "Common letters: " + str(alist)

print(compare_words('computer','house'))
