import os

# Directory structure
dirs = [
    "forex_rsi_screener/app",
    "forex_rsi_screener/app/data",
    "forex_rsi_screener/app/models",
    "forex_rsi_screener/app/static",
    "forex_rsi_screener/app/static/css",
    "forex_rsi_screener/app/static/js",
    "forex_rsi_screener/app/static/img",
    "forex_rsi_screener/app/templates",
    "forex_rsi_screener/app/templates/components",
]

# Create directories
for d in dirs:
    os.makedirs(d, exist_ok=True)

# Files to create with basic content
files = {
    "forex_rsi_screener/app/__init__.py": "# Flask app initialization\n",
    "forex_rsi_screener/app/routes.py": "# URL route handlers\n",
    "forex_rsi_screener/app/data/__init__.py": "# Data module initialization\n",
    "forex_rsi_screener/app/data/forex_data.py": "# Data fetching and processing\n",
    "forex_rsi_screener/app/models/__init__.py": "# Models module initialization\n",
    "forex_rsi_screener/app/models/indicators.py": "# Technical indicators calculation\n",
    "forex_rsi_screener/app/static/css/style.css": "/* Custom styles */\n",
    "forex_rsi_screener/app/static/js/main.js": "// JavaScript for interactivity\n",
    "forex_rsi_screener/app/templates/base.html": "<!-- Base template -->\n",
    "forex_rsi_screener/app/templates/index.html": "<!-- Main page -->\n",
    "forex_rsi_screener/app/templates/components/interval_card.html": "<!-- Interval card component -->\n",
    "forex_rsi_screener/config.py": "# Configuration settings\n",
    "forex_rsi_screener/run.py": "# Application entry point\n",
    "forex_rsi_screener/requirements.txt": "# Project dependencies\n"
}

# Create files with basic content
for file_path, content in files.items():
    with open(file_path, "w") as f:
        f.write(content)

print("Project structure created successfully!")
