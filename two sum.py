n = input("")

nums = list(map(int, str(n)))

target = int(input(""))

output = []
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            output.append(i)
            output.append(j)
            print(output)
            break

#we should give the input in such a way that it only should have one solution