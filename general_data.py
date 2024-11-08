# general_data.py

from utils import get_json_data

def get_general_info(train_number, start_day):
    json_data = get_json_data(train_number, start_day)
    if not json_data:
        return {"error": "Failed to fetch or parse data"}

    try:
        pageProps = json_data['props']['pageProps']
        if 'ltsData' not in pageProps or not pageProps['ltsData'].get('success', False):
            message = pageProps.get('message', 'Train data not found.')
            return {"error": message}

        ltsData = pageProps['ltsData']
        general_info = {
            "success": ltsData.get("success", False),
            "user_id": ltsData.get("user_id", 0),
            "train_number": ltsData.get("train_number", ""),
            "train_name": ltsData.get("train_name", ""),
            "gps_unable": ltsData.get("gps_unable", False),
            "train_start_date": ltsData.get("train_start_date", ""),
            "notification_date": ltsData.get("notification_date", ""),
            "at_src_dstn": ltsData.get("at_src_dstn", False),
            "at_src": ltsData.get("at_src", False),
            "at_dstn": ltsData.get("at_dstn", False),
            "is_run_day": ltsData.get("is_run_day", False),
            "source": ltsData.get("source", ""),
            "destination": ltsData.get("destination", ""),
            "run_days": ltsData.get("run_days", ""),
            "journey_time": ltsData.get("journey_time", ""),
            "std": ltsData.get("std", ""),
            "data_from": ltsData.get("data_from", ""),
            "new_alert_id": ltsData.get("new_alert_id", 0),
            "new_alert_msg": ltsData.get("new_alert_msg", ""),
            "diverted_stations": ltsData.get("diverted_stations", None),
            "instance_alert": ltsData.get("instance_alert", 0),
            "related_alert": ltsData.get("related_alert", 0),
            "late_update": ltsData.get("late_update", False),
            "is_ry_eta": ltsData.get("is_ry_eta", False),
            "update_time": ltsData.get("update_time", ""),
            "distance_from_source": ltsData.get("distance_from_source", 0),
            "total_distance": ltsData.get("total_distance", 0),
            "avg_speed": ltsData.get("avg_speed", 0),
            "si_no": ltsData.get("si_no", 0),
            "current_station_code": ltsData.get("current_station_code", ""),
            "current_station_name": ltsData.get("current_station_name", ""),
            "status": ltsData.get("status", ""),
            "eta": ltsData.get("eta", ""),
            "etd": ltsData.get("etd", ""),
            "delay": ltsData.get("delay", 0),
            "ahead_distance": ltsData.get("ahead_distance", 0),
            "ahead_distance_text": ltsData.get("ahead_distance_text", ""),
            "status_as_of": ltsData.get("status_as_of", ""),
            "platform_number": ltsData.get("platform_number", 0),
            "cur_stn_sta": ltsData.get("cur_stn_sta", ""),
            "cur_stn_std": ltsData.get("cur_stn_std", ""),
            "stoppage_number": ltsData.get("stoppage_number", 0),
            "a_day": ltsData.get("a_day", 0),
            "status_as_of_min": ltsData.get("status_as_of_min", 0),
            "dfp_carousel": ltsData.get("dfp_carousel", {}),
            "spent_time": ltsData.get("spent_time", 0)
        }
        return general_info
    except Exception as e:
        return {"error": f"Error parsing general info: {e}"}
