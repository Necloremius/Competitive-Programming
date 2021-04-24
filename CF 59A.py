word = str(input())
upper_list = []
lower_list = []
for x in word:
    if x.isupper():
        upper_list.append(x)
    else:
        lower_list.append(x)
if len(upper_list) > len(lower_list):
    print(word.upper())
else:
    print(word.lower())
