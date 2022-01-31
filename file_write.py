with open("writing_file.txt", mode="w") as f:
    # trancatedされる　byte=0に切り詰める mode="W"だと上書きされる
    f.write("You can write contents here\nuse backslash")

    print("You can add a new raw", file=f)