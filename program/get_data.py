# -*- coding: utf-8 -*-
"""
  Created by Wesley on 2020/4/3.
"""
import pandas as pd
from config.config import Config
from program.utils import progress_bar


class DataObject:
    """操作数据的类"""
    def __init__(self):
        print('加载数据...')
        self.data_frame = pd.read_excel(Config.data_file_path) # 数据集
        print('数据加载完成')

    @property
    def rows(self):
        """以行为单位的数据"""
        return self.data_frame.values

    @property
    def row_num(self):
        """数据的行数"""
        return self.data_frame.shape[0]

    @property
    def column_num(self):
        """数据的列数"""
        return self.data_frame.shap[1]

    def get_row(self, idx):
        """返回第 idx 行数据"""
        return self.rows[idx]

    def get_year_of_row(self, idx):
        """返回第 idx 行的年份"""
        row = self.rows[idx]
        return str(row[16])[:4] # 第16个单元格数据为年份字符串

    def get_category_of_row(self, idx):
        """返回第 idx 行的类型, 一部电影有多个类型，以 “/” 分割。
        例：剧情/悬疑/惊悚"""
        row = self.get_row(idx)
        return row[10].split('/')

    def get_country_of_row(self, idx):
        """返回第 idx 行的国家"""
        row = self.get_row(idx)
        countries = row[14].split('/')
        return [country.strip() for country in countries]

    def get_score_of_row(self, idx):
        """返回第 idx 行的得分"""
        row = self.get_row(idx)
        return row[1]

    @property
    def years(self):
        """升序返回所有上映年份"""
        years_list = self.data_frame.get('上映日期').values
        returned = set()
        for idx, item in enumerate(years_list):
            progress_bar(idx, len(years_list), prefix='计算获取所有<年份>')
            returned.add(str(item)[:4])
        # 将年份升序排列
        return sorted(returned)

    @property
    def categories(self):
        """返回所有电影类型"""
        categories_list = self.data_frame.get('类型').values
        returned = set()
        for item in categories_list:
            categories = str(item).split('/') # 一部电影有多个类型，以 “/” 分割。例：剧情/悬疑/惊悚
            returned.update(categories) # set 中添加多项数据
        return list(returned)

    @property
    def countries(self):
        """返回所有国家"""
        country_list = self.data_frame.get('制片国家/地区').values
        returned = set()
        for idx, item in enumerate(country_list):
            progress_bar(idx, len(country_list), prefix='计算获取所有<制片国家/地区>')
            countries = str(item).split('/') # 一部电影有多个制片国家，以 “/” 分割。例：美国 / 英国
            countries = [country.strip() for country in countries ] # 去除字符串两端空格
            returned.update(countries) # set 中添加多项数据
        return list(returned)
