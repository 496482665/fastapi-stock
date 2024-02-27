# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2024/2/22 17:07
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: stock => schedules.py
"""
from core.schedules.main import scheduler


async def init_schedule() -> any:
    # 开启周期任务
    scheduler.start()


async def close_schedule() -> any:
    # 关闭周期任务
    scheduler.shutdown()
