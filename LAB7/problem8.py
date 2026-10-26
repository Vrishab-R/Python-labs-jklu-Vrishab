'''n = int(input("Enter number of elements: "))
a = []

for i in range(n):
    x = int(input("Enter element: "))
    a = a + [x]

total = 0

for i in range(len(a)):
    total = total + a[i]

print("Sum =", total)'''


'''
n = int(input("Enter number of elements: "))
a = []

for i in range(n):
    x = int(input("Enter element: "))
    a = a + [x]

product = 1

for i in range(len(a)):
    product = product * a[i]

print("Product =", product)

'''
n = int(input("Enter number of elements: "))
a = []

for i in range(n):
    x = int(input("Enter element: "))
    a = a + [x]

smallest = a[0]

for i in range(1, len(a)):
    if a[i] < smallest:
        smallest = a[i]

print("Smallest element =", smallest)
