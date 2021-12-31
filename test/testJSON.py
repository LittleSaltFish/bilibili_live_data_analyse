import json

m = {"name": " ", "content": b'{"code":0}', "msg_type": "为ot,her",
       "Date": "2021.12.30", "ExactTime": "19:34:43", "DeltaTime": 0.18}

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
