s = input("Enter a paragraph: ")

digits = 0
alphabets = 0
uppercase = 0
lowercase = 0
special = 0

for ch in s:
    if ch.isdigit():
        digits = digits + 1
    elif ch.isalpha():
        alphabets = alphabets + 1

        if ch.isupper():
            uppercase = uppercase + 1
        elif ch.islower():
            lowercase = lowercase + 1
    else:
        special = special + 1

print("Digits =", digits)
print("Alphabets =", alphabets)
print("Uppercase =", uppercase)
print("Lowercase =", lowercase)
print("Special characters =", special)
