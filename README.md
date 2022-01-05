# 基于danmaku的B站直播数据分析

[![python](https://img.shields.io/badge/python-%3E=3.7.x-green.svg)](https://www.python.org/)
[![CSDN](https://img.shields.io/badge/CSDN-%E5%92%B8%E9%B1%BC%E5%92%B8-66ccff)](https://blog.csdn.net/qq_43724306)

<!-- ![GitHub All Releases](https://img.shields.io/github/downloads/LittleSaltFish/bilibili_live_data_analyse/total) -->

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
2. 直接运行，请执行：`bash AutoStart.sh` 可以获取直播间各类弹幕礼物等信息，如果想后台自动持续运行，执行：`nohup bash AutoStart.sh &`
3. 为了进一步分析未提供的信息，添加了以下代码

   执行： `nohup bash AutoMessage.sh` 可以获取直播间热度

   执行： `bash AutoPn.sh` 可以获取直播间清晰度

### 停止获取

因为脚本同时拉起了若干抓取进程，所以不能单纯使用  `ctrl+c` 简单停止

1. 运行：`bash ./AutoStop.sh` 可以停止所有执行脚本

### 数据清洗

1. 运行：`python3 ./data/WashMessage.py` 可以清洗直播间数据
2. 运行：`python3 ./data/WashInfo.py` 可以清洗热度数据
3. 运行：`python3 ./data/WashPn.py` 可以清洗清晰度数据

### 数据存档

因为数据获取时添加了时间等属性，因此为了保证最终数据的一致性，每次自动获取数据前，请执行自动存档程序，清除或转移旧数据文件

1. 运行：`bash ./AutoSave.sh`
