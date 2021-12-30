import json
import re

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

def WashLine(line):
    # 清洗数据以满足格式要求
    tmp = line.replace("\"", " ")
    tmp = tmp.replace("'", "\"")
    tmp = tmp.replace("\\x", "\\\\x")
    tmp = tmp.replace("False", "\"False\"")
    tmp = tmp.replace("True", "\"True\"")
    tmp = tmp.replace("None", "\"None\"")
    return tmp


DataDict={} # 存放所有的通知，格式为 标题行：[内容行1,内容行2,...,内容行n]

with open("./data/rawoutput.json", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        tmp=WashLine(line)
        # 初步清洗以满足json格式需要

        try:
            js = json.loads(tmp)
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
            with open("./data/FailureData.txt","a+" ,encoding="utf-8")as f:
                f.write(f"{e}\n")
                f.write(f"{line}\n")
                f.write("=============\n")
            pass

i=0
for key,value in DataDict.items():
    with open(f"./data/type{i}.csv","a+",encoding="utf-8") as f:
        
        f.write(f"{key}\n")
        for ValueLine in value:
            f.write(f"{ValueLine}\n")
    i+=1
