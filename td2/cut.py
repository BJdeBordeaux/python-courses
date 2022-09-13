import sys
from termios import VREPRINT
# assertion for hypothesis
assert(len(sys.argv) == 6)
assert(sys.argv[1] == "-d")
assert(sys.argv[3] == "-f")

# variables
max_char_per_line = 255

# get the delimiter
delimiter = sys.argv[2]
file_to_cut = sys.argv[5]

fetch_list = sys.argv[4]
fetch_list_split = fetch_list.split(",")
ftab = set()
for i in range(len(fetch_list_split)):
    try:
        # a single number
        ftab.add(int(fetch_list_split[i]))
    # patterns like "5-", "-11" or "5-11", 
    # # but ... well we do not have time, so we just implement the last one
    except ValueError:
        # a range
        local_fetch = fetch_list_split[i].split("-")
        for j in range(int(local_fetch[0]), int(local_fetch[1])+1):
            ftab.add(j)

        # print("Wrong format.\n eg. python3 cut.py -d , -f 1-3,5,7-9 file.txt")
    # except ValueError:
    #     try:
    #         local_fetch = fetch_list_split[i].split('-')
    #         if len(local_fetch) != 2:
    #             raise ValueError
    #         # like "-11"
    #         if len(local_fetch):
    #             # fetch_table = [True if i >=  int for i in range(int(fetch_list_split[i][:-1]))]
    #     except ValueError:
    #         print("Invalid pattern: " + fetch_list_split[i])
    #         exit(1)
ftab = sorted(ftab)

try:
    with open(file_to_cut, "r") as f:
        for line in f:
            line_list = line.split(delimiter)
            exist_list = [a-1 for a in ftab if a-1 <= len(line_list)-1]
            res_line = delimiter.join([line_list[i] for i in exist_list])
            print(res_line, end="")
except FileNotFoundError:
    print(f"""\n****************\nFile "{file_to_cut}" not found\n****************\n""")