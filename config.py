import os

DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key-for-development-only')

FOREX_PAIRS = [
    'EURUSD=X', 'GBPUSD=X', 'AUDUSD=X', 'USDCAD=X', 'USDCHF=X', 'NZDUSD=X',
    'EURGBP=X', 'AUDJPY=X', 'EURAUD=X', 'EURCHF=X', 'AUDNZD=X',
    'NZDJPY=X', 'GBPAUD=X', 'GBPCAD=X', 'EURNZD=X', 'AUDCAD=X', 'GBPCHF=X', 'AUDCHF=X',
    'EURCAD=X', 'CADJPY=X', 'GBPNZD=X', 'CADCHF=X', 'CHFJPY=X', 'NZDCAD=X', 'NZDCHF=X', 'USDINR=X'
]

INTERVALS = ['5m', '15m', '1h', '1d']

RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_UNDERBOUGHT = 30

CACHE_TYPE = os.environ.get('CACHE_TYPE', 'SimpleCache')
CACHE_DEFAULT_TIMEOUT = int(os.environ.get('CACHE_TIMEOUT', '300'))

# 'USDJPY=X', 'EURJPY=X', 'GBPJPY=X', 
