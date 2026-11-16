menu = input().split()
prices = list(map(int, input().split()))
ordered = input().split()
total = 0
for i in range(len(menu)):
    qty = ordered.count(menu[i])
    if qty > 0:
        cost = qty * prices[i]
        total += cost
        print(menu[i], "x", qty, "=", cost)
print("Total:", total)
