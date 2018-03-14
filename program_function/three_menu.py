# -*- coding: utf-8 -*-
# by author: Crisimple
# description:
"""
    可依次选择进入各子菜单
    可从任意一层往回退到上一层
    可从任意一层退出程序
    所需新知识点：列表、字典
"""

menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youKu':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}

# 将地区的字典复制给choice_layer
choice_layer = menu
flag = False
layers = [menu]

while not flag:
    for i in choice_layer:
        print("YOUR ADDRESS MUST TO CHOICE:".center(50, "-"),i)

    address_choice = input("PLEASE CHOICE YOUR ADDRESS>>>>>>>:").strip()

    if address_choice == "b":
        print("ATTENTION: <<<<<<<<<<<<<<-YOU HAVE GOT GO BACK NOW.")
        choice_layer = layers[-1]
        layers.pop()
    elif address_choice not in choice_layer: continue
    else:
        layers.append(choice_layer)
        choice_layer = choice_layer[address_choice]

    if address_choice == "b":
        print("ATTENTION: <<<<<<<<<<<<<<-YOU HAVE GOT GO BACK NOW.")
        choice_layer = layers[-1]
        layers.pop()


