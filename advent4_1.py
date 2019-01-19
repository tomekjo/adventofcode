# task from Day 4, part 1
# https://adventofcode.com/2018/day/4

import re

# loading txt file with data & sorting final list by date & time
textfile = open("input5.txt", "r")
content = textfile.read()
listin = content.split('\n')
print(len(listin))
print(listin)
listsorted = sorted(listin)
print(listsorted)

# input data to dict of guards where guard id is a key and time of being asleep are values of dict
guards_dict = {}
li = []
for i in listsorted:
    if 'Guard' in i:
        guardID = re.findall('#([0-9]+) ', i)[0]
        if guardID not in guards_dict.keys():
              guards_dict[guardID] = []
    elif 'falls asleep' in i:
        nap_start = int(re.findall(':([0-9]+)]', i)[0])
    elif 'wakes up' in i:
        nap_end = int(re.findall(':([0-9]+)]', i)[0])
        li = guards_dict[guardID]
        li.append((nap_start, nap_end))
        nap_start = 0
        nap_end = 0
        guards_dict[guardID] = li
    else:
        print('sth went wrong')
        break

# calculating minutes of being asleep and choosing guard who slept the most
chosen_guard = 0
max_minuts_asleep = 0
for k,v in guards_dict.items():
    print(k,v)
    guard_minuts_asleep = 0
    for i in v:
        guard_minuts_asleep += i[1] - i[0]
    if guard_minuts_asleep > max_minuts_asleep:
        max_minuts_asleep = guard_minuts_asleep
        chosen_guard = k
print('The most sleepy guard is:',chosen_guard,'that slept minutes:', max_minuts_asleep)

# finding the most sleepy minute
list_of_minutes = []
for i in range(60):
    list_of_minutes.append(0)

for j in guards_dict[chosen_guard]:
    for k in range(j[0], j[1]):
        list_of_minutes[k] += 1

most_sleepy_minute = list_of_minutes.index(max(list_of_minutes))
print("The most sleepy minute:", most_sleepy_minute)

print("Result of exercise is:", int(chosen_guard) * most_sleepy_minute)

