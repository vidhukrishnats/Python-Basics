s = input("")

stack = []

dict = {
    "(" : ")",
    "[" : "]",
    "{" : "}"
}

for i in s:
    if i in dict.keys():
        stack.append(dict[i])
    elif stack[-1] != i:
        print("false")
    else:
        stack.pop()

    if len(stack) == 0:
        print("Valid")
    else:
        print("Invalid")