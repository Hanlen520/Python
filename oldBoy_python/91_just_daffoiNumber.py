# -*- coding: utf-8 -*-
# by author: Crisimple
# description: just this number is daffoiNumber

input_number = int(input("Please your number: "))


def is_three_daffoi(number):

    return_flag = True

    a = number / 100
    print(a)
    b = (number /10 ) % 10
    print(b)
    c = number % 10
    print(c)

    if  (a**3 + b**3 + c**3) != number:
        # return_flag = False
        print("不是")
    else:
        # return_flag
        print("是")

    return return_flag

is_three_daffoi(input_number)



def is_daffoi(num):
    # sum = 0
    # while num in range(100, 1000):
    #
    #     num_length = len(str(num))
    #     a = num % 10
    #     sum += a**num_length
    #     num = num // 10
    #     return sum
    #
    #     if sum == num:
    #         print("is")
    #     else:
    #         print("is not")
    for i in range(10,1000):
        sum=0 #各个位数的立方和
        temp=i
        while temp:
            sum=sum+(temp%10)**3   #累加
            temp//=10   #地板除
        if sum==i:
            print(i)

# is_three_daffoi(input_number)