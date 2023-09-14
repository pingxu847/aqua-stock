create_table = "CREATE TABLE IF NOT EXISTS stk_xr_xd \
                (                          \
                 code String,              \
                 company_id Int32,         \
                 company_name String,      \
                 report_date Date,         \
                 bonus_type String,        \
                 board_plan_pub_date Date, \
                 board_plan_bonusnote String, \
                 distributed_share_base_board Decimal(20,4),         \
                 shareholders_plan_pub_date Date,         \
                 shareholders_plan_bonusnote String,      \
                 distributed_share_base_shareholders Decimal(20,4),         \
                 implementation_pub_date Date,         \
                 implementation_bonusnote String,         \
                 distributed_share_base_implement Decimal(20,4),        \
                 dividend_ratio Decimal(20,4),          \
                 transfer_ratio Decimal(20,4),          \
                 bonus_ratio_rmb Decimal(20,4),         \
                 bonus_ratio_usd Decimal(20,4),         \
                 bonus_ratio_hkd Decimal(20,4),         \
                 at_bonus_ratio_rmb Decimal(20,4),      \
                 exchange_rate Decimal(20,4),      \
                 dividend_number Decimal(20,4),      \
                 transfer_number Decimal(20,4),      \
                 bonus_amount_rmb Decimal(20,4),      \
                 a_registration_date Date,      \
                 b_registration_date Date,      \
                 a_xr_date Date,      \
                 b_xr_baseday Date,   \
                 b_final_trade_date Date,   \
                 a_bonus_date Date,   \
                 b_bonus_date Date,   \
                 dividend_arrival_date Date,   \
                 a_increment_listing_date Date,   \
                 b_increment_listing_date Date,   \
                 total_capital_before_transfer Decimal(20,4),      \
                 total_capital_after_transfer Decimal(20,4),      \
                 float_capital_before_transfer Decimal(20,4),      \
                 float_capital_after_transfer Decimal(20,4),      \
                 note String,      \
                 a_transfer_arrival_date Date,      \
                 b_transfer_arrival_date Date,      \
                 b_dividend_arrival_date Date,      \
                 note_of_no_dividend String,      \
                 plan_progress_code Int32, \
                 plan_progress String, \
                 bonus_cancel_pub_date Date,      \
                )                          \
                ENGINE = ReplacingMergeTree() \
                PRIMARY KEY (code)            \
                ORDER BY (code)"
