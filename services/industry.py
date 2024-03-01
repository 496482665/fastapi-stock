# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2024/2/29 16:56
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: stock => industry.py
"""
import akshare as ak


# 同花顺行业板块列表
def get_industry_list_logic():
    # todo:设置缓存
    stock_board_industry_summary_ths_df = ak.stock_board_industry_summary_ths()
    return stock_board_industry_summary_ths_df.to_dict("records")


# 同花顺行业板块成分股
def get_industry_detail_logic(industry_name: str):
    # todo:设置缓存
    stock_board_industry_cons_ths_df = ak.stock_board_industry_cons_ths(symbol=industry_name)
    return stock_board_industry_cons_ths_df.to_dict("records")


# 东方财富板块异动详情
def get_industry_abnormal_movement():
    stock_board_change_em_df = ak.stock_board_change_em()
    return stock_board_change_em_df.to_dict("records")
