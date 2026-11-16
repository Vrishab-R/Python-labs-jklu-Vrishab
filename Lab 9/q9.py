n = int(input())
seen = {}
for i in range(n):
    first, last = input().split()
    name = first.lower() + "." + last.lower()
    if name in seen:
        seen[name] += 1
        print(name + str(seen[name]) + "@jklu.edu.in")
    else:
        seen[name] = 1
        print(name + "@jklu.edu.in")
