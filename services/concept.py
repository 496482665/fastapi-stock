# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2024/2/28 16:29
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: stock => concept.py
"""
import akshare as ak


# 获取同花顺概念板块列表
def get_concept_list_logic():
    # todo:设置缓存
    stock_board_concept_name_ths_df = ak.stock_board_concept_name_ths()
    return stock_board_concept_name_ths_df.to_dict("records")


# 获取同花顺概念板块成分股
def get_concept_detail_logic(concept_name: str):
    # todo:设置缓存
    stock_board_concept_cons_ths_df = ak.stock_board_concept_cons_ths(symbol=concept_name)
    return stock_board_concept_cons_ths_df.to_dict("records")


# 获取同花顺概念板块图谱
def get_concept_graph_logic(concept_name: str):
    # todo:设置缓存
    stock_board_concept_graph_ths_df = ak.stock_board_concept_graph_ths(symbol=concept_name)
    return stock_board_concept_graph_ths_df.to_dict("records")
