s = str(input(""))

s_list = list(map(int, str(s)))

s_set = set(s_list)

s_list_og = list(s_set)

s_list_sorted = sorted(s_list_og)

print(s_list_sorted)