n = int(input("Enter number of elements: "))
a = []

for i in range(n):
    x = int(input("Enter element: "))
    a = a + [x]

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] < a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

print("Descending order:")

for i in range(len(a)):
    print(a[i], end=" ")
