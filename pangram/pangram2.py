def is_pangram(sentence):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    s = sentence.lower()
    for i in letters:
        if i not in s:
            return False
    return True

# My version of https://exercism.io/tracks/python/exercises/pangram/solutions/1af34230909f43149f1931ed6462bb54
from string import ascii_lowercase as letters

def other_is_pangram(sentence):
    # return all(i in sentence or chr(ord(i)-32) in sentence for i in letters)
    sentence = sentence.lower()
    return all(i in sentence for i in letters)

# My version of https://exercism.io/tracks/python/exercises/pangram/solutions/2d7f85e971e64e988c26904899d82f34
# import string
def another_is_pangram(sentence):
    # chars = string.ascii_lowercase
    # req = set(chars)
    # return req <= set(sentence.lower())
    return set(letters) <= set(sentence.lower())


if __name__ == '__main__':
    a = "The quick brown fox! 5 Jumps over he lazy dog."
    print("OK" if is_pangram(a) else "Error")
    print("OK" if other_is_pangram(a) else "Error")
    print("OK" if another_is_pangram(a) else "Error")
