import jqdatasdk
import clickhouse_connect
import datetime

class AquaStock:
    def __init__(self, ip, port, user, passwd):
        self._client = clickhouse_connect.get_client(host=ip, port=port, username=user, password=passwd, database="stock")

    def create_daily(self):
        self._client.command("CREATE TABLE IF NOT EXISTS daily  \
                              (                          \
                                time Date,              \
                                code String,            \
                                open Float32,           \
                                high Float32,           \
                                low Float32,            \
                                close Float32,          \
                                volume Float32,         \
                                money Float32,          \
                                factor Float32,         \
                                high_limit Float32,     \
                                low_limit Float32,      \
                                avg Float32,            \
                                pre_close Float32,      \
                                paused Float32          \
                              )                          \
                              ENGINE = ReplacingMergeTree() \
                              PRIMARY KEY (time, code)    \
                              ORDER BY (time, code)")

    def insert_daily_bar(self, start_time, end_time):
        """
        insert daily table from jq interface get_price
        """
        # 1312037935 for stock and etf
        jqdatasdk.auth("13120379359", "Zytz2020")
        code_df = jqdatasdk.get_all_securities(['stock', 'etf'])
        code_list = list(code_df.index)
        for i in range(0, len(code_list), 10):
            chunk = code_list[i: i+10]
            df = jqdatasdk.get_price(chunk, start_date = start_time, end_date = end_time, frequency="daily", fq=None,
                        fields=['open', 'close', 'low', 'high', 'volume', 'money', 'factor', 'high_limit','low_limit', 'avg', 'pre_close', 'paused'])
            self._client.insert_df('daily', df)
            print(f"insert code: {chunk}")
        # 17621627675 for index
        jqdatasdk.auth("17621627675", "Zytz2020")
        index_df = jqdatasdk.get_all_securities(['index'])
        index_list = list(index_df.index)
        for i in range(0, len(index_list), 10):
            chunk = index_list[i: i+10]
            df = jqdatasdk.get_price(chunk, start_date = start_time, end_date = end_time, frequency="daily", fq=None,
                        fields=['open', 'close', 'low', 'high', 'volume', 'money', 'factor', 'high_limit','low_limit', 'avg', 'pre_close', 'paused'])
            self._client.insert_df('daily', df)
            print(f"insert code: {chunk}")

    def update_daily_bar(self):
        """
        update daily table to today
        """
        result = self._client.query("SELECT time FROM daily ORDER BY time DESC LIMIT 1")
        start_time = str(result.first_item['time'])
        end_time = str(datetime.date.today())
        # 1312037935 for stock and etf
        jqdatasdk.auth("13120379359", "Zytz2020")
        code_df = jqdatasdk.get_all_securities(['stock', 'etf'])
        code_list = list(code_df.index)
        for i in range(0, len(code_list), 10):
            chunk = code_list[i: i+10]
            df = jqdatasdk.get_price(chunk, start_date = start_time, end_date = end_time, frequency="daily", fq=None,
                        fields=['open', 'close', 'low', 'high', 'volume', 'money', 'factor', 'high_limit','low_limit', 'avg', 'pre_close', 'paused'])
            self._client.insert_df('daily', df)
            print(f'update stock and etf {chunk} from {start_time} to now')
        # 17621627675 for index
        jqdatasdk.auth("17621627675", "Zytz2020")
        index_df = jqdatasdk.get_all_securities(['index'])
        index_list = list(index_df.index)
        for i in range(0, len(index_list), 10):
            chunk = index_list[i: i+10]
            df = jqdatasdk.get_price(chunk, start_date = start_time, end_date = end_time, frequency="daily", fq=None,
                        fields=['open', 'close', 'low', 'high', 'volume', 'money', 'factor', 'high_limit','low_limit', 'avg', 'pre_close', 'paused'])
            self._client.insert_df('daily', df)
            print(f'update index {chunk} from {start_time} to now')

if __name__ == "__main__":
    demo = AquaStock("123.207.70.79", 8123, "default", "zytz2020")
    demo.create_daily()
    demo.insert_daily_bar("2019-01-01", "2023-09-01")
    demo.update_daily_bar()
