# -*- coding: utf-8 -*-
"""
  Created by Wesley on 2020/4/3.
"""

class Config:
    # 数据文件路径(默认为相对于 program 包下文件的路径)
    # 仅支持 *.xlsx 文件
    data_file_path = '../data/test/data2000.xlsx'

    @classmethod
    def set_data_file(cls, file_path):
        cls.data_file_path = file_path