import requests
from collections import Counter
from loguru import logger


headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary',
    'DNT': '1',
    'Origin': 'https://emrnweb.eastmoney.com',
    'Referer': 'https://emrnweb.eastmoney.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}


def stock_lst(data):
    response = requests.post('https://datacenter.eastmoney.com/stock/selection/api/data/get/', headers=headers, data=data.encode())
    resp = response.json()
    if resp['success']:
        return resp['result']['data']
    else:
        logger.info(resp)
        return []


def get_stock_list():
    all_result = []
    stock_set = {}
    # 精选白马
    data = '------WebKitFormBoundary\r\nContent-Disposition: form-data; name="type"\r\n\r\nRPTA_APP_STOCKSELECT\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="sty"\r\n\r\nSECUCODE,SECURITY_CODE,SECURITY_NAME_ABBR,NEW_PRICE,CHANGE_RATE,BASIC_EPS,NETPROFIT_YOY_RATIO,PE9,ROE_WEIGHT,TOI_YOY_RATIO\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="filter"\r\n\r\n(BASIC_EPS>=0.5)(NETPROFIT_YOY_RATIO>=15)(PE9>=0)(PE9<=40)(ROE_WEIGHT>=15)(TOI_YOY_RATIO>=20)\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="p"\r\n\r\n1\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ps"\r\n\r\n400\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="sr"\r\n\r\n-1\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="st"\r\n\r\nCHANGE_RATE\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="source"\r\n\r\nSELECT_SECURITIES\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="client"\r\n\r\nAPP\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ct"\r\n\r\n\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ut"\r\n\r\n\r\n------WebKitFormBoundary--\r\n'
    for stock in stock_lst(data):
        all_result.append(stock)
        if stock['SECURITY_NAME_ABBR'] not in stock_set:
            stock_set[stock['SECURITY_NAME_ABBR']] = []
        stock_set[stock['SECURITY_NAME_ABBR']].append('精选白马')

    # 高送转预期
    data = '------WebKitFormBoundary\r\nContent-Disposition: form-data; name="type"\r\n\r\nRPTA_APP_STOCKSELECT\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="sty"\r\n\r\nSECUCODE,SECURITY_CODE,SECURITY_NAME_ABBR,NEW_PRICE,CHANGE_RATE,BASIC_EPS,BVPS,PER_CAPITAL_RESERVE,PER_UNASSIGN_PROFIT,TOTAL_MARKET_CAP\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="filter"\r\n\r\n(BASIC_EPS>=0.5)(BVPS>5)(PER_CAPITAL_RESERVE>=3)(PER_UNASSIGN_PROFIT>=2)(TOTAL_MARKET_CAP<=20000000000)\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="p"\r\n\r\n1\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ps"\r\n\r\n400\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="sr"\r\n\r\n-1\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="st"\r\n\r\nCHANGE_RATE\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="source"\r\n\r\nSELECT_SECURITIES\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="client"\r\n\r\nAPP\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ct"\r\n\r\n\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ut"\r\n\r\n\r\n------WebKitFormBoundary--\r\n'
    for stock in stock_lst(data):
        all_result.append(stock)
        if stock['SECURITY_NAME_ABBR'] not in stock_set:
            stock_set[stock['SECURITY_NAME_ABBR']] = []
        stock_set[stock['SECURITY_NAME_ABBR']].append('高送转预期')
    # 格雷厄姆
    data = '------WebKitFormBoundary\r\nContent-Disposition: form-data; name="type"\r\n\r\nRPTA_APP_STOCKSELECT\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="sty"\r\n\r\nSECUCODE,SECURITY_CODE,SECURITY_NAME_ABBR,NEW_PRICE,CHANGE_RATE,GRAHAM_STOCK\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="filter"\r\n\r\n(GRAHAM_STOCK="1")\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="p"\r\n\r\n1\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ps"\r\n\r\n400\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="sr"\r\n\r\n-1\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="st"\r\n\r\nCHANGE_RATE\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="source"\r\n\r\nSELECT_SECURITIES\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="client"\r\n\r\nAPP\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ct"\r\n\r\n\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ut"\r\n\r\n\r\n------WebKitFormBoundary--\r\n'
    for stock in stock_lst(data):
        all_result.append(stock)
        if stock['SECURITY_NAME_ABBR'] not in stock_set:
            stock_set[stock['SECURITY_NAME_ABBR']] = []
        stock_set[stock['SECURITY_NAME_ABBR']].append('格雷厄姆')
    # 绩优大盘股
    data = '------WebKitFormBoundary\r\nContent-Disposition: form-data; name="type"\r\n\r\nRPTA_APP_STOCKSELECT\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="sty"\r\n\r\nSECUCODE,SECURITY_CODE,SECURITY_NAME_ABBR,NEW_PRICE,CHANGE_RATE,NETPROFIT_YOY_RATIO,PE9,ROE_WEIGHT,TOI_YOY_RATIO,TOTAL_MARKET_CAP\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="filter"\r\n\r\n(NETPROFIT_YOY_RATIO>=5)(PE9>=0)(PE9<=30)(ROE_WEIGHT>=20)(TOI_YOY_RATIO>=20)(TOTAL_MARKET_CAP>50000000000)\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="p"\r\n\r\n1\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ps"\r\n\r\n400\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="sr"\r\n\r\n-1\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="st"\r\n\r\nCHANGE_RATE\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="source"\r\n\r\nSELECT_SECURITIES\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="client"\r\n\r\nAPP\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ct"\r\n\r\n\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ut"\r\n\r\n\r\n------WebKitFormBoundary--\r\n'
    for stock in stock_lst(data):
        all_result.append(stock)
        if stock['SECURITY_NAME_ABBR'] not in stock_set:
            stock_set[stock['SECURITY_NAME_ABBR']] = []
        stock_set[stock['SECURITY_NAME_ABBR']].append('绩优大盘股')
    # 高股息
    data = '------WebKitFormBoundary\r\nContent-Disposition: form-data; name="type"\r\n\r\nRPTA_APP_STOCKSELECT\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="sty"\r\n\r\nSECUCODE,SECURITY_CODE,SECURITY_NAME_ABBR,NEW_PRICE,CHANGE_RATE,PE9,TOTAL_MARKET_CAP,ZXGXL\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="filter"\r\n\r\n(PE9>=0)(PE9<=20)(TOTAL_MARKET_CAP>=20000000000)(ZXGXL>=4)\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="p"\r\n\r\n1\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ps"\r\n\r\n400\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="sr"\r\n\r\n-1\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="st"\r\n\r\nCHANGE_RATE\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="source"\r\n\r\nSELECT_SECURITIES\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="client"\r\n\r\nAPP\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ct"\r\n\r\n\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ut"\r\n\r\n\r\n------WebKitFormBoundary--\r\n'
    for stock in stock_lst(data):
        all_result.append(stock)
        if stock['SECURITY_NAME_ABBR'] not in stock_set:
            stock_set[stock['SECURITY_NAME_ABBR']] = []
        stock_set[stock['SECURITY_NAME_ABBR']].append('高股息')
    # 高盈利价值
    data = '------WebKitFormBoundary\r\nContent-Disposition: form-data; name="type"\r\n\r\nRPTA_APP_STOCKSELECT\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="sty"\r\n\r\nSECUCODE,SECURITY_CODE,SECURITY_NAME_ABBR,NEW_PRICE,CHANGE_RATE,PBNEWMRQ,ROE_WEIGHT\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="filter"\r\n\r\n(PBNEWMRQ>0)(PBNEWMRQ<=5)(ROE_WEIGHT>=10)\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="p"\r\n\r\n1\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ps"\r\n\r\n400\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="sr"\r\n\r\n-1\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="st"\r\n\r\nCHANGE_RATE\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="source"\r\n\r\nSELECT_SECURITIES\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="client"\r\n\r\nAPP\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ct"\r\n\r\n\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ut"\r\n\r\n\r\n------WebKitFormBoundary--\r\n'
    for stock in stock_lst(data):
        all_result.append(stock)
        if stock['SECURITY_NAME_ABBR'] not in stock_set:
            stock_set[stock['SECURITY_NAME_ABBR']] = []
        stock_set[stock['SECURITY_NAME_ABBR']].append('高盈利价值')
    # 业绩翻倍
    data = '------WebKitFormBoundary\r\nContent-Disposition: form-data; name="type"\r\n\r\nRPTA_APP_STOCKSELECT\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="sty"\r\n\r\nSECUCODE,SECURITY_CODE,SECURITY_NAME_ABBR,NEW_PRICE,CHANGE_RATE,NETPROFIT_YOY_RATIO,TOI_YOY_RATIO\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="filter"\r\n\r\n(NETPROFIT_YOY_RATIO>100)(TOI_YOY_RATIO>100)\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="p"\r\n\r\n1\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ps"\r\n\r\n300\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="sr"\r\n\r\n-1\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="st"\r\n\r\nCHANGE_RATE\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="source"\r\n\r\nSELECT_SECURITIES\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="client"\r\n\r\nAPP\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ct"\r\n\r\n\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ut"\r\n\r\n\r\n------WebKitFormBoundary--\r\n'
    for stock in stock_lst(data):
        all_result.append(stock)
        if stock['SECURITY_NAME_ABBR'] not in stock_set:
            stock_set[stock['SECURITY_NAME_ABBR']] = []
        stock_set[stock['SECURITY_NAME_ABBR']].append('业绩翻倍')
    # 彼得林奇
    data = '------WebKitFormBoundary\r\nContent-Disposition: form-data; name="type"\r\n\r\nRPTA_APP_STOCKSELECT\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="sty"\r\n\r\nSECUCODE,SECURITY_CODE,SECURITY_NAME_ABBR,NEW_PRICE,CHANGE_RATE,PETERLYNCH_STOCK\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="filter"\r\n\r\n(PETERLYNCH_STOCK="1")\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="p"\r\n\r\n1\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ps"\r\n\r\n400\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="sr"\r\n\r\n-1\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="st"\r\n\r\nCHANGE_RATE\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="source"\r\n\r\nSELECT_SECURITIES\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="client"\r\n\r\nAPP\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ct"\r\n\r\n\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ut"\r\n\r\n\r\n------WebKitFormBoundary--\r\n'
    for stock in stock_lst(data):
        all_result.append(stock)
        if stock['SECURITY_NAME_ABBR'] not in stock_set:
            stock_set[stock['SECURITY_NAME_ABBR']] = []
        stock_set[stock['SECURITY_NAME_ABBR']].append('彼得林奇')
    # 社保大量持股
    data = '------WebKitFormBoundary\r\nContent-Disposition: form-data; name="type"\r\n\r\nRPTA_APP_STOCKSELECT\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="sty"\r\n\r\nSECUCODE,SECURITY_CODE,SECURITY_NAME_ABBR,NEW_PRICE,CHANGE_RATE,SOCIAL_STOCK_HOLD\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="filter"\r\n\r\n(SOCIAL_STOCK_HOLD="1")\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="p"\r\n\r\n1\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ps"\r\n\r\n400\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="sr"\r\n\r\n-1\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="st"\r\n\r\nCHANGE_RATE\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="source"\r\n\r\nSELECT_SECURITIES\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="client"\r\n\r\nAPP\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ct"\r\n\r\n\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ut"\r\n\r\n\r\n------WebKitFormBoundary--\r\n'
    for stock in stock_lst(data):
        all_result.append(stock)
        if stock['SECURITY_NAME_ABBR'] not in stock_set:
            stock_set[stock['SECURITY_NAME_ABBR']] = []
        stock_set[stock['SECURITY_NAME_ABBR']].append('社保大量持股')
    # 高成长优选
    data = '------WebKitFormBoundary\r\nContent-Disposition: form-data; name="type"\r\n\r\nRPTA_APP_STOCKSELECT\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="sty"\r\n\r\nSECUCODE,SECURITY_CODE,SECURITY_NAME_ABBR,NEW_PRICE,CHANGE_RATE,NETPROFIT_YOY_RATIO,PE9,PS9,TOI_YOY_RATIO\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="filter"\r\n\r\n(NETPROFIT_YOY_RATIO>=30)(NETPROFIT_YOY_RATIO<=1000)(PE9>=0)(PE9<=50)(PS9>=0)(PS9<=2)(TOI_YOY_RATIO>=30)(TOI_YOY_RATIO<=1000)\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="p"\r\n\r\n1\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ps"\r\n\r\n200\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="sr"\r\n\r\n-1\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="st"\r\n\r\nCHANGE_RATE\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="source"\r\n\r\nSELECT_SECURITIES\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="client"\r\n\r\nAPP\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ct"\r\n\r\n\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ut"\r\n\r\n\r\n------WebKitFormBoundary--\r\n'
    for stock in stock_lst(data):
        all_result.append(stock)
        if stock['SECURITY_NAME_ABBR'] not in stock_set:
            stock_set[stock['SECURITY_NAME_ABBR']] = []
        stock_set[stock['SECURITY_NAME_ABBR']].append('高成长优选')
    # 机构主力关注
    data = '------WebKitFormBoundary\r\nContent-Disposition: form-data; name="type"\r\n\r\nRPTA_APP_STOCKSELECT\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="sty"\r\n\r\nSECUCODE,SECURITY_CODE,SECURITY_NAME_ABBR,NEW_PRICE,CHANGE_RATE,CHANGERATE_3DAYS,NETINFLOW_5DAYS,ORG_RATING\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="filter"\r\n\r\n(CHANGERATE_3DAYS>=5)(NETINFLOW_5DAYS>=0)(ORG_RATING IN ("买入","买入-") )\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="p"\r\n\r\n1\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ps"\r\n\r\n300\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="sr"\r\n\r\n-1\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="st"\r\n\r\nCHANGE_RATE\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="source"\r\n\r\nSELECT_SECURITIES\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="client"\r\n\r\nAPP\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ct"\r\n\r\n\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ut"\r\n\r\n\r\n------WebKitFormBoundary--\r\n'
    for stock in stock_lst(data):
        all_result.append(stock)
        if stock['SECURITY_NAME_ABBR'] not in stock_set:
            stock_set[stock['SECURITY_NAME_ABBR']] = []
        stock_set[stock['SECURITY_NAME_ABBR']].append('高成长优选')
    # 估值三低
    data = '------WebKitFormBoundary\r\nContent-Disposition: form-data; name="type"\r\n\r\nRPTA_APP_STOCKSELECT\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="sty"\r\n\r\nSECUCODE,SECURITY_CODE,SECURITY_NAME_ABBR,NEW_PRICE,CHANGE_RATE,DUNMPTON_STRATEGY\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="filter"\r\n\r\n(DUNMPTON_STRATEGY="1")\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="p"\r\n\r\n1\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ps"\r\n\r\n300\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="sr"\r\n\r\n-1\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="st"\r\n\r\nCHANGE_RATE\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="source"\r\n\r\nSELECT_SECURITIES\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="client"\r\n\r\nAPP\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ct"\r\n\r\n\r\n------WebKitFormBoundary\r\nContent-Disposition: form-data; name="ut"\r\n\r\n\r\n------WebKitFormBoundary--\r\n'
    for stock in stock_lst(data):
        all_result.append(stock)
        if stock['SECURITY_NAME_ABBR'] not in stock_set:
            stock_set[stock['SECURITY_NAME_ABBR']] = []
        stock_set[stock['SECURITY_NAME_ABBR']].append('估值三低')

    return all_result, stock_set

if __name__ == '__main__':
    stock_list, stock_set = get_stock_list()
    temp = Counter([i['SECURITY_NAME_ABBR'] for i in stock_list])
    res_list = sorted(temp.items(), key=lambda x: x[1])
    res_dict = dict(res_list)

    for i in stock_set:
        if i in ['宇信科技', '中原传媒', '永辉超市', '大族激光', '歌尔股份']:
            logger.info(i)
    for i in res_list:
        if i[1] < 3:
            continue
        if '彼得林奇' in stock_set[i[0]] and '格雷厄姆' in stock_set[i[0]]:
            logger.info(f'{i[0]}: {"-".join(stock_set[i[0]])}')
        if '社保大量持股' in stock_set[i[0]]:
            logger.info(f'{i[0]}: {"-".join(stock_set[i[0]])}')
