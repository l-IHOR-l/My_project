roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
reverse_roman_num = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
[print(f"{v}:'{k}',", end=' ') for k, v in roman_num.items()]
print()
s = "MCMXCIV"
a = 0

for i in range(1, len(s)):
    if int(roman_num[s[i]]) > int(roman_num[s[i - 1]]):
        a -= roman_num[s[i - 1]]
    else:
        a += roman_num[s[i - 1]]
a += roman_num[s[-1]]

print(a)
