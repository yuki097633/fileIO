import json

with open("example.json")as f:
    data = json.load(f)

print(data["glossary"]["title"])


new_json = {"key1": "val1", "key2": (1, "val2")}
with open("new_json.json", mode="w") as f:
    json.dump(new_json, f)

with open("new_json.json", mode="r") as f:
    new_reload = json.load(f)

print(new_reload)

# 文字列にできる
json_str = json.dumps(new_json)
print(json_str)

# 文字列からpythonのデータ構造にできる
python_data = json.loads(json_str)
print(python_data)

