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

for z in range(1,n+1):
    for j in range(1,(n+1)-z):
        print(' ',end='')
    for k in range(1,z+1):
        if k==1:
            print(a,end='')
            continue
        print(' ',end='')
    for p in range(2,z+1):
        if p==z:
            print(a,end='')
            continue
        print(' ',end='')
    print()


for i in range(1,n+1):
    for j in range(1,i+1):
        print(' ',end='')
    for q in range(1,(n+1)-i):
        if q==1:
            print(a,end='')
            continue
        print(' ',end='')
    for t in range((n-1)-i,0,-1):
        if t==1:
            print(a,end='')
            continue
        print(' ',end='')
    print()
