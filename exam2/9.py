word = input()
for i in range(len(word)):
    char = word[i]
    new_word = char * (i + 1) + word[i + 1:]
    print(new_word)
