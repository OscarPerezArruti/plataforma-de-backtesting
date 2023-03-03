
##########################
## TWELVE DATA CONSTANS ##
##########################


ValidParameters = {
    "time_series": [
        "symbol",
        "interval",
        "apikey",
        "exchange",
        "mic_code",
        "country",
        "type",
        "outputsize",
        "format",
        "delimiter",
        "prepost",
        "dp",
        "order",
        "timezone",
        "date",
        "start_date",
        "end_date",
        "previous_close"],
    "quote": [
        "symbol",
        "interval",
        "exchange",
        "mic_code",
        "country",
        "volume_time_period",
        "type",
        "format",
        "delimiter",
        "apikey",
        "prepost",
        "eod",
        "rolling_period",
        "dp",
        "timezone"
    ],
    "exchange_rate": [
        "symbol",
        "date",
        "format",
        "delimiter",
        "apikey",
        "dp",
        "timezone"
    ],
    "stocks": [
        "symbol",
        "exchange",
        "mic_code",
        "country",
        "type",
        "format",
        "delimiter",
        "show_plan",
        "include_delisted",
    ],
    "etf": [
        "symbol",
        "exchange",
        "mic_code",
        "country",
        "format",
        "delimiter",
        "show_plan",
        "include_delisted",
    ],
    "indices": [
        "symbol",
        "exchange",
        "mic_code",
        "country",
        "format",
        "delimiter",
        "show_plan",
        "include_delisted",
    ],
    "exchanges": [
        "type",
        "name",
        "code",
        "country",
        "format",
        "delimiter",
        "show_plan",
    ],
    "technical_indicators": [],
    "symbol_search": [
        "symbol",
        "outputsize",
        "show_plan",
    ],
    "earliest_timestamp": [
        "symbol",
        "interval",
        "exchange",
        "mic_code",
        "apikey",
        "timezone",
    ],
    "market_state": [],


}
"""
ValidParameters stores every optional parameter
allowed for every endpoint of TwelveData API
"""

RequieredParameters = {
    "time_series": ["symbol","interval","apikey"],
    "quote": ["symbol","apikey"],
    "exchange_rate": ["symbol","apikey"],
    "stocks": [],
    "etf": [],
    "indices": [],
    "exchanges": [],
    "technical_indicators": [],
    "symbol_search": ["symbol"],
    "earliest_timestamp": ["symbol","interval","apikey"],
    "market_state": ["symbol","code","country","apikey"],
}
"""
ValidParameters stores every required parameter for 
every endpoint of TwelveData API
"""

validTimeSpans = [
    "1min", "5min", "15min", "30min",
    "45min", "1h", "2h", "4h", "1day", "1week", "1month"]
"""
validTimeSpans store all allowed time spans of TwelveData API
"""
