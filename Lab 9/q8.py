s = input()
digits = []
for ch in s:
    if ch.isdigit():
        digits.append(int(ch))
print(digits)
print("Sum:", sum(digits))
