# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2024/2/23 15:03
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: stock => dataframe_func.py
"""
import numpy as np


# 限制浮点数类型的长度
def round_float_length(df):

    # 获取浮点数类型的列
    float_columns = df.select_dtypes(include='float').columns

    # 将浮点数数据处理为字符串，并限制长度为6
    df[float_columns] = df[float_columns].applymap(lambda x: '{:.2f}'.format(x) if np.isfinite(x) else str(x))

    return df
