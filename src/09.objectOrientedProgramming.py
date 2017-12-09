#!/usr/bin/evn python
# -*- coding:utf-8 -*-
# by author: crisimple

# 九.面向对象编程
# 数据封装、继承和多态是面向对象的三大特点


# ======================================================================================================================
# 9.1.1.类和实例
class Student(object):

    # 在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def print_message(self):
        print('%s: %s' % (self.__name, self.__age))

    def judge_age(self):
        if self.__age >= 30:
            return '中年'
        elif self.__age >= 20:
            return '青年'
        else:
            return '少年'

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        if name != '':
            self.__name = name
        else:
            raise ValueError("your name is wrong, please check your name")

    def set_age(self, age):
        if 0 <= age <= 130:
            self.__age = age
        else:
            raise ValueError("error age, please check your input")


# ↓↓↓↓↓↓↓实例↓↓↓↓↓↓↓↓
instance_people = Student('crisimple', 23)


# 特点一：数据封装
instance_people.print_message()
print(instance_people.get_name())


# ----------------------------------------------------------------------------------------------------------------------
# 9.1.2.访问限制
instance_people.age = 24
print(instance_people.get_age())


# ======================================================================================================================
# 9.3.1.继承和多态
class Animal(object):

    def run(self):
        print("Animal is running")


class Dog(Animal):

    def run(self):
        print("Dog is happy run")

    def eat(self):
        print("Dog eats meat")


# 9.3.2.多态--polymorphic
def run_twice(animal):
    animal.run()


run_twice(Animal())
run_twice(Dog())


# ======================================================================================================================
# 9.4.获取对象信息
# 9.4.1.使用type()
