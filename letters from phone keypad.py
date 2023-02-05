d = str(input(""))

dict = {
    "2" : "abc",
    "3" : "def",
    "4" : "ghi",
    "5" : "jkl",
    "6" : "mno",
    "7" : "pqrs",
    "8" : "tuv",
    "9" : "wxyz"
    }

output = ""

for i in d:
    output += dict.get(i) + " "

for i in output:
    if i == " ":
       oplist1 = output.split()

oplist2 = oplist1[-1]

oplist1.remove(oplist2)

output2 = oplist1[0]

oplist1og = list(map(str, str(output2)))

oplist2og = list(map(str, str(oplist2)))


result = []
for i in oplist1og:
    for j in oplist2og:
        result.append(i)
        result.append(j)

word = ""
finalres = []
for i in result:
    word = result[0] + result[1]
    finalres.append(word)
    del result[0]
    del result[1]
    word = ""
print(finalres)