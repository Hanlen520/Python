# -*- coding: utf-8 -*-
# by author: Crisimple
# description: 购物车程序

# 商品列表信息
product_list = [
    ("电脑", 1999),
    ("鼠标", 10),
    ("游艇", 20),
    ("美女", 998)
]

# 数据库已存在的用户信息
users_info = [
    ["A", "123"],
    ["B", "456"],
    ["C", "789"]
]

# 定义空的列表充当空购物车
shopping_cart = []


userName = input("Please input your name: ").strip()
passWord = input("Please input your password: ").strip()

for user in users_info:
    if userName == user[0] and passWord == user[1]:
        print("Hello %s, welcome to your shopping time.".center(50, "=") % userName)

        salary = input("Please input your salary: ")

        if salary.isdigit():
            salary = int(salary)
            while True:
                # 打印商品列表
                for i, v in enumerate(product_list):
                    print(i, ">>>>", v)

                choice = input("Please choice your like product number[or q]: ")

                if choice.isdigit():
                    choice = int(choice)

                    if (choice > 0) and (choice <= len(product_list)):
                        # 允许用户根据商品编号购买商品
                        product = product_list[choice]
                        # 钱够才能买
                        if product[1] < salary:
                            shopping_cart.append(product)
                        else:
                            print("Your salary is not enough, you have %s money" %salary)
                        salary -= product[1]
                        print(product)
                    else:
                        print("Sorry, your choice dose not existed.")

                elif choice == "q":
                    # 可随时退出，退出时，打印已购买商品和余额
                    print("You have got this".center(50, "="))
                    for i in shopping_cart:
                        print(i)
                    print("Your have $%s now" % salary)
                    break
                else:
                    print("Please check the number of your choice.")

        break
else:
    print("userName or passWord is wrong, please check!")






