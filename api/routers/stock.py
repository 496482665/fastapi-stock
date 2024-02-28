# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2024/2/7 17:44
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: stock => stock.py
"""
from fastapi import APIRouter, Query

from db.stock import StockAccountAnalyse
from utils import basic_data, daily_data
from utils.basic_data import get_stock_account_statistics
from services.stock import get_stock_rank_logic

router = APIRouter()


@router.get("/basic_data", summary="获取股票市场基本数据")
async def get_basic_data():
    """获取股票市场基本数据"""
    return basic_data.basic_stock_market_data()


@router.get("/stock_account_statistics", summary="获取股票市场投资者数量数据")
async def get_account_statistics():
    """获取股票市场投资者数量数据"""
    return basic_data.get_stock_account_statistics()


@router.get("/stock_market_activity", summary="获取股票市场赚钱效应")
async def get_stock_market_activity():
    """获取股票市场赚钱效应"""
    return daily_data.get_stock_market_activity_legu()


@router.get("/stock_daily_data/{stock_code}", summary="获取某支股票的每日基本数据")
async def get_basic_data(stock_code: str):
    """获取某支股票的每日基本数据"""
    return daily_data.get_stock_daily_data(stock_code)


@router.get("/stock_account_storage", summary="存储股票市场投资者数量数据")
async def test():
    # 第一次启动时，初始化基础数据
    account_statistics = get_stock_account_statistics(fetch=True)

    model_list = []
    for account_data in account_statistics:
        model_list.append(StockAccountAnalyse(**account_data))

    await StockAccountAnalyse.all().delete()
    await StockAccountAnalyse.bulk_create(model_list)


@router.get("/company_dynamic/{date}", summary="获取某日的股市公司动态")
async def get_company_dynamic(date: str):
    """获取某支股票的每日基本数据"""
    return daily_data.get_company_dynamic(date)


@router.get("/stock_rank", summary="获取量价齐升股价指数")
async def get_stock_rank(stock_code: str = Query(
    None,
    title="股票代码",
    description="股票代码",
    deprecated=True,
)):
    """"""
    return get_stock_rank_logic(stock_code=stock_code)
