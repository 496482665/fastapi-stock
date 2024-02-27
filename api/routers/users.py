# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2024/2/4 10:23
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: 机器学习 => users.py
"""
from fastapi import APIRouter
from models.users import UserIn, UserInUpdate
from services import users

router = APIRouter()


@router.get("", summary="获取所有用户")
async def get_users():
    all_users = await users.get_all_user()
    return all_users


@router.post("", summary="创建用户")
async def create_user(user: UserIn):
    return await users.create_user(user)


@router.put("/{user_id}", summary="更新用户")
async def update_user(user_id: int, user: UserInUpdate):
    return await users.update_user(user_id, user)


@router.delete("/{user_id}", summary="删除用户")
async def update_user(user_id: int):
    await users.delete_user(user_id)
    return {"msg": "删除成功"}
