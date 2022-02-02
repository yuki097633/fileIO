import csv

# csv.reader(f)
# with open("example.csv") as f:
#     reader = csv.reader(f)
#     for line in reader:
#         print(line[1])

# csv.Dictreader(f)　一行目をキーと認識する
# with open("example.csv") as f:
#     reader = csv.DictReader(f)
#     for line in reader:
#         print(line["Country"])

# csv.writer(f)
# with open("sample.csv", mode="w") as f:
#     writer = csv.writer(f)
#     writer.writerow(["value1", "value2"])
#     writer.writerow(["value3", "value4"])

# csv.Dictwriter(f)
with open("sample.csv", mode="w") as f:
    writer = csv.DictWriter(f, ["col1", "col2"])
    writer.writeheader()
    writer.writerow({"col1": "val1", "col2": "val3"})
