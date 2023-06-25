import pandas as pd
def price(loca):
    data=pd.read_csv(loca)
    data.drop(['1. open','2. high','3. low','5. volume'],axis=1,inplace=True)
    data.rename(columns={'date':'ds','4. close':'y'},inplace=True)
    from prophet import Prophet
    a=Prophet()
    a.fit(data)
    future=a.make_future_dataframe(periods=31)
    predict_price=a.predict(future)
    price=pd.DataFrame(predict_price)
    return price
