# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2024/2/6 10:46
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: 机器学习 => base.py
"""
from enum import Enum

from tortoise.models import Model
from tortoise import fields

from utils.constant import LEN_LONG


class SexEnum(str, Enum):
    MALE = '男'
    FEMALE = '女'
    UNKNOWN = '未知'


class BaseModel(Model):
    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)


class User(BaseModel):
    name = fields.CharField(max_length=LEN_LONG)
    email = fields.CharField(max_length=LEN_LONG)
    phone = fields.IntField()
    age = fields.IntField()
    sex = fields.CharEnumField(SexEnum, max_length=LEN_LONG)
    cn_name = fields.CharField(max_length=LEN_LONG, description="中文名")

