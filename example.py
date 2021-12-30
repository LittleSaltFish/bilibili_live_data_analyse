import asyncio
import danmaku
import sys
import time
import json


async def printer(q,link):
    while True:
        m = await q.get()

        Now=time.time()
        m["Date"]=time.strftime('%Y.%m.%d',time.localtime(time.time()))
        m["ExactTime"]=time.strftime('%H:%M:%S',time.localtime(time.time()))
        m["DeltaTime"]=round(Now-StartTime,2)

        RoomId=link.split("/")[-1]
        with open(f"./{RoomId}.json","a+",encoding="utf-8") as f:
            data=m
            # data=json.dumps(m)
            f.write(str(data)+"\n")
        print(data)

async def main():
    q = asyncio.Queue()
    dmc = danmaku.DanmakuClient(sys.argv[1], q)
    asyncio.create_task(printer(q,sys.argv[1]))
    await dmc.start()

StartTime=time.time()
asyncio.run(main())
