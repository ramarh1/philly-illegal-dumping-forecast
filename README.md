# Illegal Dumping Forecasting Tool

#### Problem: Forecast weekly counts of Philadelphia 311 **illegal dumping** requests to support staffing and cleanup planning

**Data**
- Source: OpenDataPhilly - CARTO table public_cases_fc (service_code = SR-ST02)
- Range: 2016-present (daily aggregated to weekly)
- Files: 'data/illegal_dumping_daily.csv', 'data/illegal_dumping_weekly.csv'

**Method**
- Baseline: Prophet (weekly and yearly seasonality)
- Advanced: LSTM (lookback=12 weeks), optional exogenous features (weather, holidays)

**Backtesting**
- Time-based split 70/15/15 (train/val/test)
- LTSM -> RMSE: 2.98
- Metrics: MAE; naseline = naïve last-value

**Results**
**Prophet**
<img width="989" height="590" alt="image" src="https://github.com/user-attachments/assets/8825b113-44c4-4a9a-8f74-4909a73eb4cb" />
<img width="886" height="890" alt="image" src="https://github.com/user-attachments/assets/ceae92bb-1b2a-4e66-9905-6868986ded5d" />
<img width="989" height="590" alt="image" src="https://github.com/user-attachments/assets/56a7f2de-df3d-41bc-99b5-1616a030096c" />

**LSTM**
<img width="996" height="547" alt="image" src="https://github.com/user-attachments/assets/5709897c-1683-4e75-85f0-e0be283872e7" />
  
- LSTM error table + plots, table + chart; when each model wins; error analysis

**Limitations**: 
- Reporting changes, COVID shifts, category drift.

**Key Insights**:
- Illegal dumping 311 reports have spiked most often in July and August in recent years.
- Reports are typically made Monday through Wednesday, suggesting that illegal dumping increases over the weekend.

**How to run**: 
- Elaborate on how to run each file type...make_dataset.py -> notebooks -> app

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
