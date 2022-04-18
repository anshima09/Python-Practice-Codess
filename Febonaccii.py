print("Program for febonacci series !!!")

num=int(input("Enter the number of terms : "))
a=0
b=1
print(a)
print(b)
for i in range(2,num):
    
    next_num=a+b
    a=b
    b=next_num
    print(next_num)

