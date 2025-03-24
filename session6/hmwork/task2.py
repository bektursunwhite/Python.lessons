def abbreviate(word):
    lst_of_words = word.split()
    final = ""

    for word in lst_of_words:
        final += word[0].upper()

    return final


inp = input("Input: ")
print(abbreviate(inp))