limak,bob = input().split()
limak, bob = int(limak),int(bob)
years = 0
while True:
    years+=1
    limak *= 3
    bob *= 2
    if limak > bob:
        print(years)
        break
