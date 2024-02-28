# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2024/2/28 16:25
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: stock => concept.py
"""
from fastapi import APIRouter

from services.concept import get_concept_list_logic, get_concept_detail_logic, get_concept_graph_logic

router = APIRouter()


@router.get("/list", summary="获取同花顺概念板块列表")
async def get_concept_list():
    return get_concept_list_logic()


@router.get("/concept_detail/{concept_name}", summary="获取同花顺概念板块成份股")
async def get_concept_detail(concept_name: str):
    return get_concept_detail_logic(concept_name)


@router.get("/concept_graph/{concept_name}", summary="获取同花顺概念板块图谱")
async def get_concept_detail(concept_name: str):
    return get_concept_graph_logic(concept_name)
