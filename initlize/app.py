# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2024/2/23 16:53
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: stock => app.py
"""
import argparse


def init_app():
    # 创建解析器对象
    parser = argparse.ArgumentParser(description='命令行参数示例')

    # 添加命令行参数
    parser.add_argument('--init', help='是否需要初始化数据', default=False)

    # 解析命令行参数
    args = parser.parse_args()

    # 访问命令行参数
    init = args.init
