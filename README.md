# 基于danmaku的B站直播数据分析

[![python](https://img.shields.io/badge/python-%3E=3.7.x-green.svg)](https://www.python.org/)
[![CSDN](https://img.shields.io/badge/CSDN-%E5%92%B8%E9%B1%BC%E5%92%B8-66ccff)](https://blog.csdn.net/qq_43724306)

<!-- ![GitHub All Releases](https://img.shields.io/github/downloads/LittleSaltFish/bilibili_live_data_analyse/total) -->

## 一、项目简介

本仓库主要实现b站弹幕数据的自动化数据采集、清洗和分析

直播间信息爬取代码修改自 [danmaku](https://github.com/THMonster/danmaku)

## 二、依赖安装

```
pip install aiohttp
sudo apt-get install zip
```

## 三、使用方法

_以下所有命令脚本，均在文件夹 `/bilibili_live_data_analyse/` 下执行_

### 3.1 数据获取

#### 3.11 配置直播间房间号

1. 将想要获取的直播间房间号填进 `./RoomIdList.csv` 文件下

#### 3.12 运行抓取程序

1. 获取直播间各类弹幕礼物等信息：输出路径为 `./data/Rooms/`

   若想观察程序输出，执行：`bash AutoStart.sh` 

   若想后台自动持续运行，执行：`nohup bash AutoStart.sh &`
2. 若想进一步获取其他信息：

   执行： `nohup bash AutoMessage.sh` 可以获取直播间热度，输出文件为 `./data/info.json`

   执行： `bash AutoPn.sh` 可以获取直播间清晰度，输出文件为 `./data/Pn.json`

### 3.2 停止获取

因为脚本同时拉起了若干抓取进程，所以不能单纯使用  `ctrl+c` 简单停止

1. 运行：`bash ./AutoStop.sh` 可以停止所有执行脚本

### 3.3 数据清洗

1. 运行：`python3 ./data/WashMessage.py` 可以清洗直播间数据，输出路径为 `./data/OutPut/`
2. 运行：`python3 ./data/WashInfo.py` 可以清洗热度数据，输出文件为 `./data/Info.csv`
3. 运行：`python3 ./data/WashPn.py` 可以清洗清晰度数据，输出文件为 `./data/PnOut.csv`

### 3.4 数据提取

鉴于消息种类过多，且各个文件夹type对应表头不统一，本仓库提供筛选最常用的存储 `弹幕` 和 `礼物` 数据的程序，若想提取其他数据，略加修改即可。

1. 运行：`python3 ./data/GetUseful.py` ，输出路径为 `./data/Useful/`

### 3.5 数据存档

因为数据获取时添加了时间等属性，因此为了保证最终数据的一致性，每次自动获取数据前，请执行自动存档程序，清除或转移旧数据文件

1. 运行：`bash ./AutoSave.sh` ，输出路径为 `./data/FetchHistory/`
