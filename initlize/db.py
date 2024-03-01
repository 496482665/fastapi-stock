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
from utils.basic_data import get_stock_account_statistics, get_all_company_code
from db.stock import StockAccountAnalyse, CompanyCode


async def init_db() -> any:
    # 创建数据库连接
    await Tortoise.init(
        config=TORTOISE_ORM
    )
    # 初始化生成数据库表
    await Tortoise.generate_schemas()


async def close_db() -> any:
    await Tortoise.close_connections()


# 初始化公司代码
async def init_company_code():
    company_codes = get_all_company_code()

    model_list = []
    for company_code in company_codes:
        model_list.append(CompanyCode(**company_code))

    await CompanyCode.all().delete()
    await CompanyCode.bulk_create(model_list)


# 初始化投资者账号情况
async def init_stock_account_storage():
    account_statistics = get_stock_account_statistics(fetch=True)

    model_list = []
    for account_data in account_statistics:
        model_list.append(StockAccountAnalyse(**account_data))

    await StockAccountAnalyse.all().delete()
    await StockAccountAnalyse.bulk_create(model_list)


# 初始化股市基本数据
async def init_stock_basic_data():
    await init_stock_account_storage()
    await init_company_code()
