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

typedict={} # 存放所有的通知类型
with open("./data/rawoutput.json", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        # if ": b'" in line:
        #     continue
        tmp = line.replace("\"", " ")
        tmp = tmp.replace("'", "\"")
        tmp = tmp.replace("\\x", "\\\\x")
        tmp = tmp.replace("False", "\"False\"")
        tmp = tmp.replace("True", "\"True\"")
        tmp = tmp.replace("None", "\"None\"")

        try:
            js = json.loads(tmp)
            message=js["msg_type"]
            if message not in typedict.keys():
                typedict[message]=[]
                typedict[message].append(js)
                # 若不存在该类型，初始化并插入
            else:
                typedict[message].append(js)
                # 若存在，直接插入
            
            # js = json.dumps(js, indent=4, separators=(',', ':'))
            # 调试用，格式化输出js

        except Exception as e:
            # 保存错误输出
            with open("./data/FailureData.txt","a+" ,encoding="utf-8")as f:
                f.write(f"{e}\n")
                f.write(f"{line}\n")
                f.write("=============\n")
            pass

for key,value in typedict.items():
    print(key)
    with open(f"./data/{key}.csv","a+",encoding="utf-8") as f:

        # 拿第0行出来把标题写进文件
        ExampleLine=value[0]
        
        # if ExampleLine["msg_type"]!="danmaku" or ExampleLine["msg_type"]!="broadcast":
        #     # 对于非弹幕信息，只保留通知内容就行
        #     ExampleLine=ExampleLine["content"]
        # else:
        #     # 对于弹幕信息，只去除msg_type
        #     ExampleLine.pop("msg_type")
        # # 可以去掉_msg_type，否则标题太长

        FlatKey=extract("",ExampleLine)
        KeyLine=flat2title(FlatKey)
        f.write(f"{KeyLine}\n")

        # 用其他普通行提取数据
        for RawLine in value:

            # if RawLine["msg_type"]!="danmaku" or RawLine["msg_type"]!="broadcast":
            #     # 对于非弹幕信息，只保留通知内容就行
            #     RawLine=RawLine["content"]
            # else:
            #     # 对于弹幕信息，只去除msg_type
            #     RawLine.pop("msg_type")
            # # 相应去掉_msg_type的数据

            FlatValue=extract("",RawLine)
            DataLine=flat2row(FlatValue)
            f.write(f"{DataLine}\n")
