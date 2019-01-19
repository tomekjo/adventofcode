# task from Day 3, part 2
# https://adventofcode.com/2018/day/3

import re, csv

# loading txt file with data & basic data spliting
textfile = open("input4.txt", "r")
content = textfile.read()
listin = content.split('\n')
len_listin = len(listin)
# print(listin)

# final preparing of data for usage in fibermap
cleaned_list = []
for q in listin:
    li = []
    x_begin = int(re.findall(',(\d+):',q)[0]) + 1
    li.append(x_begin)
    y_begin = int(re.findall('@\s(\d+),',q)[0]) + 1
    li.append((y_begin))
    x_width = int(re.findall('x(\d+)',q)[0])
    li.append(x_width)
    y_hight = int(re.findall('\s(\d+)x',q)[0])
    li.append(y_hight)
    claim_id = int(re.findall('#(\d+)',q) [0])
    li.append(claim_id)
    claim_surface = x_width * y_hight
    li.append(claim_surface)
    cleaned_list.append(li)
# print(cleaned_list)

# finding max width and hight of fabric
max_fabric_hight = 0
max_fabric_width = 0
for i in cleaned_list:
    if max_fabric_hight < i[0] + i[2]:
        max_fabric_hight = i[0] + i[2]
    if max_fabric_width < i[1] + i[3]:
        max_fabric_width = i[1] + i[3]
# print(max_fabric_hight,max_fabric_width)

'''
# saving list to csv file to check the data
with open ('coordinates.csv', 'w') as new_file:
    csv_writer = csv.writer(new_file)
    for line in cleaned_list:
        csv_writer.writerow(line)
'''

# creating fabric table
# i rows, j columns
fabric = dict()
for i in range(max_fabric_hight):
    for j in range(max_fabric_width):
        fabric[(i + 1, j + 1)] = 0
# print(fabric)

# upload values in fabric table according to data in list
for li in cleaned_list:
    for i in range(li[2]):
        for j in range(li[3]):
            fabric[(li[0] + i, li[1] + j)] += 1

# final counting inches of fabric with over 1 value
inch_counter = 0
for k,v in fabric.items():
    if v > 1:
        inch_counter += 1
        # print(k,v)
print("number of inches:", inch_counter)

# selection id claim that doesn't overlap
chosen_id = 0

for li in cleaned_list:
    sum_of_surface = 0
    for i in range(li[2]):
        for j in range(li[3]):
            sum_of_surface += fabric[(li[0] + i, li[1] + j)]
    if sum_of_surface == li[5]:
        chosen_id = li[4]
        break
print("Id of not-overlaped is:", chosen_id)






