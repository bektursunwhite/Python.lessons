#### Task number4. 


word = input("Please enter a word: ")

char_count = {}
for char in word: 
    if char in char_count:
        char_count[ char ] += 1
    else: 
        char_count[ char ] = 1 
print(char_count)