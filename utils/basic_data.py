# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2023/11/9 15:53
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: 机器学习 => basic_data.py
"""
import akshare as ak
import pandas as pd

from utils.dataframe_func import round_float_length
from utils.series_func import get_merge_series


# 上证所股票数据总览
def get_sse_summary():
    stock_sse_summary_df = ak.stock_sse_summary()
    return stock_sse_summary_df


# 深证所股票数据总览
def get_szse_summary():
    stock_szse_summary_df = ak.stock_szse_summary()

    def format_float(x):
        x = x / 100000000  # 把数字转换成亿为基础的单位
        return float('{:.2f}'.format(x))

    stock_szse_summary_df["成交金额"] = stock_szse_summary_df["成交金额"].apply(format_float)
    stock_szse_summary_df["总市值"] = stock_szse_summary_df["总市值"].apply(format_float)
    stock_szse_summary_df["流通市值"] = stock_szse_summary_df["流通市值"].apply(format_float)

    return stock_szse_summary_df


# 合并上证和深证的数据
def merge_stock_market_data(szse_data, sse_data):
    """
    合并交易所数据

    :param szse_data: 深证所所数据
    :param sse_data: 上证所数据
    :return:
    """
    merge_stock_data = pd.DataFrame(
        columns=["数量", "总市值", "流通市值"],
        index=["主板", "科创板", "创业板"]
    )

    # 证券类别
    sse_data = sse_data.T
    sse_data.columns = sse_data.loc["项目"]
    sse_data = sse_data.rename(columns={'上市公司': '数量'})

    sse_data = sse_data.drop(index="项目")
    szse_data.index = szse_data["证券类别"]

    # 处理成合并后的数据，分为：主板、创业板、科创板
    merge_stock_data.loc["科创板"] = sse_data.loc["科创板"]
    merge_stock_data.loc["创业板"] = szse_data.loc["创业板A股"]
    merge_stock_data.loc["主板"] = get_merge_series(sse_data.loc["主板"], szse_data.loc["主板A股"], szse_data.loc["中小板"])

    # 每列转换成数字
    merge_stock_data['数量'] = pd.to_numeric(merge_stock_data['数量'], errors='coerce', downcast="unsigned")
    merge_stock_data['流通市值'] = pd.to_numeric(merge_stock_data['流通市值'], errors='coerce', downcast="float")
    merge_stock_data['总市值'] = pd.to_numeric(merge_stock_data['总市值'], errors='coerce', downcast="float")

    # 生成统计行
    merge_stock_data.loc["统计"] = merge_stock_data.sum()

    return merge_stock_data


# 获取股票市场总貌数据 - （沪深主板、科创、创业板）
def basic_stock_market_data():
    # 深圳股市数据
    szse_data = get_szse_summary()
    # 上海股市数据
    sse_data = get_sse_summary()

    merged_stock_market_data = merge_stock_market_data(szse_data, sse_data)

    return merged_stock_market_data.to_dict()


# 获取股市投资者增减数量统计概况
def get_stock_account_statistics(fetch: bool = False):
    stock_account_statistics_em_df = ak.stock_account_statistics_em()

    # 需要修改列名时使用
    def fetch_columns(stock_account_statistics_em_df):
        stock_account_statistics_em_df = stock_account_statistics_em_df[[
            "数据日期",
            "新增投资者-数量",
            "期末投资者-总量",
            "期末投资者-A股账户",
            "期末投资者-B股账户",
            "沪深总市值",
            "沪深户均市值",
            "上证指数-收盘",
            "上证指数-涨跌幅",
        ]]

        stock_account_statistics_em_df.columns = [
            "date",
            "add_number",
            "total_number",
            "total_number_a",
            "total_number_b",
            "total_value",
            "total_avg_value",
            "sse_index",
            "sse_increase",
        ]
        return stock_account_statistics_em_df

    if fetch:
        stock_account_statistics_em_df = fetch_columns(stock_account_statistics_em_df)

    stock_account_statistics_em_df = round_float_length(stock_account_statistics_em_df)

    return stock_account_statistics_em_df.to_dict("records")


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
