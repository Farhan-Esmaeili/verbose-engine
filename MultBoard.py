#input
x = int(input("Enter x : "))
y = int(input("Enter y : "))
#intializing and output
def mult(x,y) :
    for n in range(x+1):
        if (n+1) != (x+1) :
            print((n), end=" ")
        else :
            print((n), end="\n")
    mult = 1
    for m in range(y):
        print((m+1),end=" ")
        for i in range(x):
            if (i+1) != x :
                print((i+1)*mult, end=" ")
            else :
                print((i+1)*mult, end="\n")
        mult += 1

mult(x,y)