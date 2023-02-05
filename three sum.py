n = int(input(""))

n_list = list(map(int, str(n)))

a = []
b = []
c = []

for i in range(len(n_list)):
    for j in range(len(n_list)):
        for k in range(len(n_list)):
            