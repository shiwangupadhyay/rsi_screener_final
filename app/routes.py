# URL route handlers
from flask import Blueprint, render_template, request, jsonify
from config import TIME_INTERVALS
from app.data.forex_data import get_combined_analysis

# Create blueprint
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Render the main page"""
    return render_template('index.html', intervals=TIME_INTERVALS)

@main_bp.route('/analyze', methods=['POST'])
def analyze():
    """
    API endpoint to get forex analysis based on selected intervals
    
    Expected POST data:
    {
        "intervals": ["5m", "15m", ...]
    }
    """
    data = request.get_json()
    selected_intervals = data.get('intervals', [])
    
    # Validate intervals
    valid_intervals = [interval for interval in selected_intervals if interval in TIME_INTERVALS]
    
    if not valid_intervals:
        return jsonify({
            'success': False,
            'message': 'No valid intervals selected'
        }), 400
    
    # Get analysis results
    analysis = get_combined_analysis(valid_intervals)
    
    return jsonify({
        'success': True,
        'data': analysis
    })