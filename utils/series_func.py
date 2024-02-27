# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2023/11/11 17:01
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: 机器学习 => series_func.py
"""
from functools import reduce

import pandas as pd


def get_merge_series(*series):
    # 找到共同的，需要合并的index
    # common_index = list(set(series1.index) & set(series2.index))
    series_list = [i.index for i in series]
    common_index = reduce(pd.Index.intersection, series_list)

    merge_series = pd.Series()
    # 合并Series并进行数字相加
    for s in series:
        merge_series = merge_series.add(s.loc[common_index].astype("float"), fill_value=0)

    # # 打印合并后的Series
    # print(merge_series)

    return merge_series
