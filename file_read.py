# # for loop
# with open("pep8_introduction.txt") as f:
#     for line in f:
#         print(line, end="")

# .readでファイルの中身の全てを一つのstring
# 大きなファイルでやらないように注意
# with open("pep8_introduction.txt") as f:
#     print(f.read())

# # .readline()一行ずつ取得しstringで返す
# with open("pep8_introduction.txt") as f:
#     line = f.readline()
#     while line:
#         print(line, end="")
#         line = f.readline()

# .readlines()で全ての行をlistで返す
with open("pep8_introduction.txt") as f:
    lines = f.readlines()
    print(lines)