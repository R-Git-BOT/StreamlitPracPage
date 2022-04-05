from django.forms import inlineformset_factory
import pandas as pd
import yfinance as yf
import altair as alt
import streamlit as st

aapl = yf.ticker('AAPL')
days = 20
hist = aapl.history(period = f'{days}d')
# histのデータ構造とは？ pandas.dataframe型
# headerが2段 dateがインデックスの役割をしている

hist.index = hist.index.strftime('%d %B %y')

# dataframe無いのcloseカラムのみぬきだし　
hist = hist[['Close']]
hist.columns = ['apple']

hist.T #銘柄を行名に持ってきたい
hist.index.name = 'Name'

tickers = {
    'apple':'AAPL',
    'facebook':'FB',
    'google':'GOOGL',
    'microsoft':'MSFT',
    'netflix':'NFLX',
    'amazon':'AMZN'
}

def get_data(days, tickers):    
    df = pd,DataFrame()
    for comp in tickers.key():
        print(company)
            #company = 'apple'
        tkr = yf.Ticker(tickers[company])
        hist = tkr.history(period = f'{days}d')
        hist.index = hist.index.strftime('%d %B %y')
        hist = hist[['Close']]
        hist.columns = [company]
        hist.T
        hist.index.name = 'Name'
        df = pd.concat([df,hist])
        # 現在のdfにhistを追加する

days = 20
data = get_data(days, tickers)

#streamlit と相性のいい Altair を使う
#altairに適合させるための形にする

data = data.T.reset_index()

#便利だけど分かりにくいデータフレームを再構築するPandasのMelt()関数のお話し
#Dateをキーとしてdataデータフレームを再構築 pivot関数の逆
#DateとどのColumn,値が連携しているか
data = pd.melt(data, id_vars = ['Date']).rename(
    columns={'value':'Stock Prices (USD)'}
)

chart = (
    alt.chart(data)
    .mark_line(opacity=0.8)
    .encode(
        x="Date:T",
        y=alt.Y("Stock Prices (USD):Q", stack=None),
        color="Name:N"
    )
)