# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2024/2/7 14:57
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: stock => users.py
"""
from typing import Optional

from pydantic import BaseModel

from db.base import SexEnum


class UserIn(BaseModel):
    name: str
    age: Optional[int] = None
    sex: str = SexEnum.UNKNOWN
    phone: Optional[int] = None
    email: Optional[str] = None
    cn_name: Optional[str] = None


class UserInUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    sex: Optional[str] = None
    phone: Optional[int] = None
    email: Optional[str] = None
    cn_name: Optional[str] = None
