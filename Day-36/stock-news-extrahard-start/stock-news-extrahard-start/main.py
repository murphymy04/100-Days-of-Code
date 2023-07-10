import requests
from datetime import date, timedelta
import statistics
from twilio.rest import Client
import smtplib
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_VANTAGE_API_KEY = "P66EH1N17WIUCCVE"
NEWS_API_KEY = "d99e9eced686414bb5b31d3ba40281f4"
ACCOUNT_SID = "AC3b24caa29feb5cbdc9f60823232205c2"
AUTH_TOKEN = "ff7d824d83e3a05c86d3292252233c2c"
TWILIO_PHONE = "+18885133013"
my_email = "mylesm2004@gmail.com"
password = "tntkwbeyxhwjoxgb"


# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def get_stocks(stock, api_key):
    response = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={stock}'
                            f'&apikey={api_key}')
    response.raise_for_status()
    data = response.json()
    time_series = data["Time Series (Daily)"]
    today = date.today()
    yesterday = today - timedelta(days=1)
    day_before = yesterday - timedelta(days=1)
    yesterday_stock = float(time_series[f"{yesterday}"]["4. close"])
    day_before_stock = float(time_series[f"{day_before}"]["4. close"])
    difference = ((yesterday_stock - day_before_stock)/statistics.mean([yesterday_stock, day_before_stock])) * 100
    return difference


# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def get_news(api_key, company_name):
    response = requests.get(f'https://newsapi.org/v2/everything?q={company_name}&apiKey={api_key}')
    response.raise_for_status()
    data = response.json()
    all_articles = data["articles"]
    articles = [article["title"] for article in all_articles][0:3]
    return articles


# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
def sms(auth, sid, out_phone, in_phone, news, difference):
    client = Client(sid, auth)
    if difference > 0:
        message = client.messages.create(
            body=f"Tesla:🔺{abs(difference)}%\n"
                 f"Headline 1: {news[0]}\n"
                 f"Headline 2: {news[1]}\n"
                 f"Headline 3: {news[2]}",
            from_=out_phone,
            to=in_phone
        )
    elif difference < 0:
        message = client.messages.create(
            body=f"Tesla:🔻{abs(difference)}%\n"
                 f"Headline 1: {news[0]}\n"
                 f"Headline 2: {news[1]}\n"
                 f"Headline 3: {news[2]}",
            from_=out_phone,
            to=in_phone
        )


def email(email, password, news, difference):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        if difference > 0:
            connection.sendmail(from_addr=email, to_addrs=email, msg=f"Subject: Tesla: Up {abs(difference)}%\n\n"
                 f"Headline 1: {news[0]}\n"
                 f"Headline 2: {news[1]}\n"
                 f"Headline 3: {news[2]}")
        elif difference < 0:
            connection.sendmail(from_addr=email, to_addrs=email, msg=f"Subject: Tesla: Down {abs(difference)}%\n\n"
                 f"Headline 1: {news[0]}\n"
                 f"Headline 2: {news[1]}\n"
                 f"Headline 3: {news[2]}")


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

stock_difference = get_stocks(STOCK, ALPHA_VANTAGE_API_KEY)
if abs(stock_difference) >= 5:
    news = get_news(NEWS_API_KEY, COMPANY_NAME)
    email(my_email, password, news, stock_difference)
