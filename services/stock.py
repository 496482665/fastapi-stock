# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2024/2/7 17:42
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: stock => stock.py
"""
from utils import basic_data, daily_data
from utils.dataframe_func import round_float_length


# 获取量价齐升股价指数
def get_stock_rank_logic(stock_code: str = None):
    data = basic_data.get_stock_rank()

    if stock_code:
        tmp_data = data[data["股票代码"] == stock_code]
        if tmp_data.empty:
            return f"股票代码:{stock_code} 今日不存在量价齐升情况"
        else:
            return tmp_data.to_dict("records")

    data = round_float_length(data)

    return data.to_dict("records")
