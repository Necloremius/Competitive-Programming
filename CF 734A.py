x = int(input())
b = list(input())
if b.count("A") > b.count("D"):
    print("Anton")
elif b.count("A") < b.count("D"):
    print("Danik")
else:
    print("Friendship")
