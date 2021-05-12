def compare_words(a,b): 
    word_1 = set(a) 
    word_2 = set(b)
    remove ={" "} 
    list = (word_1 & word_2)-remove
    alist= ''.join(list)
    return alist
print(compare_words('joy','flow'))

