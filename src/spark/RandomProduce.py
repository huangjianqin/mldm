# -*- coding: utf-8 -*-
import random

if __name__ == "__main__":
    file = open("../data.txt","w")
    for i in range(0, 20000):
        js = 30
        content = random.randint(0,js).__str__()
        for j in range(1, js):
            content += " " + random.randint(1, js).__str__()
        file.write(content + "\n")
    file.close()