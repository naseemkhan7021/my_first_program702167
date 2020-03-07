# print
#       *
#      * *
#     *   *
#    *     *
#   *       *
#  *         *
# *           *
#*             *
# *           *
#  *         *
#   *       *
#    *     *
#     *   *
#      * *
#       *
n=int(input('entar number of row = '))
a=input('entar your sape that you like = ')
i=1
while i<=n:
    j=1
    while j<=(n+40)-i:
        print(' ',end='')
        j+=1
    k=1
    while k<=i:
        if k==1:
            print('*',end='')
        else:
            print(' ',end='')
        k+=1
    l=i-1
    while l>=1:
        if l==1:
            print('*',end='')
        else:
            print(' ',end='')
        l-=1
    print()
    i+=1

z=1
while z<=n:
    j=1
    while j<=z+39:
        print(' ',end='')
        j+=1
    k=n
    while k>=z:
        if k==n:
            print('*',end='')
        else:
            print(' ',end='')
        k-=1
    x=n-1
    while x>=z:
        if x==z:
            print('*',end='')
        else:
            print(' ',end='')
        x-=1
    print()
    z+=1
        
