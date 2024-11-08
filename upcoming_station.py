# upcoming_station.py

from utils import get_json_data

def get_upcoming_stations(train_number, start_day):
    json_data = get_json_data(train_number, start_day)
    if not json_data:
        return {"error": "Failed to fetch or parse data"}

    try:
        ltsData = json_data['props']['pageProps'].get('ltsData', {})
        upcoming_stations = ltsData.get('upcoming_stations', [])
        if not upcoming_stations:
            return {"message": "No upcoming stations found. The train may have completed its journey or data is unavailable."}

        all_upcoming_stations = []

        for station in upcoming_stations:
            # Add the main station if it exists
            if station.get('station_code'):
                station_data = {
                    "si_no": station.get('si_no'),
                    "station_code": station.get('station_code'),
                    "station_name": station.get('station_name'),
                    "is_diverted_station": station.get('is_diverted_station', False),
                    "distance_from_source": station.get('distance_from_source'),
                    "distance_from_current_station": station.get('distance_from_current_station'),
                    "distance_from_current_station_txt": station.get('distance_from_current_station_txt'),
                    "sta": station.get('sta'),
                    "std": station.get('std'),
                    "eta": station.get('eta'),
                    "etd": station.get('etd'),
                    "halt": station.get('halt'),
                    "a_day": station.get('a_day'),
                    "arrival_delay": station.get('arrival_delay'),
                    "platform_number": station.get('platform_number'),
                    "station_lat": station.get('station_lat'),
                    "station_lng": station.get('station_lng'),
                    "stoppage_number": station.get('stoppage_number'),
                    "day": station.get('day'),
                    "eta_a_min": station.get('eta_a_min'),
                    "food_available": station.get('food_available'),
                    "non_stops": []
                }

                # Add non-stop stations if any
                non_stops = station.get('non_stops', [])
                for non_stop in non_stops:
                    non_stop_data = {
                        "si_no": non_stop.get('si_no'),
                        "station_code": non_stop.get('station_code'),
                        "station_name": non_stop.get('station_name'),
                        "is_diverted_station": non_stop.get('is_diverted_station', False),
                        "distance_from_source": non_stop.get('distance_from_source'),
                        "sta": non_stop.get('sta'),
                        "std": non_stop.get('std'),
                        "non_stops": []
                    }
                    station_data["non_stops"].append(non_stop_data)

                all_upcoming_stations.append(station_data)
        return all_upcoming_stations
    except Exception as e:
        return {"error": f"Error parsing upcoming stations: {e}"}
