def pal(s):
    s = s.lower()
    s = ''.join(char for char in s)
    return s == s[::-1]

print(pal(input()))