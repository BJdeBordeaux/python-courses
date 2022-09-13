import sys
# print(sys.argv, len(sys.argv))

for i in range(1, len(sys.argv)):
    try:
        with open(sys.argv[i], "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"""\n****************\nFile "{sys.argv[i]}" not found\n****************\n""")