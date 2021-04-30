
def find_vowels(string):
    vowels_list = "aeiouAEIOU"
    res = set([each for each in string if each in vowels_list])
    return res
print("vowels found in word are: ", find_vowels(input()))
    




