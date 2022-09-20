#!/usr/bin/env python3
from loguru import logger
import talib as tb
import pandas as pd


def technical_indicators_df(daily_data):
    """
    Assemble a dataframe of technical indicator series for a single stock
    """
    o = daily_data['open']#.astype(float).values
    c = daily_data['close']#astype(float).values
    h = daily_data['high']#astype(float).values
    l = daily_data['low']#astype(float).values
    v = daily_data['volume']#astype(float).values
    # define the technical analysis matrix


    # Most data series are normalized by their series' mean
    ta = pd.DataFrame()
    ta['MA5'] = tb.MA(c)  / tb.MA(c, timeperiod=5).mean()
    ta['MA10'] = tb.MA(c, timeperiod=10) / tb.MA(c, timeperiod=10).mean()
    ta['MA20'] = tb.MA(c, timeperiod=20) / tb.MA(c, timeperiod=20).mean()
    ta['MA60'] = tb.MA(c, timeperiod=60) / tb.MA(c, timeperiod=60).mean()
    ta['MA120'] = tb.MA(c, timeperiod=120) / tb.MA(c, timeperiod=120).mean()
    ta['MA5'] = tb.MA(v, timeperiod=5) / tb.MA(v, timeperiod=5).mean()
    ta['MA10'] = tb.MA(v, timeperiod=10) / tb.MA(v, timeperiod=10).mean()
    ta['MA20'] = tb.MA(v, timeperiod=20) / tb.MA(v, timeperiod=20).mean()
    ta['ADX'] = tb.ADX(h, l, c, timeperiod=14) / tb.ADX(h, l, c, timeperiod=14).mean()
    ta['ADXR'] = tb.ADXR(h, l, c, timeperiod=14) / tb.ADXR(h, l, c, timeperiod=14).mean()
    ta['MACD'] = tb.MACD(c, fastperiod=12, slowperiod=26, signalperiod=9)[0] / \
                 tb.MACD(c, fastperiod=12, slowperiod=26, signalperiod=9)[0].mean()
    ta['RSI'] = tb.RSI(c, timeperiod=12)
    ta['BBANDS_U'] = tb.BBANDS(c, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)[0] / \
                     tb.BBANDS(c, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)[0].mean()
    ta['BBANDS_M'] = tb.BBANDS(c, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)[1] / \
                     tb.BBANDS(c, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)[1].mean()
    ta['BBANDS_L'] = tb.BBANDS(c, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)[2] / \
                     tb.BBANDS(c, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)[2].mean()
    ta['AD'] = tb.AD(h, l, c, v) / tb.AD(h, l, c, v).mean()
    ta['ATR'] = tb.ATR(h, l, c, timeperiod=14) / tb.ATR(h, l, c, timeperiod=14).mean()
    ta['HT_DC'] = tb.HT_DCPERIOD(c) / tb.HT_DCPERIOD(c).mean()
    ta["High/Open"] = h / o
    ta["Low/Open"] = l / o
    ta["Close/Open"] = c / o

    return ta
