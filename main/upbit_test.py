import upbit_get_info
import pyupbit

def backtest(ticker, days): # days : 조회하고 싶은 일수
    df = make