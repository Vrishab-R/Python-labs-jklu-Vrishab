words = input().split()
result = []
for w in words:
    if len(w) > 3:
        result.append(w)
print(result)
