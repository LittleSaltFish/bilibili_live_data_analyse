import json
import re
import os


Datas=[]
roomid=[
257958427,1958342,238329119,3766866,777536,1646746,1262638877,10330740,730732,14110780,416523954,374377,434334701,672353429,58485079,3900277,2131609593,83178096,392836434,29022551,1388514638,16573314,7774837,484322035,672328094,]

with open("./data/Info.json", "r", encoding="utf-8-sig") as f:
    lines = f.readlines()
    for line in lines:
        try:
            DataDict={}
            js = json.loads(line)
            DataDict["time"]=js["time"]
            for i in roomid:
                DataDict[f"{i}_online"]=js["data"]["data"][str(i)]["online"]
                DataDict[f"{i}_status"]=js["data"]["data"][str(i)]["live_status"]
                DataDict[f"{i}_livetime"]=js["data"]["data"][str(i)]["live_time"]
                DataDict[f"{i}_broadcast_type"]=js["data"]["data"][str(i)]["broadcast_type"]
            Datas.append(DataDict)
        except Exception as e: 
            print(line)
            print(e)


with open("./data/Info.csv", "a+", encoding="utf-8-sig") as f:
    for key in Datas[0].keys():
        f.write(f"{key},")
    f.write("\n")
    for i in Datas:
        for value in i.values():
            f.write(f"{value},")
        f.write("\n")
