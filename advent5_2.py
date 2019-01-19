# task from Day 5, part 2
# https://adventofcode.com/2018/day/5


finallist = []

def polymer_reactor(listinn):
    has_changed = 1
    i = 0
    while has_changed == 1:
        has_changed = 0
        while i < len(listinn)-1:
            if abs(ord(listinn[i]) - ord(listinn[i+1])) == 32:
                listinn.pop(i)
                listinn.pop(i)
                has_changed = 1
                if i > 0:
                    i -= 1
            else:
                i += 1
    return listinn

def import_text():
    textfile = open("input6.txt", "r")
    return tuple(textfile.read())

def remove_elements(tuple_in):
    polymer_lenght = len(tuple_in)
    print("Total lenght of polymer:", polymer_lenght)
    for i in range(65, 91):
        temp_list = []
        sum_of_chosen_char = tuple_in.count(chr(i)) + tuple_in.count(chr(i+32))
        print("chr(i)=", chr(i), "chr(i+32)=", chr(i+32), sum_of_chosen_char, polymer_lenght - sum_of_chosen_char)
        temp_list = list(tuple_in)
        temp_list = [elem for elem in temp_list if elem not in (chr(i), chr(i+32))]
        cutlistlen = len(temp_list)
        print(cutlistlen)
        reactedlistlen = len(polymer_reactor(temp_list))
        print(reactedlistlen)
        finallist.append((reactedlistlen))


a = import_text()
print(a)
remove_elements(a)
print("shortest polymer has:", min(finallist))


