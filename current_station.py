# current_station.py

from utils import get_json_data

def get_current_location_info(train_number, start_day):
    json_data = get_json_data(train_number, start_day)
    if not json_data:
        return {"error": "Failed to fetch or parse data"}

    try:
        ltsData = json_data['props']['pageProps'].get('ltsData', {})
        current_location_info = ltsData.get('current_location_info', [])
        if not current_location_info:
            return {"message": "Current location information is unavailable at the moment."}
        return current_location_info
    except Exception as e:
        return {"error": f"Error parsing current location info: {e}"}
