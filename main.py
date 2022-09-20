from loguru import logger
from eastmoney_xuanguqi import get_stock_list
import tushare as ts
from data_process import technical_indicators_df
import numpy
import talib as ta


if __name__ == '__main__':
    stock_list, _ = get_stock_list()
    for stock in stock_list:
        if 'BJ' in stock['SECUCODE']:
            # 跳过北京交易所
            logger.info(stock)
            continue
        code = stock['SECURITY_CODE']
        dw = ts.get_k_data(code, start='2022-06-27')
        # logger.info(dw)
        dw.index = range(len(dw))
        close = dw.close.values
        dw["rsi"] = ta.RSI(close, timeperiod=12)
        logger.info(dw)
        # tb_data = technical_indicators_df(hist_data)
        logger.info(stock)
        break
