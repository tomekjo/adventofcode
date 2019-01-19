# task from Day 1, part 2
# https://adventofcode.com/2018/day/1

# warning: long execution, probably there is a better solution

textfile = open("input2.txt", "r")
content = textfile.read()
numlist = content.split()

lenght = len(numlist)
print(numlist)

print("quantity:", lenght)

iterator = 0
out_list = set()
result = 0
a = 1

while True:
    print(result, int(numlist[iterator]))
    result += int(numlist[iterator])
    if result in out_list:
        print('Found:', result)
        break
    else:
        out_list.add(result)
        print(len(out_list), result, sorted(out_list))
        iterator += 1
        a += 1

        if iterator == lenght:
            iterator = 0
        if a < 0:
            break

