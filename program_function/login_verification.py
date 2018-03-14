# -*- coding: utf-8 -*-
# by author: jiangheng
# description:

_userName = "Crisimple"
_passWord = "159357"

# user_list = ["A", "B"]
# passWord_list = ["123", "321"]
users_info = [
    ["A", "123"],
    ["B", "456"],
    ["C", "789"]
]

# 定义一个标志位计数
number = 0
times = 3

# 认证成功的标志位
pass_auth_flag = False

first_input_user = None
is_same_name = True

f = open("locked_user", "r")
locked_users = []
for line in f:
    locked_users.append(line.strip())

# 判断次数
while number < times:

    # 输入用户名密码
    userName = input("Please input your name: ").strip()
    passWord = input("Please input your password: ").strip()

    if userName in locked_users:
        exit("This user is locked, please check your user name.")

    if not first_input_user:
        first_input_user = userName

    # 代表本次输入的用户名，跟第一次相同
    if userName != first_input_user:
        is_same_name = False


    # 验证用户名和密码的正确性
    for user in users_info:
        if userName == user[0] and passWord == user[1]:
            print("Hello %s, welcome to your home page." % userName)
            pass_auth_flag = True
            break
    else:
        print("userName or passWord is wrong, please check!")

    # 登陆成功用标志位来决定程序退出
    if pass_auth_flag :
        break

    # 登陆次数的限制
    number += 1

    if number == 3:
        continue_choice = input("Do you want to continue?[y/n]")
        if continue_choice == "y":
            number = 0

else:
    print("Don't try again...")