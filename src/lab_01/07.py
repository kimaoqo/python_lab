from string import *
string = input()
f_1 = f_2 = 1
f_char = s_char = 0
l_char = string.find('.')
for i in range(0,len(string) - 1):
    if string[i] in ascii_uppercase and f_1 == 1:
        f_char = string[i]
        f_1 = 0
    if string[i] in digits and f_2 == 1:
        s_char = string[i + 1]
        f_2 = 0
    if f_char != 0 and s_char != 0:
        step = abs(string.find(s_char) - string.find(f_char))

cursor = string.find(f_char)
source = ''
while cursor <= l_char:
    source += string[cursor]
    cursor += step

print(source)