n1 = int(input(""))

n1_list = list(map(int, str(n1)))

n2 = int(input(""))

n2_list = list(map(int, str(n2)))

n1list_sort = sorted(n1_list)

n2list_sort = sorted(n2_list)

nlist = n1list_sort + n2list_sort

sum = 0

for i in range(len(nlist)):
    sum += int(nlist[i])

median = sum / len(nlist)

print(median)