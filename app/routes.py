# Routes for the Forex RSI Screener
from flask import Blueprint, render_template, jsonify, request
from app.data.forex_data import get_combined_analysis, clear_data_cache
from config import INTERVALS
from datetime import datetime

# Create Blueprint
main = Blueprint('main', __name__)

@main.route('/')
def index():
    """Render the main page"""
    return render_template('index.html', intervals=INTERVALS)

@main.route('/analyze', methods=['POST'])
def analyze():
    """Analyze forex data across selected intervals"""
    try:
        # Get JSON data from request
        data = request.get_json()
        
        if not data or 'intervals' not in data:
            return jsonify({
                'success': False,
                'message': 'No intervals provided'
            })
            
        intervals = data['intervals']
        
        # Force refresh flag (optional)
        force_refresh = data.get('force_refresh', False)
        
        # Clear cache if force refresh is requested
        if force_refresh:
            clear_data_cache()
        
        # Get combined analysis
        result = get_combined_analysis(intervals)
        
        # Check if result contains valid data
        if not result:
            return jsonify({
                'success': False,
                'message': 'No data available for the selected intervals'
            })
            
        # Make sure all entries in result are valid
        for interval in intervals:
            if interval not in result or not result[interval] or len(result[interval]) < 2:
                # If missing or invalid data, provide empty lists
                result[interval] = ([], [])
                
        # Make sure combined results exist
        if 'combined' not in result or not result['combined'] or len(result['combined']) < 2:
            result['combined'] = ([], [])
        
        # Get current time for timestamp
        now = datetime.now()
        
        return jsonify({
            'success': True,
            'data': result,
            'timestamp': now.strftime('%Y-%m-%d %H:%M:%S')
        })
        
    except Exception as e:
        import traceback
        print(f"Error in analyze route: {str(e)}")
        print(traceback.format_exc())
        return jsonify({
            'success': False,
            'message': f'Error: {str(e)}'
        })

@main.route('/clear-cache', methods=['POST'])
def clear_cache():
    """Clear the cache to force data refresh"""
    try:
        clear_data_cache()
        return jsonify({
            'success': True,
            'message': 'Cache cleared successfully'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error clearing cache: {str(e)}'
        })