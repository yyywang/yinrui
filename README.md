# 项目简介
![Python3.7](https://img.shields.io/badge/python-3.7-green.svg?style=flat-square&logo=python&colorB=blue)

以豆瓣电影网爬取的2万余部电影作为研究对象，通过计算特征向量的相似度构建电影评分预测模型，进而预测电影评分，为观众客观评分提供参考数据。

## 快速上手
1. 克隆此仓库
```commandline
git clone https://github.com/yyywang/yinrui.git
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

## 生产环境
1. 将数据 `xxx.xlsx` 放入 `/data/production/` 文件夹中 
2. 在 `starter.py` 中修改数据文件路径
```python
file_path = './data/production/xxx.xlsx'      # 数据文件路径，仅支持 xlsx 格式
```
3. 运行
```commandline
python starter.py
```