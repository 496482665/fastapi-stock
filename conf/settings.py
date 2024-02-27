# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2024/2/7 16:09
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: stock => settings.py
"""
TORTOISE_ORM = {
    "connections": {"default": "mysql://root:1qaz@WSX@127.0.0.1:3306/fastapi-stock?charset=utf8mb4"},  # MySQL
    # "connections": {"default": "sqlite://db.sqlite3"},  # sqlite
    "apps": {
        # 模型分组名字，当需要使用此app下的模型的时候，需使用 此名字.模型名称
        "default": {
            # 须添加"aerich.models", 此时，会在数据库中生成一个名为aerich的表用于存模型信息，以便以后做脚本迁移
            "models": ["aerich.models", "db.base", "db.stock"],  # 模型所在的py文件
            "default_connection": "default"
        }
    }
}