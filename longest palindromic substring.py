s = input("")

max_word = ""
max_len = 0

for i in range(len(s)):
    for j in range(i+1, len(s)):
        word = s[i:j]
        if word == word[::-1]:
            if max_len < len(word):
                max_len = len(word)
                max_word = word
                print(max_word)