#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Created__ = '2018/4/10'

import csv
import numpy as np
import matplotlib.pyplot as plt
from config import ORIGINAL_DATA_FILEPATH, MAX_DAY

class ReadStockTool(object):
    def __init__(self, stock_code):
        self.stock_code = stock_code


    def read_one_stock(self):
        stockdata_list = []
        if isinstance(self.stock_code, int):
            self.stock_code = str(self.stock_code)
        for i in range(1, MAX_DAY + 1):
            file_path = ORIGINAL_DATA_FILEPATH + "/" + str(i) + ".csv"
            with open(file_path) as f:
                reader = csv.reader(f)
                for row in reader:
                    if row[0] == "stock" + self.stock_code:
                        stockdata_list.append(row[1])
                        break
        return stockdata_list

    def draw_chart(self):
        """
        画图
        :return:
        """
        stockdata_list = self.read_one_stock()
        print(stockdata_list)
        y = stockdata_list
        x = range(1, MAX_DAY + 1)
        plt.ylabel("价格")
        plt.plot(x, y)
        plt.show()




if __name__ == "__main__":
    rst = ReadStockTool(102419)
    rst.draw_chart()
