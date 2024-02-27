# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2024/2/7 14:28
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: stock => db.py
"""
from tortoise import Tortoise

from conf.settings import TORTOISE_ORM
from utils.basic_data import get_stock_account_statistics
from db.stock import StockAccountAnalyse


async def init_db() -> any:
    # 创建数据库连接
    await Tortoise.init(
        config=TORTOISE_ORM
    )
    # 初始化生成数据库表
    await Tortoise.generate_schemas()


async def close_db() -> any:
    await Tortoise.close_connections()


