# previous_station.py

from utils import get_json_data

def get_previous_stations(train_number, start_day):
    json_data = get_json_data(train_number, start_day)
    if not json_data:
        return {"error": "Failed to fetch or parse data"}

    try:
        ltsData = json_data['props']['pageProps'].get('ltsData', {})
        previous_stations = ltsData.get('previous_stations', [])
        if not previous_stations:
            return {"message": "No previous stations found. The train may not have started yet."}

        all_previous_stations = []

        for station in previous_stations:
            # Add the main station
            station_data = {
                "si_no": station.get('si_no'),
                "station_code": station.get('station_code'),
                "station_name": station.get('station_name'),
                "is_diverted_station": station.get('is_diverted_station', False),
                "distance_from_source": station.get('distance_from_source'),
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

            all_previous_stations.append(station_data)

        return all_previous_stations
    except Exception as e:
        return {"error": f"Error parsing previous stations: {e}"}
