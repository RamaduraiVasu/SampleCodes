#This is the program to find the factorial of a given number

#First We need to accept a number from user

n=int(input("Enter a Number"))

#number should be greater than or equal to 0 to find the factorial or else display error messgae

if n>=0:
    f:int =1
    for i in range(1,n+1):
        f=f*i # can be writen as f*=i
    print(f"Factorial of {n} is {f}")
else:
    print("Invalid Input")
