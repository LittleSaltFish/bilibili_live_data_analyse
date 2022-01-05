import asyncio
import danmaku
import sys
import time
import json


async def printer(q, link):
    while True:
        m = await q.get()

        Now = time.time()
        m["Date"] = time.strftime('%Y.%m.%d', time.localtime(time.time()))
        m["ExactTime"] = time.strftime('%H:%M:%S', time.localtime(time.time()))
        m["DeltaTime"] = round(Now-StartTime, 2)

        RoomId = link.split("/")[-1]
        with open(f"./data/Rooms/{RoomId}.json", "a+", encoding="utf-8-sig") as f:

            for key, value in m.items():
                if type(value).__name__ == "bytes":
                    m[key] = str(m[key])
                if type(value).__name__ == "str":
                    m[key] = m[key].replace(",", "，")
            # 将byte型数据转化为可以json.dump的格式，并处理英文逗号，以免在CSV中混淆

            data = json.dumps(m, ensure_ascii=False)
            f.write(str(data)+"\n")
        print(data)


async def main():
    q = asyncio.Queue()
    dmc = danmaku.DanmakuClient(sys.argv[1], q)
    asyncio.create_task(printer(q, sys.argv[1]))
    await dmc.start()

StartTime = time.time()
asyncio.run(main())
