# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2024/2/21 17:28
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: stock => stock.py
"""
from .base import BaseModel

import datetime
from tortoise import fields


# 市场每日基本数据
class BaseMarketDailyData(BaseModel):
    date = fields.DateField(auto_now_add=True, default=datetime.date.today())
    total_value = fields.FloatField(description="总市值")
    total_company_count = fields.IntField(description="公司总数量")
    total_circulation_value = fields.IntField(description="总流通市值")
    raw_value = fields.JSONField(description="原始数据")

    class Meta:
        table = "base_market_daily_data"


# 投资者数量变化概况
class StockAccountAnalyse(BaseModel):
    date = fields.CharField(default="", description="月份", max_length=255)
    add_number = fields.FloatField(description="新增投资者-数量")
    total_number = fields.FloatField(description="期末投资者-总量")
    total_number_a = fields.FloatField(description="期末投资者-A股账户")
    total_number_b = fields.FloatField(description="期末投资者-B股账户")
    total_value = fields.FloatField(description="沪深总市值")
    total_avg_value = fields.FloatField(description="沪深户均市值")
    sse_index = fields.FloatField(description="上证指数-收盘")
    sse_increase = fields.FloatField(description="上证指数-涨跌幅")

    class Meta:
        table = "stock_account_analyse"


# 赚钱效应分析
class StockMarketActivity(BaseModel):
    date = fields.DateField(default=datetime.date.today(), description="日期")
    rise = fields.FloatField(description="上涨")
    rise_limit = fields.FloatField(description="涨停")
    rise_limit_real = fields.FloatField(description="真实涨停")
    rise_limit_st = fields.FloatField(description="st*涨停")
    fall = fields.FloatField(description="下跌")
    fall_limit = fields.FloatField(description="跌停")
    fall_limit_real = fields.FloatField(description="真实跌停")
    fall_limit_st = fields.FloatField(description="st*跌停")
    zero = fields.FloatField(description="平盘")
    stop = fields.FloatField(description="停牌")
    activity = fields.CharField(description="活跃度", default="0%", max_length=255)

    class Meta:
        table = "stock_market_activity"
