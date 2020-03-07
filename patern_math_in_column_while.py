#print
#1
#2 6
#3 7 10
#4 8 11 13
#5 9 12 14 15

i=1
while i<=5:
    j=i
    p=1
    z=4
    while p<=i:
        print(j,end=' ')
        j+=z
        z-=1
        p+=1
    i+=1
    print()
