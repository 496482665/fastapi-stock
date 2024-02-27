# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2023/11/8 20:44
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: 机器学习 => daily_data.py
"""
# -*- coding: utf-8 -*-
import datetime

import pandas
import tushare as ts


def get_stock_daily_data(stock_code, trade_date: str = None):
    """

    :param stock_code:
    :param start_date:
    :param end_date:
    :return:
    """
    pro = ts.pro_api()
    if not trade_date:
        start_date = datetime.datetime.now().strftime("YYYYMMDD")

    df: pandas.DataFrame = pro.daily(ts_code=stock_code, trade_date=trade_date)

    return df.to_dict("records")
