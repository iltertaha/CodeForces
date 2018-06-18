inp=input()
b=str(inp)

def digit_differ(x):
    a=str(x)
    flag=1
    for i in range(4):
        for j in range(4):
            if i!=j:
                if a[i]==a[j]:
                    return 0
    return 1


inp=inp+1
while True:
    if digit_differ(inp):
        break
    inp=inp+1

print inp
