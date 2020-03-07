#print
#        *
#       * *
#      *   *
#     *     *
#    *       *
#   *         *
#  *           *
# *             *
#*****************

n=int(input('entar number of row = '))
a=input('entar your sape that you like = ')
for i in range(n+1):
    for j in range(1,(n+1)-i):
        print(' ',end='')
    for k in range(1,i+1):
        if k==1 or i==n:
            print(a,end='')
            continue
        print(' ',end='')
    for p in range(2,i+1):
        if p==i or i==n:
            print(a,end='')
            continue
        print(' ',end='')      
    print()
