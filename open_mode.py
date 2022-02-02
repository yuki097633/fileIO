# mode = "a"(append) ファイルの最後尾に内容を追加
# with open("writing_file.txt", mode="a") as f:
#     f.write("append!!!!")

# mode = "r+" 読み書きどちらも可能
# with open("writing_file.txt", mode="r+") as f:
#     f.write("mode f+++")
#     print(f.read())

# mode = "w+" 読み書きどちらも可能
# Truncateされる　開いたファイルは全て置き換えられる
# with open("writing_file.txt", mode="w+") as f:
#     print(f.read())
#     f.write("w+ dayo")
#     f.seek(0)
#     print(f.read())

# mode = "a+" 読み書きどちらも可能
# Truncateされない　positionが最後尾からになる
with open("writing_file.txt", mode="a+") as f:
    print(f.read())
    f.write("a+ dayo")
    print(f.read())
