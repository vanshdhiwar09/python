num = int(input("Enter the Number"))
flag = False

if num == 1:
    print("is not a Prime number")
elif num > 1:
     for i in range(2,num):
         if(num%i) == 0:
           flag = True 
           break
if flag:
       print(num,"is not a prime Number")
else:
    print(num,"is a prime number")
       
           