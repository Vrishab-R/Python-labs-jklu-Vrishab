n = int(input("Enter number of elements: "))
a = []

for i in range(n):
    x = int(input("Enter element: "))
    a = a + [x]

total = 0

for i in range(len(a)):
    total = total + a[i]

print("Sum =", total)
