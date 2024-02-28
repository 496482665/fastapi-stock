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
import akshare as ak


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


# 获取赚钱效应
def get_stock_market_activity_legu(fetch: bool = False):
    stock_market_activity_legu_df = ak.stock_market_activity_legu()

    # 需要修改列名时使用
    def fetch_columns(x):
        x_map = {
            "上涨": "rise",
            "涨停": "rise_limit",
            "真实涨停": "rise_limit_real",
            "st st*涨停": "rise_limit_st",
            "下跌": "fall",
            "跌停": "fall_limit",
            "真实跌停": "fall_limit_real",
            "st st*跌停": "fall_limit_st",
            "平盘": "zero",
            "停牌": "stop",
            "活跃度": "activity",
            "统计日期": "date"
        }

        return x_map[x]

    if fetch:
        stock_market_activity_legu_df["item"] = stock_market_activity_legu_df["item"].apply(fetch_columns)

    return stock_market_activity_legu_df.to_dict("records")


# 获取公司动态
def get_company_dynamic(date: str):
    """

    :param date: 20240228
    :return:
    """
    stock_gsrl_gsdt_em_df = ak.stock_gsrl_gsdt_em(date=date)
    print(stock_gsrl_gsdt_em_df)
    return stock_gsrl_gsdt_em_df.to_dict("records")