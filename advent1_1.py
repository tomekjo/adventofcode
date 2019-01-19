# task from Day 1, part 1
# https://adventofcode.com/2018/day/1


textfile = open("input.txt", "r")
content = textfile.read()
numlist = content.split()
print(numlist)
sum = 0

for i in numlist:
    sum += int(i)

print(sum)

