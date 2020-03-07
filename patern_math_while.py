#print
#1
#2 3
#4 5 6
#7 8 9 10
#11 12 13 14 15

i=1  
z=1
while z<=5:            #z=1, #z=2   #,z=3     #z=4          #z=5
    j=i                #j=1, #j=2,  #,j=4     #j=7          #j=11
    p=1                 #1      ,1
    while p<=z:         #1<=1 #1<=2, #1<=3    #1<=4,        #1<=5
        print(j,end=' ') #print 1..2,3...4,5,6...7,8,9,10..11,12,13,14,15
        j+=1              #increasing velue
        p+=1
    print()
    print()
    i+=z   #increasing velue   #i=2,  #i=4   #i=7  #i=11
    z+=1   #increasing velue   #z=2,  #z=3   #z=4  #z=5
     
