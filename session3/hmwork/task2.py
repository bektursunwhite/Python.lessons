### Trying to use "for" for reverse the word >>> 


word = input("Enter a word: ")
re_word = ""

for char in word:
    re_word = char + re_word 

print("Reversed Word:", re_word)
