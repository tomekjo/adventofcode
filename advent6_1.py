# task from Day 6, part 1
# https://adventofcode.com/2018/day/6

import re
from collections import Counter

def import_text():
    dict_of_points = dict()
    textfile = open("input7.txt", "r")
    content = textfile.read()
    listin = content.split('\n')
    points_numbers = 1
    for i in listin:
        x = int(re.findall('([0-9]+),', i)[0])
        y = int(re.findall(', ([0-9]+)', i)[0])
        dict_of_points[x,y] = points_numbers
        points_numbers += 1
    print(dict_of_points)
    return dict_of_points

def find_minmax_points(initial_dict):
    x_min = list(initial_dict.keys())[list(initial_dict.values()).index(1)][0]
    y_min = list(initial_dict.keys())[list(initial_dict.values()).index(1)][1]
    x_max = list(initial_dict.keys())[list(initial_dict.values()).index(1)][0]
    y_max = list(initial_dict.keys())[list(initial_dict.values()).index(1)][1]
    for i in initial_dict.keys():
        if i[0] < x_min:
            x_min = i[0]
        if i[0] > x_max:
            x_max = i[0]
        if i[1] < y_min:
            y_min = i[1]
        if i[1] > y_max:
            y_max = i[1]
    return x_min,x_max, y_min, y_max


def find_boundary_points(initial_dict, minmax):
    list_of_boundary = list()
    for k in initial_dict.keys():
        if k[0] == minmax[0] or k[0] == minmax[1] or k[1] == minmax[2] or k[1] == minmax[3]:
            list_of_boundary.append(k)
    return list_of_boundary


def calculate_distance(tup1, tup2):
    width = abs(tup1[0] - tup2[0])
    hight = abs(tup1[1] - tup2[1])
    distance = width + hight
    # print(tup1, tup2, distance)
    return distance


def find_closest(tup3, pointsDict):
    closest = -1
    minDistance = 100000
    for k,v in pointsDict.items():
        tempDistance = calculate_distance(k, tup3)
        if minDistance == tempDistance:
            closest = 0
        elif minDistance > tempDistance:
            minDistance = tempDistance
            closest = v
    return closest


def fillin_table(pointsDict, minmax):
    finalDict = dict()
    for x in range(minmax[0], minmax[1] + 1):
        for y in range(minmax[2], minmax[3] + 1):
            finalDict[x, y] = find_closest((x,y), pointsDict)
    return finalDict


def final_search(finalDict, minmax):
    infiniteList = list()
    limitedDict = dict()
    for k,v in finalDict.items():
        if k[0] == minmax[0] or k[0] == minmax[1] or k[1] == minmax[2] or k[1] == minmax[3]:
            infiniteList.append(v)
    for k,v in finalDict.items():
        if v not in infiniteList:
            limitedDict[k] = v
    print(limitedDict)
    return max(Counter(limitedDict.values()).values())


dict_of_points = import_text()
table_coordinates = find_minmax_points(dict_of_points)
print(table_coordinates)
print(find_boundary_points(dict_of_points,table_coordinates))
print(final_search(fillin_table(dict_of_points, table_coordinates),table_coordinates))





