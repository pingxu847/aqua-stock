'''
调用方法

get_all_securities(types=['stock'], date=None)
参数

types：默认为stock，这里请在使用时注意防止未来函数。
date: 日期, 一个字符串或者 [datetime.datetime]/[datetime.date] 对象, 用于获取某日期还在上市的股票信息. 默认值为 None, 表示获取所有日期的股票信息
返回

display_name # 中文名称
name # 缩写简称
start_date # 上市日期
end_date # 退市日期，如果没有退市则为2200-01-01
type # 类型，stock(股票)，index(指数)，etf(ETF基金)，fja（分级A），fjb（分级B）
'''

import jqdatasdk
import clickhouse_connect
import all_securities_schema

class AllSecurities:
    def __init__(self, tenancy):
        db = "stock"
        if tenancy == "testing":
            db = "testing"

        self._client = clickhouse_connect.get_client(host="123.207.70.79", port=8123, username="default", password="zytz2020", database=db)

    def create_table(self):
        '''
        create the table
        '''
        self._client.command(all_securities_schema.create_table)

    def backfill_table(self):
        '''
        backfill the entire table
        '''


    def update_table(self):
        '''
        update the table with most recent data
        '''
        return

    def validate_table(self):

        return
