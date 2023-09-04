# stock database

## create database

```sql
CREATE DATABASE STOCK
```

## create table

```sql
CREATE TABLE daily 
(
    timestamp Date, 
    symbol String, 
    open Float32, 
    high Float32, 
    low Float32, 
    close Float32, 
    volume UInt32
) 
ENGINE = ReplacingMergeTree() 
PRIMARY KEY (timestamp, symbol) 
ORDER BY (timestamp, symbol)
PARTION BY toYYYY(timestamp)
```
这里假定日线表中，所含字段只包括日期，股票代码，还有开高低收，成交量这几个字段，上述创建语句使用时间和代码作为主键并排序，然后使用年份做表的分区（可选）

## add column

```sql
ADD COLUMN daily ma10 Float32
```
上述为日线表增加一列10日均线，该操作只改变表结构，不插入真实数据
