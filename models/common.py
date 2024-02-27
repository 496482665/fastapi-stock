# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2024/2/2 09:52
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: 机器学习 => common.py
"""
import datetime

from pydantic import BaseModel, Field


class DateTimeModelMixin(BaseModel):
    created_at: datetime.datetime = None  # type: ignore
    updated_at: datetime.datetime = None  # type: ignore


class CommonModel(DateTimeModelMixin, BaseModel):
    user_id: int = Field(...)
