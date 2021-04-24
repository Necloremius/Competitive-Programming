k,n,w = input().split()
k,n,w = int(k),int(n),int(w)
cost = 0
for x in range(w+1):
    cost += x*k
if n<cost:
    print(cost-n)
else:
    print(0)
