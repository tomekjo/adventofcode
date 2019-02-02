# task from Day 7, part 1
# https://adventofcode.com/2018/day/7

import re

final_list = list()

def import_text():
    list_of_points = list()
    textfile = open("input8.txt", "r")
    content = textfile.read()
    listin = content.split('\n')
    for i in listin:
        listin2 = []
        x = re.findall('([A-Z]) must', i)[0]
        y = re.findall('([A-Z]) can', i)[0]
        listin2.append(x)
        listin2.append(y)
        list_of_points.append(listin2)
    return list_of_points


def delete_point(somelist, point):
    for i in somelist:
        if point in i:
            i.remove(point)
    return sorted(list(filter(None, somelist)))


def find_point(somelist):
    next_point = str()
    flag = 0
    for i in somelist:
        if flag == 1:
            break
        next_point = i[0]
        for j in somelist:
            if len(j) > 1:
                if j[1] == next_point:
                    flag = 0
                    break
                else:
                    flag = 1
    return next_point


def final_scheme(somelist):
    newlist = somelist
    while len(newlist) > 0:
        point = find_point(newlist)
        final_list.append(point)
        newlist = delete_point(newlist, point)
    print(''.join(final_list))


somelist = sorted(import_text())
final_scheme(somelist)












