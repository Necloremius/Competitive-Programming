a = int(input())
x = str(input())
count = 0
for char in range(a-1):
    if x[char] == x[char+1]:
        count+=1
print(count)
