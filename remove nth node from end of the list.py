n = int(input(""))

head = int(input(""))

head_list = list(map(int, str(head)))

res = (len(head_list) - n)

del head_list[res]
    

print(head_list)

