# -*- coding: utf-8 -*-
# by author: Crisimple
# description:

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
                '优酷':{},
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
            '火车站':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}



exit_flag = False
current_layer = menu
layers = [menu]

while not exit_flag:

    for i in current_layer:
        print("YOUR ADDRESS MUST TO CHOICE:".center(50, "-"),i)

    address_choice = input("PLEASE CHOICE YOUR ADDRESS>>>>>>>:").strip()

    if address_choice == "b":
        print("ATTENTION: <<<<<<<<<<<<<<-YOU HAVE GOT GO BACK NOW.")
        current_layer = layers[-1]
        layers.pop()
    elif address_choice not in current_layer: continue
    else:
        layers.append(current_layer)
        current_layer = current_layer[address_choice]

    if address_choice == "b":
        print("ATTENTION: <<<<<<<<<<<<<<-YOU HAVE GOT GO BACK NOW.")
        choice_layer = layers[-1]
        layers.pop()














