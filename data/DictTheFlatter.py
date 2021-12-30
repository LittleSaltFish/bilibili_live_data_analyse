import json

def extract(front,dic):
    # 递归“解压”字典文件，因为递归进行，所以只能返回数组形式，需要二次处理
    # 输入格式： 多层嵌套的字典
    # 输出格式： 一个[[kay1,value1],[key2,value2]...,[keyN,valueN]]的非嵌套数组
    InStack=[]
    OutStack=[]
    for key,value in dic.items():
        InStack.append([key,value])
    while(InStack):
        top=InStack[-1]
        if type(top[1]).__name__=="dict":
            InStack=InStack[:-1]
            InStack.extend(extract(top[0],top[1]))
        else:
            OutStack.append([f"{front}_{top[0]}",top[1]])
            InStack=InStack[:-1]
            # for i in OutStack:
            #     print(OutStack)
    return OutStack

def flat2row(flat):
    # 将flat格式存储的每一个value行拼起来，输出数据行
    ret=""
    for i in flat:
        ret+=str(i[1])
        ret+=","
    return ret

def flat2title(flat):
    # 将flat格式存储的每一个key行拼起来，输出标题行
    ret=""
    for i in flat:
        ret+=str(i[0])
        ret+=","
    return ret

def FlatDict(dic):
    # 将多层嵌套字典“拍扁”
    ret={}
    tmp=extract("",dic)
    for k_v in tmp:
        ret[k_v[0]]=k_v[1]
    return ret

def Flat2CSV(DicList):
    # 将多层嵌套字典输出到CSV文件
    DataDict={}

    for dic in DicList:
        data=extract("",dic)
        KeyLine=flat2title(data)
        ValueLine=flat2row(data)

        if KeyLine not in DataDict.keys():
            DataDict[KeyLine]=[]
            DataDict[KeyLine].append(ValueLine)
        else:
            DataDict[KeyLine].append(ValueLine)

    # js = json.dumps(js, indent=4, separators=(',', ':'))
    # print(KeyLine)
    # print(ValueLine)
    # 调试用，格式化输出js

    i=0
    for key,value in DataDict.items():
        # 每种类型的dict均会有一个文件，自行选择特征，并修改文件名即可
        with open(f"./data/type_{i}.csv","a+",encoding="utf-8") as f:
            
            f.write(f"{key}\n")
            for ValueLine in value:
                f.write(f"{ValueLine}\n")
        i+=1


    
dic={
    "msg_type": "other",
    "_content": {
        "cmd": "LIVE_INTERACTIVE_GAME",
        "data": {
            "type": 1,
            "uid": 385956415,
            "uname": "工号1001", 
            "uface": "http://i1.hdslb.com/bfs/face/e2ddc2275df94af1cebf7028aa1bdc1bb30e78f4.jpg", 
            "gift_id": 31036, 
            "gift_name": "小花花", 
            "gift_num": 1, 
            "price": 100, 
            "paid": "True", 
            "msg": "", 
            "fans_medal_level": 0, 
            "guard_level": 0, 
            "timestamp": 1640693582, 
            "anchor_lottery": "None", 
            "pk_info": "None", 
            "anchor_info": {
                "uid": 23920239, 
                "uname": "小米公司", 
                "uface": "http://i0.hdslb.com/bfs/face/398e4b6654bbb64d87f645b9b45591e4f959f6ce.jpg"
            }
        }
    }
 }

diclist=[
    {
    "msg_type": "other",
    "_content": {
        "cmd": "LIVE_INTERACTIVE_GAME",
        "data": {
            "type": 1,
            "uid": 385956415,
            "uname": "工号1001", 
            "uface": "http://i1.hdslb.com/bfs/face/e2ddc2275df94af1cebf7028aa1bdc1bb30e78f4.jpg", 
            "gift_id": 31036, 
            "gift_name": "小花花", 
            "gift_num": 1, 
            "price": 100, 
            "paid": "True", 
            "msg": "", 
            "fans_medal_level": 0, 
            "guard_level": 0, 
            "timestamp": 1640693582, 
            "anchor_lottery": "None", 
            "pk_info": "None", 
            "anchor_info": {
                "uid": 23920239, 
                "uname": "小米公司", 
                "uface": "http://i0.hdslb.com/bfs/face/398e4b6654bbb64d87f645b9b45591e4f959f6ce.jpg"
            }
        }
    }
 },
 {
    "msg_type": "other",
    "_content": {
        "cmd": "LIVE_INTERACTIVE_GAME",
        "data": {
            "type": 1,
            "uid": 385956415,
            "uname": "工号1001", 
            "uface": "http://i1.hdslb.com/bfs/face/e2ddc2275df94af1cebf7028aa1bdc1bb30e78f4.jpg", 
            "gift_id": 31036, 
            "gift_name": "小花花", 
            "gift_num": 1, 
            "price": 100, 
            "paid": "True", 
            "msg": "", 
            "fans_medal_level": 0, 
            "guard_level": 0, 
            "timestamp": 1640693582, 
            "anchor_lottery": "None", 
            "pk_info": "None", 
            "anchor_info": {
                "uid": 23920239, 
                "uname": "小米公司", 
                "uface": "http://i0.hdslb.com/bfs/face/398e4b6654bbb64d87f645b9b45591e4f959f6ce.jpg"
            }
        }
    }
 }
]

print(FlatDict(dic))
Flat2CSV(diclist)
