l1 = int(input(""))
l2 = int(input(""))

list1 = list(map(int, str(l1)))
list2 = list(map(int, str(l2)))

listfinal = list1 + list2

listog = sorted(listfinal)

print(listog)