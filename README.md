# Illegal Dumping Forecasting Tool
[EDIT THESE PLACEHOLDERS]
**Problem**: forecast illegal dumping 311 requests in Philly

**Data**: OpenDataPhilly 311 (CARTO public_cases_fc), data span used, filters

**Method**: Prophet baseline; LSTM advanced; exogenous vars if used.

**Backtesting**: how data was split, metrics.

**Results**: table + chart; when each model wins; error analysis

**Limitations**: reporting changes, COVID shifts, category drift.

**How to run**: elaborate on how to run each file type...make_dataset.py -> notebooks -> app

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
