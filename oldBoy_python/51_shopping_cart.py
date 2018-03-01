# -*- coding: utf-8 -*-
# by author: Crisimple
# description: 列表 切片 内置方法 列表的嵌套


print("Welcome to your shopping times...")

product_list = [
    ("Mix2S", 3),
    ("Tesla", 9),
    ("Cloth", 1)
]

salary = input("Please input your salary: ")
shopping_cart = []  # define a blank list to accept the product that you have got

if salary.isdigit():
    salary = int(salary)
    while True:

        # print the list of the product
        for i, v in enumerate(product_list, 1):
            print(i, "====", v)

        # let the customer to choice product and buy it
        choice = input("Please choice your like product number[or q]: ")

        if choice.isdigit():

            choice = int(choice)

            # just customer's choice in correct scope
            if (choice > 0) and (choice <= len(product_list)):

                # take out the product that customer have choice
                p_item = product_list[choice-1]

                # if your input salary is enough, then you can buy it and add it to your shopping cart
                if p_item[1] < salary:
                    shopping_cart.append(p_item)
                else:
                    print("Your salary is not enough, you have %s money" %salary)
                salary -= p_item[1]
                print(p_item)
            else:
                print("Sorry, your choice dose not existed.")

        elif choice == "q":
            print("you have got this".center(50, "="))
            for i in shopping_cart:
                print(i)
            print("your have $%s now" % salary)
            break

        else:
            print("Please check the number of your choice.")



