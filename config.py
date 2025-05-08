# Configuration settings
import os
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

# Flask configuration
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key-for-forex-screener')
DEBUG = os.environ.get('FLASK_DEBUG', 'True').lower() in ('true', '1', 't')

# Forex pairs configuration
FOREX_PAIRS = [
    'EURUSD=X', 'USDJPY=X', 'GBPUSD=X', 'AUDUSD=X', 'USDCAD=X', 'USDCHF=X', 'NZDUSD=X',
    'EURJPY=X', 'GBPJPY=X', 'EURGBP=X', 'AUDJPY=X', 'EURAUD=X', 'EURCHF=X', 'AUDNZD=X',
    'NZDJPY=X', 'GBPAUD=X', 'GBPCAD=X', 'EURNZD=X', 'AUDCAD=X', 'GBPCHF=X', 'AUDCHF=X',
    'EURCAD=X', 'CADJPY=X', 'GBPNZD=X', 'CADCHF=X', 'CHFJPY=X', 'NZDCAD=X', 'NZDCHF=X', 'USDINR=X'
]

# Available time intervals
TIME_INTERVALS = ['5m', '15m', '1h', '1d']