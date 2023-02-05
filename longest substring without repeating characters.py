s = input("")

substring = []

for i in range(len(s)):
    substring += s[i]
    if s[i] != s[i+1] and i+1 <= len(s):
        substring += s[i+1]
        i += 1
    else:
        break
        
        

print(substring)
