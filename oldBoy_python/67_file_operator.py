# -*- coding: utf-8 -*-
# by author: Crisimple
# description: file operator

import sys
import time

# mo fang jin du tiao

for i in range(30):
    sys.stdout.write("*")
    time.sleep(0.1)

print("\n")

f = open("./file_operator.txt", encoding="utf-8")

number = 0
for line in f:
    number += 1
    if number == 2:
        line = line.strip() + "...\n"
    print(line)

f.close



