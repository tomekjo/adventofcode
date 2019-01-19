# task from Day 2, part 1
# https://adventofcode.com/2018/day/2

from collections import Counter

textfile = open("input3.txt", "r")
content = textfile.read()
listin = content.split()
print(len(listin), listin)

counter2 = 0
counter3 = 0
result = 0

for i in listin:
    a = list(i)
    b = Counter(a)
    if 2 in b.values():
        counter2 += 1
    if 3 in b.values():
        counter3 += 1

print('counter of 2:', counter2)
print('counter of 3', counter3)

result  = counter2 * counter3
print('result', result)