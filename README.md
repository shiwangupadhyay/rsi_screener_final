# Forex RSI Screener

A modern web application that screens forex pairs for overbought and underbought conditions using the Relative Strength Index (RSI) technical indicator. This tool helps traders identify potential trading opportunities across multiple timeframes.

![Forex RSI Screener Screenshot](https://via.placeholder.com/800x450.png?text=Forex+RSI+Screener)

## Features

- **Multi-timeframe Analysis**: Screen forex pairs across multiple timeframes (5m, 15m, 1h, 1d)
- **Combined Signals**: Find pairs that meet criteria across multiple timeframes
- **Real-time Data**: Uses yfinance to fetch up-to-date forex data
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Modern UI**: Clean, intuitive interface with Bootstrap 5
- **Efficient Caching**: Minimizes API calls with smart caching

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Data Processing**: Pandas, TA-Lib
- **Data Source**: Yahoo Finance API (via yfinance)
- **Caching**: Flask-Caching
- **Deployment**: Docker, Heroku, AWS compatible

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/forex-rsi-screener.git
   cd forex-rsi-screener
   ```

2. Create and activate a virtual environment:
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python run.py
   ```

5. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## Usage

1. Select the timeframes you want to analyze by checking the corresponding checkboxes
2. The application will display overbought and underbought forex pairs for each selected timeframe
3. If multiple timeframes are selected, a "Combined Results" section will show pairs that meet the criteria across all selected timeframes

## Project Structure

```
forex_rsi_screener/
│
├── app/
│   ├── __init__.py           # Flask app initialization
│   ├── routes.py             # URL route handlers
│   ├── data/
│   │   ├── __init__.py
│   │   └── forex_data.py     # Data fetching and processing
│   ├── models/
│   │   ├── __init__.py
│   │   └── indicators.py     # Technical indicators calculation
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css     # Custom styles
│   │   ├── js/
│   │   │   └── main.js       # JavaScript for interactivity
│   │   └── img/              # Images directory
│   └── templates/
│       ├── base.html         # Base template
│       ├── index.html        # Main page
│       └── components/       # Reusable template components
│           └── interval_card.html
│
├── config.py                 # Configuration settings
├── run.py                    # Application entry point
└── requirements.txt          # Project dependencies
```

## Deployment

For detailed deployment instructions, refer to the [Deployment Guide](DEPLOYMENT.md).

### Docker Deployment

```bash
# Build the Docker image
docker build -t forex-rsi-screener .

# Run the container
docker run -p 8080:8080 forex-rsi-screener
```

### Heroku Deployment

```bash
# Login to Heroku
heroku login

# Create a Heroku app
heroku create your-app-name

# Deploy the application
git push heroku main

# Open the application
heroku open
```

## Customization

### Adding More Forex Pairs

Edit the `FOREX_PAIRS` list in `config.py` to add or remove forex pairs.

### Modifying RSI Parameters

The default RSI period is 14. You can change this by modifying the `window` parameter in `app/models/indicators.py`.

### Changing Overbought/Underbought Thresholds

The default thresholds are 70 for overbought and 30 for underbought. You can modify these values in `app/models/indicators.py`.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [yfinance](https://github.com/ranaroussi/yfinance) for providing free access to market data
- [TA-Lib](https://github.com/mrjbq7/ta-lib) for technical analysis indicators
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [Bootstrap](https://getbootstrap.com/) for the UI components