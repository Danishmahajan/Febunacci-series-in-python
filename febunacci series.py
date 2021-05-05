# Febunacci series =0  1  1  2  3  5  8  13
def febonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return  febonacci(n-1) + febonacci(n-2)


def febunacci_series(n):
    x=0
    y=1
    z=0
    while (z<=n):
        print(z)
        x=y
        y=z
        z=x+y

number= int(input("Enter the number"))
print("Febunacci of",number," is" , febonacci(number))
print("The series  is given below :")
febunacci_series(number)