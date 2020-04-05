# -*- coding: utf-8 -*-
"""
  Created by Wesley on 2020/4/1.
"""
from config.config import Config
from program.draw_table import draw_bar_year_category, show_all_chart
from program.get_data import DataObject

if __name__ == '__main__':
    file_path = './data/test_process2000.xlsx'      # 数据文件路径，仅支持 xlsx 格式
    Config.set_data_file(file_path)                 # 配置数据文件
    data_obj = DataObject()                         # 操作数据的对象
    draw_bar_year_category(data_obj)                # 各年份各电影类型下的电影数
    show_all_chart()                                # 绘制所有图表