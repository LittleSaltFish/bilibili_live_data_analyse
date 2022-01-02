import json

m = {"name": "", "content": "{\"code\":0}", "msg_type": "other",
     "Date": "2021.12.31", "ExactTime": "16:51:13", "DeltaTime": "0.55"}

# print(type(m["msg_type"]).__name__)
for key, value in m.items():
    if type(value).__name__ == "bytes":
        m[key] = m[key].decode()
        print(m[key])
    if type(value).__name__ == "str":
        m[key] = m[key].replace(",", "_")

# data = json.dumps(m, ensure_ascii=False)
# print(data)
data = json.dumps(m, indent=4, separators=(',', ':'), ensure_ascii=False)
print(data)
