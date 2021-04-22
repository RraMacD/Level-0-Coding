user_1 =input('Add a word: ')
user_2 =input('Add a word: ')
word_1 = set ( user_1)
word_2 = set (user_2)
list = [word_1 & word_2]
print('common letters: {}' .format(list))
