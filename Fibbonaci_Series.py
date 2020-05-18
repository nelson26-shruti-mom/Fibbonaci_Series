
#This code gives an extra output

#The Fibonacci numbers are the numbers in the following integer sequence.
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..

n=int(input("Enter an input ="))
a=0
b=1
print(a,b, end=" ")
for i in range (n):
    c=a+b
    print(c, end=" ")
    a=b
    b=c

#print("Nelson")
#print("Advik", end= " ")