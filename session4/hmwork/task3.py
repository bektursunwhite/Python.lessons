# Task3.


words = input("Enter words: ").split()
longest_word = max(words, key=len) if words else "No words entered."
print("Longest word:", longest_word)
