# Illegal Dumping Forecasting Tool

#### Problem: Forecast weekly counts of Philadelphia 311 **illegal dumping** requests to support staffing and cleanup planning

**Data**:
- Source: OpenDataPhilly - CARTO table public_cases_fc (service_code = SR-ST02)
- Range: 2016-present (daily aggregated to weekly)
- Files: 'data/illegal_dumping_daily.csv', 'data/illegal_dumping_weekly.csv'

**Method**:
- Baseline: Prophet (weekly and yearly seasonality)
- Advanced: LSTM (lookback=12 weeks), optional exogenous features (weather, holidays)

**Backtesting**:
- Time-based split 70/15/15 (train/val/test)
- Metrics: MAE, RMSE; naseline = naïve last-value

**Results**:
- (fill in) Prophet vs LSTM error table + plots
- table + chart; when each model wins; error analysis

**Limitations**: 
- Reporting changes, COVID shifts, category drift.

**How to run**: 
- elaborate on how to run each file type...make_dataset.py -> notebooks -> app

1. check status of api:
curl --get "https://phl.carto.com/api/v2/sql" \
  --data-urlencode "q=SELECT date_trunc('day', requested_datetime)::date AS day,
                           COUNT(*) AS cnt
                    FROM public_cases_fc
                    WHERE service_code = 'SR-ST02'
                      AND requested_datetime >= '2016-01-01'
                    GROUP BY 1
                    ORDER BY 1" \
  --data-urlencode "format=csv" \
  -o ./illegal_dumping_daily.csv
