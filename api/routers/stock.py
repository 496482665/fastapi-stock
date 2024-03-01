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

from initlize.db import init_stock_basic_data
from utils import basic_data, daily_data
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


@router.get("/init_stock_basic_data", summary="初始化存储股市基本数据")
async def test():
    await init_stock_basic_data()


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
