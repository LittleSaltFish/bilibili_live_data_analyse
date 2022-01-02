# 基于danmaku的B站直播数据分析

![python](https://img.shields.io/badge/python-%3E=3.7-green.svg)

## 项目简介

本仓库主要实现b站弹幕数据的自动化数据采集、清洗和分析

直播间信息爬取代码修改自 [danmaku](https://github.com/THMonster/danmaku)

## 依赖安装

```
pip install aiohttp
sudo apt-get install zip
```

## 使用方法

_以下所有命令脚本，均在文件夹 `/bilibili_live_data_analyse/` 下执行_

### 数据获取

1. 将想要获取的直播间房间号填进 `./RoomIdList.csv` 文件下
2. 直接运行，请执行：`bash AutoStart.sh`

   如果想后台自动运行，执行：`nohup bash AutoStart.sh &`

   如果不想保留 `nohup.out` 的输出，执行：`nohup bash AutoStart.sh >/dev/null 2>&1 &`

### 停止获取

由于AutoFetch脚本同时拉起了若干进程，因此不能单纯使用  `ctrl+c` 简单停止进程

1. 运行：`bash ./AutoStop.sh`

### 数据清洗

1. 运行：`python3 ./data/wash.py`

### 数据存档

因为数据获取时添加了时间等属性，因此为了保证最终数据的一致性，每次自动获取数据前，请执行自动存档程序，清除或转移旧数据文件

1. 运行：`bash ./AutoSave.sh`
