#!/usr/bin/evn python
# -*- coding:utf-8 -*-
# by author: crisimple

# 九.面向对象编程
# 数据封装、继承和多态是面向对象的三大特点


# ======================================================================================================================
# 9.1.1.类和实例
class Student(object):

    # 在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身
    # 定义一个特殊的__init__方法，在创建实例的时候，就把name，age等属性绑上去
    # 类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。
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
# 通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
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
print(type('str'))
print(type(123))
print(type(abs))
print(type(Animal))


# 9.4.2.使用isinstance()--一个对象是否是某种类型
print(isinstance(instance_people, Student))


# 9.4.3.使用dir()--获得一个对象的所有属性和方法
print(dir('ABC'))


# getattr()
# setattr()
# hasattr()
class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()
# 这个对象有没有这个属性
print(hasattr(obj, 'x'))
print(obj.x)
# 设置一个属性
setattr(obj, 'y', 19)
# 获取这个属性
getattr(obj, 'y')
print(obj.y)


# ======================================================================================================================
# 实例属性和类属性



