word = list(input())
first_char = word[0]
word.remove(first_char)
word.insert(0,first_char.upper())
print(''.join(word))
