n = int(input())
m = int(input())
i = 1

# code here
while i <= n:
    j = 1
    while j <= m:
        if i == 1 or i ==n or j ==1 or j ==m:
            print("*", end="")
        else:
            print(" ", end="")
        j += 1
    print()
    i +=1
    