# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2024/2/22 15:21
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: stock => main.py
"""
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from .basic_data import save_base_market_daily_data, save_stock_market_activity

scheduler = BackgroundScheduler()


def test():
    print("aa")


# 每天16:00执行，更新股票市场基本数据
scheduler.add_job(save_base_market_daily_data, CronTrigger(hour='16', minute='0'))
# 每天16：:00执行，更新每日赚钱效应
scheduler.add_job(save_stock_market_activity, CronTrigger(hour='16', minute='0'))
