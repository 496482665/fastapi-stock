# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2024/2/29 17:00
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: stock => industry.py
"""
from fastapi import APIRouter

from services.industry import get_industry_list_logic, get_industry_detail_logic

router = APIRouter()


@router.get("/list", summary="获取同花顺行业板块列表")
async def get_industry_list():
    return get_industry_list_logic()


@router.get("/industry_detail/{industry_name}", summary="获取同花顺行业板块成份股")
async def get_concept_detail(industry_name: str):
    return get_industry_detail_logic(industry_name)
