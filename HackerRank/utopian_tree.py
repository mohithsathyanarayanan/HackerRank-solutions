n=input()
cycles=list()
initial_length=1
for i in range(n):
    a=input()
    cycles.append(a)
for i in range(len(cycles)):
    for j in range(cycles[i]):
        if(j%2==1):
            initial_length=initial_length+1

        if(j%2==0):
            initial_length=initial_length*2
    print(initial_length)
    initial_length=1


