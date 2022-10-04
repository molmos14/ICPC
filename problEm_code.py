import math 

def viajes(N,M):
    x = (N / M)
    if N < M:
         print(1)

    elif x <= .4:
        print(math.floor(x))

    else:
        print(math.ceil(x))

string = input()
string = string.split()
for i in range(len(string)):
    string[i] = int(string[i])
viajes(string[0], string[1])