# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2024/2/4 11:04
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: 机器学习 => users.py
"""
from db.base import User
from models.users import UserIn, UserInUpdate


# 创建用户
async def create_user(user_in: UserIn) -> User:
    user = User(**user_in.dict())
    await user.save()
    return user


# 获取所有用户
async def get_all_user() -> list[User]:
    return await User.all()


# 更新用户信息
async def update_user(user_id: int, user_update: UserInUpdate) -> User:
    user = await User.get(id=user_id)
    for k, v in user_update.dict().items():
        if v:
            setattr(user, k, v)
    await user.save()
    return user


# 删除用户
async def delete_user(user_id: int):
    post = await User.get(id=user_id)
    await post.delete()
