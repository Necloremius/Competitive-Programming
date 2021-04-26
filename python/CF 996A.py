a = int(input())
count = 0
for i in [100, 20, 10, 5]:
  d = a // i
  count += d
  a -= i*d
print(count+(a))
