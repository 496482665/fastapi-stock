# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2024/2/4 10:22
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: 机器学习 => base.py
"""
from fastapi import APIRouter
from .routers import users, stock, concept

router = APIRouter()

router.include_router(users.router, tags=["用户"], prefix="/users")
router.include_router(stock.router, tags=["股票分析"], prefix="/stock")
router.include_router(concept.router, tags=["概念板块"], prefix="/concept")
