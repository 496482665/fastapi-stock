# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2024/2/22 11:33
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: stock => basic_data.py
"""
from tortoise import run_async

from db.stock import BaseMarketDailyData, StockMarketActivity
from utils.basic_data import basic_stock_market_data, get_stock_market_activity_legu


# 保存每日股市数据
async def save_base_market_daily_data():
    """
    {
      "数量": {
        "主板": 3121,
        "科创板": 569,
        "创业板": 818,
        "统计": 4508
      },
      "总市值": {
        "主板": 598957.5,
        "科创板": 50957.9,
        "创业板": 78453.45,
        "统计": 728368.85
      },
      "流通市值": {
        "主板": 542417.62,
        "科创板": 33383.82,
        "创业板": 53848.54,
        "统计": 629649.98
      }
    }
    """
    data = basic_stock_market_data()

    await BaseMarketDailyData.create(
        total_value=data["总市值"]["统计"],
        total_company_count=data["数量"]["统计"],
        total_circulation_value=data["流通市值"]["统计"],
        raw_value=data
    )


# 保存每日赚钱效应
async def save_stock_market_activity():
    data = get_stock_market_activity_legu(fetch=True)

    format_dict = dict()
    for item in data:
        format_dict[item["item"]] = item["value"]

    await StockMarketActivity.create(**format_dict)
