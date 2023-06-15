roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
print(roman_num['I'])
s = "MCMXCIV"
a = 0

for i in range(1, len(s)):
    if int(roman_num[s[i]]) > int(roman_num[s[i-1]]):
        a -= roman_num[s[i-1]]
    else:
        a += roman_num[s[i-1]]
a += roman_num[s[-1]]

print(a)