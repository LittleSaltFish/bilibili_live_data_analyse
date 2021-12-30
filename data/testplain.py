import json

def extract(front,dic):
    input=[]
    output=[]
    for key,value in dic.items():
        input.append([key,value])
    while(input):
        top=input[-1]
        if type(top[1]).__name__=="dict":
            input=input[:-1]
            input.extend(extract(top[0],top[1]))
        else:
            output.append([f"{front}|{top[0]}",top[1]])
            input=input[:-1]
            # for i in output:
            #     print(output)
    return output


txt="{\"_msg_type\": \"other\", \"_content\": {\"cmd\": \"LIVE_INTERACTIVE_GAME\", \"data\": {\"type\": 1, \"uid\": 385956415, \"uname\": \"工号1001\", \"uface\": \"http://i1.hdslb.com/bfs/face/e2ddc2275df94af1cebf7028aa1bdc1bb30e78f4.jpg\", \"gift_id\": 31036, \"gift_name\": \"小花花\", \"gift_num\": 1, \"price\": 100, \"paid\": \"True\", \"msg\": \"\", \"fans_medal_level\": 0, \"guard_level\": 0, \"timestamp\": 1640693582, \"anchor_lottery\": \"None\", \"pk_info\": \"None\", \"anchor_info\": {\"uid\": 23920239, \"uname\": \"小米公司\", \"uface\": \"http://i0.hdslb.com/bfs/face/398e4b6654bbb64d87f645b9b45591e4f959f6ce.jpg\"}}}}"

js = json.loads(txt)

a=extract("",js)
print(a[0])
tmp={}
for i in a:
    tmp[i[0]]=i[1]
print(tmp)
