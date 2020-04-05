# 项目简介
![Python3.7](https://img.shields.io/badge/python-3.7-green.svg?style=flat-square&logo=python&colorB=blue)

为了能够更好的对尚未上映的电影进行客观评分，供观众进行参考和向观众推荐高质量电影，本项目以豆瓣电影网爬取的2万余部电影作为研究对象，通过计算特征向量的相似度构建电影评分预测模型，进而预测电影评分，为观众客观评分提供参考数据。

## 快速上手
1. 克隆此仓库
```commandline
git clone https://github.com/yyywang/yinrui
cd yinrui
```
2. 安装依赖包
+ 若未安装 `pipenv` 先执行以下命令安装
```commandline
pip install pipenv
```
+ 通过 `pipenv` 自动安装依赖包
```commandline
pipenv shell
```
3. 运行
```commandline
python starter.py
```