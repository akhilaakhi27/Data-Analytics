row=10
for i in range(1,row+1):
    for j in range(1,row+1):
        print(i*j,end=" ")
    print(" ")
    
#create a fn tht takes a string as input return no of vowels

s=str(input("Enter a string"))
def v(s):
    S=["a","e","i","o","u","A","E","I","O","U"]
    c=0
    for i in s:
        if i in S:
           c=c+1
    return c
print(v(s))
