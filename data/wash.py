import json
import re
import os

def extract(front,dic):
    # 递归“解压”Json文件，因为递归进行，所以只能返回数组形式，需要二次处理
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

# def WashLine(line):
#     # 清洗数据以满足格式要求
#     # 因为改变了保存策略，不需要额外再清洗数据了。
#     # 异常捕获暂时保留，以备其他情况
#     tmp = tmp.replace("False", "\"False\"")
#     tmp = tmp.replace("True", "\"True\"")
#     tmp = tmp.replace("None", "\"None\"")
#     return tmp

for curDir, dirs, files in os.walk("./data/Rooms/"):
    for FileName in files:
        RoomId=FileName[:-5]
        print(FileName)

        if not os.path.exists(f"./data/OutPut/{RoomId}/") :
            os.makedirs(f"./data/OutPut/{RoomId}/")

        DataDict={} # 存放所有的通知，格式为 标题行：[内容行1,内容行2,...,内容行n]

        with open(f"./data/Rooms/{FileName}", "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                # line=WashLine(line)
                # 初步清洗以满足json格式需要

                try:
                    js = json.loads(line)
                    data=extract("",js)
                    KeyLine=flat2title(data)
                    ValueLine=flat2row(data)

                    if str(KeyLine) not in DataDict.keys():
                        DataDict[str(KeyLine)]=[]
                        DataDict[str(KeyLine)].append(ValueLine)
                    else:
                        DataDict[str(KeyLine)].append(ValueLine)

                    # js = json.dumps(js, indent=4, separators=(',', ':'))
                    # print(KeyLine)
                    # print(ValueLine)
                    # 调试用，格式化输出js

                except Exception as e:
                    # 保存错误输出，观察清洗效果，以便调整清洗策略
                    with open(f"./data/OutPut/{RoomId}/FailureData_{RoomId}.txt","a+" ,encoding="utf-8")as f:
                        f.write(f"{e}\n")
                        f.write(f"{line}\n")
                        f.write("=============\n")
                    pass

        i=0
        for key,value in DataDict.items():
            with open(f"./data/OutPut/{RoomId}/type{i}.csv", "a+", encoding="utf-8") as f:
                
                f.write(f"{key}\n")
                for ValueLine in value:
                    f.write(f"{ValueLine}\n")
            i+=1
