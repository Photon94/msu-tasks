
def solve(list):
    for i in range(len(list)-1):
        lower_index = i
        for j in range(i+1, len(list)):
            if list[j] < list[lower_index]:
                lower_index = j

        saved_num = list[i]
        list[i] = list[lower_index]
        list[lower_index] = saved_num

    return list

print(solve(p))

string = p
substring = "[]"
count = string.count(substring)
print (count)

n=p[::-1]
print(n)

def minimum(x):
    x = sorted(x)
    return x[0]

def maximum(x):
    x = sorted(x)
    return x[-1]

print(minimum(p))
print(maximum(p))

lst = p
lst1 = []
for i in lst:
    if i not in lst1:
        lst1.append(i)
print(lst1)

def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

print(listsum(p))
