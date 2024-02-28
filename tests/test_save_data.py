# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2024/2/23 14:10
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: stock => test_save_data.py
"""
# 如果需要单独执行
from tortoise import run_async

from core.schedules.basic_data import save_base_market_daily_data,save_stock_market_activity
from initlize.db import init_db, close_db

run_async(init_db())
run_async(save_base_market_daily_data())
run_async(save_stock_market_activity())
run_async(close_db())
