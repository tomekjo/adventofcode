# task from Day 2, part 2
# https://adventofcode.com/2018/day/2

textfile = open("input3.txt", "r")
content = textfile.read()
listin = content.split()
print(len(listin), listin)
listlist = []
mismatched_no = 0
result1 = []
result2 = []

for i in listin:
    listlist.append(list(i))
print(len(listlist), listlist)


for i in range(249):
    n = i + 1
    for n in range(250):
        for q in range(26):
            if listlist[i][q] != listlist[n][q]:
                mismatched_no += 1
            if mismatched_no == 2:
                mismatched_no = 0
                break
        if mismatched_no == 1:
            result1 = listlist[i]
            result2 = listlist[n]
        else:
            mismatched_no = 0

print('First list found:', result1)
print('Second list found', result2)


