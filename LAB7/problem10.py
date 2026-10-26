s = input("Enter hyphen-separated words: ")

words = s.split("-")

for i in range(len(words)):
    for j in range(i + 1, len(words)):
        if words[i] > words[j]:
            temp = words[i]
            words[i] = words[j]
            words[j] = temp

result = ""

for i in range(len(words)):
    if i > 0:
        result = result + "-"
    result = result + words[i]

print(result)
