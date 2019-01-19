# task from Day 4, part 2
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

# finding which guard is most frequently asleep on the same minute
most_sleepy_minute = 0
quantity_of_sleeps = 0
chosen_guard = 0

for k,v in guards_dict.items():
    print(k,v)
    list_of_minutes = []
    for i in range(60):
        list_of_minutes.append(0)
    guard_minuts_asleep = 0

    for j in v:
        guard_minuts_asleep += j[1] - j[0]
        for qq in range(j[0], j[1]):
            list_of_minutes[qq] += 1
    print("Guard no:", k, "slept minutes:", guard_minuts_asleep)
    print("the most sleepy minute is:", list_of_minutes.index(max(list_of_minutes)), "with quantity of:", max(list_of_minutes))

    if max(list_of_minutes) > quantity_of_sleeps:
        most_sleepy_minute = list_of_minutes.index(max(list_of_minutes))
        chosen_guard = k
        quantity_of_sleeps = max(list_of_minutes)

print("The most sleepy minute:", most_sleepy_minute)
print("The quantity of asleep:", quantity_of_sleeps)
print("The id guard is:", chosen_guard)

print("Result of exercise is:", int(chosen_guard) * most_sleepy_minute)

