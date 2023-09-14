'''
上市公司分红送股（除权除息）数据

from jqdata import finance
finance.run_query(query(finance.STK_XR_XD).filter(finance.STK_XR_XD.code==code).order_by(finance.STK_XR_XD.report_date).limit(n))
记录由上市公司年报、中报、一季报、三季报统计出的分红转增情况。

参数：

query(finance.STK_XR_XD)：表示从finance.STK_XR_XD这张表中查询上市公司除权除息的数据，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：sqlalchemy.orm.query.Query对象
finance.STK_XR_XD：代表除权除息数据表，记录由上市公司年报、中报、一季报、三季报统计出的分红转增情况。表结构和字段信息如下：

字段名称	中文名称	字段类型	能否为空	含义
code	股票代码	varchar(12)	N	加后缀
company_id	机构ID	int	N	
company_name	机构名称	varchar(100)		
report_date	分红报告期	date	N	一般为：一季报:YYYY-03-31;中报:YYYY-06-30;三季报:YYYY-09-30;年报:YYYY-12-31同时也可能存在其他日期
bonus_type	分红类型	varchar(60)		201102新增,类型如下：年度分红 中期分红 季度分红 特别分红 向公众股东赠送 股改分红
board_plan_pub_date	董事会预案公告日期	date		
board_plan_bonusnote	董事会预案分红说明	varchar(500)		每10股送XX转增XX派XX元
distributed_share_base_board	分配股本基数（董事会）	decimal(20,4)		单位:万股
shareholders_plan_pub_date	股东大会预案公告日期	date		
shareholders_plan_bonusnote	股东大会预案分红说明	varchar(200)		
distributed_share_base_shareholders	分配股本基数（股东大会）	decimal(20,4)		单位:万股
implementation_pub_date	实施方案公告日期	date		
implementation_bonusnote	实施方案分红说明	varchar(200)		维护规则: 每10股送XX转增XX派XX元 或:不分配不转赠
distributed_share_base_implement	分配股本基数（实施）			单位:万股
dividend_ratio	送股比例	decimal(20,4)		每10股送XX股
transfer_ratio	转增比例	decimal(20,4)		每10股转增 XX股 ；
bonus_ratio_rmb	派息比例(人民币)	decimal(20,4)		每10股派 XX。说明：这里的比例为最新的分配比例，预案公布的时候，预案的分配基数在此维护，如果股东大会或实施方案发生变化，再次进行修改，保证此处为最新的分配基数
bonus_ratio_usd	派息比例（美元）	decimal(20,4)		每10股派 XX。说明：这里的比例为最新的分配比例，预案公布的时候，预案的分配基数在此维护，如果股东大会或实施方案发生变化，再次进行修改，保证此处为最新的分配基数 如果这里只告诉了汇率，没有公布具体的外币派息，则要计算出；
bonus_ratio_hkd	派息比例（港币）	decimal(20,4)		每10股派 XX。说明：这里的比例为最新的分配比例，预案公布的时候，预案的分配基数在此维护，如果股东大会或实施方案发生变化，再次进行修改，保证此处为最新的分配基数 如果这里只告诉了汇率，没有公布具体的外币派息，则要计算出；
at_bonus_ratio_rmb	税后派息比例（人民币）	decimal(20,4)		
exchange_rate	汇率	decimal(20,4)		当日以外币（美元或港币）计价的B股价格兑换成人民币的汇率
dividend_number	送股数量	decimal(20,4)		单位：万股
transfer_number	转增数量	decimal(20,4)		单位：万股
bonus_amount_rmb	派息金额(人民币)	decimal(20,4)		单位：万元
a_registration_date	A股股权登记日	date		
b_registration_date	B股股权登记日	date		B股股权登记存在最后交易日，除权基准日以及股权登记日三个日期，由于B股实行T+3制度，最后交易日持有的股份需要在3个交易日之后确定股东身份，然后在除权基准日进行除权。
a_xr_date	A股除权日	date		
b_xr_baseday	B股除权基准日	date		根据B股实行T＋3交收制度,则B股的“股权登记日”是“最后交易日”后的第 三个交易日,直至“股权登记日”这一日为止,B股投资者的股权登记才告完成,也 就意味着B股股份至股权登记日为止,才真正划入B股投资者的名下。
b_final_trade_date	B股最后交易日	date		
a_bonus_date	派息日(A)	date		
b_bonus_date	派息日(B)	date		
dividend_arrival_date	红股到帐日	date		
a_increment_listing_date	A股新增股份上市日	date		
b_increment_listing_date	B股新增股份上市日	date		
total_capital_before_transfer	送转前总股本	decimal(20,4)		单位：万股
total_capital_after_transfer	送转后总股本	decimal(20,4)		单位：万股
float_capital_before_transfer	送转前流通股本	decimal(20,4)		单位：万股
float_capital_after_transfer	送转后流通股本	decimal(20,4)		单位：万股
note	备注	varchar(500)		
a_transfer_arrival_date	A股转增股份到帐日	date		
b_transfer_arrival_date	B股转增股份到帐日	date		
b_dividend_arrival_date	B股送红股到帐日	date		20080801新增
note_of_no_dividend	有关不分配的说明	varchar(1000)		
plan_progress_code	方案进度编码	int		
plan_progress	方案进度	varchar(60)		董事会预案 实施方案 股东大会预案 取消分红 公司预案 延迟实施
bonus_cancel_pub_date	取消分红公告日期	date
'''

import jqdatasdk
import clickhouse_connect
import stk_xr_xd_schema

class StkXrXd:
    def __init__(self, tenancy):
        db = "stock"
        if tenancy == "testing":
            db = "testing"

        self._client = clickhouse_connect.get_client(host="123.207.70.79", port=8123, username="default", password="zytz2020", database=db)

    def create_table(self):
        '''
        create the table
        '''
        self._client.command(stk_xr_xd_schema.create_table)

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
