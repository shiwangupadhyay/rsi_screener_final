# Technical indicators calculation
import pandas as pd
import ta

def calculate_rsi(df, window=14):
    """
    Calculate RSI indicator and determine market condition (Overbought/Underbought/Neutral)
    
    Args:
        df (pandas.DataFrame): DataFrame with price data including 'Close' column
        window (int): RSI window period (default: 14)
        
    Returns:
        pandas.DataFrame: Original DataFrame with added RSI and indication columns
    """
    if df is None or df.empty or 'Close' not in df.columns:
        return df

    # Calculate RSI using the TA library
    close_prices = df['Close'].squeeze()
    rsi_series = ta.momentum.RSIIndicator(close_prices, window=window).rsi()
    df['RSI'] = rsi_series.squeeze()
    
    # Drop NaN values
    df.dropna(inplace=True)
    
    # Determine market condition based on RSI values
    df['indication'] = ''
    df.loc[df['RSI'] > 70, 'indication'] = 'Overbought'
    df.loc[df['RSI'] < 30, 'indication'] = 'Underbought'
    df.loc[(df['RSI'] >= 30) & (df['RSI'] <= 70), 'indication'] = 'Neutral'
    
    return df