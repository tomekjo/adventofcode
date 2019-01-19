# task from Day 5, part 1
# https://adventofcode.com/2018/day/5

# loading txt file with data
textfile = open("input6.txt", "r")
content = textfile.read()
listin = list(content)
print(len(listin), listin)

has_changed = 1
i = 0
while has_changed == 1:
    has_changed = 0
    while i < len(listin)-1:
        if abs(ord(listin[i]) - ord(listin[i+1])) == 32:
            listin.pop(i)
            listin.pop(i)
            has_changed = 1
            if i > 0:
                i -= 1

        else:
            i += 1

print(len(listin), listin)
