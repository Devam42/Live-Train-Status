# app.py

from flask import Flask, jsonify, request
from flask_cors import CORS
from general_data import get_general_info
from upcoming_station import get_upcoming_stations
from previous_station import get_previous_stations
from current_station import get_current_location_info
import logging

app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/train_info', methods=['GET'])
def train_info():
    try:
        train_number = request.args.get('train_number')
        start_day = request.args.get('start_day')

        if not train_number or not start_day:
            return jsonify({"error": "Please provide both train_number and start_day"}), 400

        # Get the different types of data
        general_data = get_general_info(train_number, start_day)
        if "error" in general_data:
            logging.error(f"General data error: {general_data['error']}")
            return jsonify({"error": general_data["error"]}), 404

        upcoming_stations = get_upcoming_stations(train_number, start_day)
        if "error" in upcoming_stations:
            logging.error(f"Upcoming stations error: {upcoming_stations['error']}")
            return jsonify({"error": upcoming_stations["error"]}), 500

        previous_stations = get_previous_stations(train_number, start_day)
        if "error" in previous_stations:
            logging.error(f"Previous stations error: {previous_stations['error']}")
            return jsonify({"error": previous_stations["error"]}), 500

        current_location_info = get_current_location_info(train_number, start_day)
        if "error" in current_location_info:
            logging.error(f"Current location info error: {current_location_info['error']}")
            return jsonify({"error": current_location_info["error"]}), 500

        # Final result combining all sections
        result = general_data.copy()
        result["upcoming_stations"] = upcoming_stations if isinstance(upcoming_stations, list) else []
        result["previous_stations"] = previous_stations if isinstance(previous_stations, list) else []
        result["current_location_info"] = current_location_info if isinstance(current_location_info, list) else []
        
        return jsonify(result)
    except Exception as e:
        logging.exception(f"Unhandled exception: {e}")
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
