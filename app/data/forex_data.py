import yfinance as yf
import pandas as pd
import time
import random
from datetime import datetime, timedelta
from app import cache
from config import FOREX_PAIRS
from app.models.indicators import calculate_rsi

def try_yf_download(ticker, interval, start=None, end=None):
    """
    Attempt to download data from yfinance with retry mechanism using date ranges
    
    Args:
        ticker (str): Forex pair symbol
        interval (str): Time interval between data points
        start (str): Start date for data
        end (str): End date for data
        
    Returns:
        pandas.DataFrame or None: DataFrame with price data or None if download failed
    """
    max_retries = 3 
    retry_delay = 5 
    
    for attempt in range(max_retries):
        try:
            df = yf.download(ticker, start=start, end=end, interval=interval, auto_adjust=False)
                
            if not df.empty and 'Close' in df.columns:
                return df
                
            if attempt < max_retries - 1:  
                print(f"Empty dataframe for {ticker}, retrying in {retry_delay} seconds... (Attempt {attempt+1}/{max_retries})")
                time.sleep(retry_delay)
                
        except Exception as e:
            if attempt < max_retries - 1:  
                print(f"Error downloading {ticker}, retrying in {retry_delay} seconds... (Attempt {attempt+1}/{max_retries}): {type(e).__name__}: {e}")
                time.sleep(retry_delay)
            else:
                print(f"Failed to fetch data for {ticker} after {max_retries} attempts: {type(e).__name__}: {e}")
    
    return None

@cache.memoize(timeout=60)
def download_forex_data(pair, interval):
    """
    Download forex data using yfinance with retry mechanism and cache the results
    Always uses date ranges instead of periods
    
    Args:
        pair (str): Forex pair symbol (e.g., 'EURUSD=X')
        interval (str): Time interval ('5m', '15m', '1h', '1d')
        
    Returns:
        pandas.DataFrame or None: DataFrame with price data or None if download failed
    """
   
    end_date = datetime.now()
    
    
    if interval == '5m' or interval == '15m':
        start_date = end_date - timedelta(days=1) 
    elif interval == '1h':
        start_date = end_date - timedelta(days=30)
    elif interval == '1d':
        start_date = end_date - timedelta(days=180) 
    else:
        start_date = end_date - timedelta(days=30) 
    
    # Format dates as strings
    start_str = start_date.strftime('%Y-%m-%d')
    end_str = end_date.strftime('%Y-%m-%d')
    
    try:
        data = try_yf_download(pair, interval=interval, start=start_str, end=end_str)
        
        if data is None or data.empty or 'Close' not in data.columns:
            print(f"No data found for {pair} ({interval} interval)")
            return None
            
        if data.index.tz is None:
            data.index = data.index.tz_localize('UTC').tz_convert('Asia/Kolkata')
        else:
            data.index = data.index.tz_convert('Asia/Kolkata')
            
        return data
        
    except Exception as e:
        print(f"Error in download_forex_data for {pair} ({interval} interval): {type(e).__name__}: {e}")
        return None

def clear_data_cache():
    """Clear all cached forex data"""
    cache.clear()
    return True

def get_forex_analysis(interval):
    """
    Get forex analysis for all pairs at a specific interval
    
    Args:
        interval (str): Time interval ('5m', '15m', '1h', '1d')
        
    Returns:
        tuple: (underbought_pairs, overbought_pairs)
    """
    underbought = []
    overbought = []
    
    for pair in FOREX_PAIRS:
        time.sleep(random.uniform(0.1, 0.3))
        
        data = download_forex_data(pair, interval)
        
        if data is not None and not data.empty and 'Close' in data.columns:
            data = calculate_rsi(data)
            
            if not data.empty and 'indication' in data.columns:
                last_indication = data['indication'].iloc[-1]
                
                if last_indication == 'Underbought':
                    underbought.append(pair.replace('=X', ''))
                elif last_indication == 'Overbought':
                    overbought.append(pair.replace('=X', ''))
    
    return underbought, overbought

def get_combined_analysis(intervals):
    """
    Get combined forex analysis across multiple intervals
    
    Args:
        intervals (list): List of time intervals to analyze
        
    Returns:
        dict: Dictionary with analysis for each interval and combined results
    """
    result = {}
    
    for interval in intervals:
        result[interval] = get_forex_analysis(interval)

    if intervals:
        combined_underbought = set(result[intervals[0]][0]) if result[intervals[0]] and len(result[intervals[0]]) >= 1 else set()
        combined_overbought = set(result[intervals[0]][1]) if result[intervals[0]] and len(result[intervals[0]]) >= 2 else set()
        
        for interval in intervals[1:]:
            interval_data = result.get(interval, ([], []))
            underbought = set(interval_data[0]) if interval_data and len(interval_data) >= 1 else set()
            overbought = set(interval_data[1]) if interval_data and len(interval_data) >= 2 else set()
            
            combined_underbought.intersection_update(underbought)
            combined_overbought.intersection_update(overbought)
            
        result['combined'] = (list(combined_underbought), list(combined_overbought))
    
    return result
