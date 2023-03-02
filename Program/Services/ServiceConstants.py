
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
    ]
}
"""
ValidParameters stores every optional parameter
allowed for every endpoint of TwelveData API
"""

RequieredParameters = {
    "time_series": [
        "symbol",
        "interval",
        "apikey"],
    "quote": [
        "symbol",
        "apikey"
    ]
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
