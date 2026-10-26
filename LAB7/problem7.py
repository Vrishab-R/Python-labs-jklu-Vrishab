s = input("Enter a string: ")

i = 0
j = len(s) - 1
flag = 1

while i < j:
    if s[i] != s[j]:
        flag = 0
        break
    i = i + 1
    j = j - 1

if flag == 1:
    print("Palindrome")
else:
    print("Not a palindrome")
