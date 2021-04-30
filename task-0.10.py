def compare_words(a,b):
    word_1 = set(a)
    word_2 = set(b)
    list = [word_1 & word_2]
    return list
print(compare_words(input(),input()))

