def pasg():
    import time
    import pandas as pd
    from alpha_vantage.timeseries import TimeSeries
    import threading
    o=1
    while o==1:
        api_key="JEYQ8PRP5P4YLMGF"
        from alpha_vantage.timeseries import TimeSeries
        ts=TimeSeries(key="api_key",output_format='pandas')
        data=ts.get_intraday(symbol='MSFT',interval='1min',outputsize="full")
        data1=ts.get_intraday(symbol='AAPL',interval='1min',outputsize="full")
        data2=ts.get_intraday(symbol='GOOGL',interval='1min',outputsize="full")
        data3=ts.get_intraday(symbol='AMZN',interval='1min',outputsize="full")
        data4=ts.get_intraday(symbol='TSLA',interval='1min',outputsize="full")
        data[0].to_csv('data.csv')
        data1[0].to_csv('data1.csv')
        data2[0].to_csv('data2.csv')
        data3[0].to_csv('data3.csv')
        data4[0].to_csv('data4.csv')

    
    time.sleep(3600)