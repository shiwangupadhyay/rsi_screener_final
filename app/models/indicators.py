import pandas as pd
from ta.momentum import RSIIndicator
from config import RSI_PERIOD, RSI_OVERBOUGHT, RSI_UNDERBOUGHT

def calculate_rsi(data, period=None, overbought=None, underbought=None):
    """
    Calculate RSI (Relative Strength Index) using ta library.
    """
    period = period or RSI_PERIOD
    overbought = overbought or RSI_OVERBOUGHT
    underbought = underbought or RSI_UNDERBOUGHT

    try:
        df = data.copy()

        if 'Close' not in df.columns:
            print("Error: Close price column not found in data")
            return pd.DataFrame()

        close_series = df['Close']
        if isinstance(close_series, pd.DataFrame):
            close_series = close_series.squeeze()

        rsi_indicator = RSIIndicator(close=close_series, window=period)
        df['RSI'] = rsi_indicator.rsi()

        df['indication'] = 'Normal'
        df.loc[df['RSI'] > overbought, 'indication'] = 'Overbought'
        df.loc[df['RSI'] < underbought, 'indication'] = 'Underbought'

        return df

    except Exception as e:
        print(f"Error calculating RSI: {type(e).__name__}: {e}")
        return pd.DataFrame()
