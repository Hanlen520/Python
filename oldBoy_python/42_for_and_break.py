# -*- coding: utf-8 -*-
# by author: Crisimple
# description: 登陆程序,如果登陆三次错误的话账号锁定

_userName = "Crisimple"
_passWord = "159357"
# passed_authentication = False
#
# for i in range(3):
#     userName = input("userName: ")
#     passWord = input("passWord: ")
#     if userName == _userName and passWord == _passWord:
#         print("Welcome %s login..." %_userName)
#         passed_authentication = True
#         break
#     else:
#         print("Invalid userName or password!")
#
# if not passed_authentication:
#     print("要不要小流氓,还想盗取我的账号?")

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# for i in range(3):
#     userName = input("userName: ")
#     passWord = input("passWord: ")
#     if userName == _userName and passWord == _passWord:
#         print("Welcome %s login..." %_userName)
#         break
#     else:
#         print("Invalid userName or password!")
# else:
#     print("要不要小流氓,还想盗取我的账号?")

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
counter = 0
while counter < 3:
    userName = input("Please input your name: ")
    passWord = input("Please input your password: ")

    if userName == _userName and passWord == _passWord:
        print("Hello %s, welcome to your home page." % _userName)
        break
    else:
        print("Invalid userName or passWord!")
    counter += 1
    if counter == 3:
        keep_going_choice = input("还想玩么?[y/n]")
        if keep_going_choice == "y":
            counter = 0

else:
    print("要不要脸小流氓,还想盗取我的账号?")



# 取0-100之间的奇数
# for i in range(1, 100, 2):
#     print(i)
#
# for i in range(1, 100):
#     if i % 2 == 1:
#         print(i)