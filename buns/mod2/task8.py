s = input()
for i in range(len(s)):
    if s[i] == " ":
        break
a = s[:i-1]
b = s[-1]
count = 0
for i in a:
# Идём по строке, пока не встретим символ отличающийся от b
    if i == b:
        count += 1
    else:
        break
print(count)