num = input("Please write a number")
if num.isnumeric():
    num=int(num)
    if num % 2==0:
        print (f"The number {num} is even")
    else: 
        print (f"The number {num} is odd")

else:
    print ("Error")