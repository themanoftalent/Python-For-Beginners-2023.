#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#


def faktor(sayi):
    fak=1


    for numara in range(1,sayi+1):
        fak*=numara


    return fak


bb=faktor(5)
print(bb)