## the task require us to write a code that reads a word forward and backward

# word = input("Please enter ur word: ")
# re_word = word == word[::1]
# print(re_word)


def palindrome(s):
    s = [char.lower() for char in (s) if char.isalnum()]
    return s == list(reversed(s))

print(palindrome("madam"))
print(palindrome("hello"))
print(palindrome("checo"))
print(palindrome("wakaw"))