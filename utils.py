# utils.py

import requests
from bs4 import BeautifulSoup
import json
import random
import logging

def get_json_data(train_number, start_day):
    url = f"https://www.railyatri.in/live-train-status/{train_number}?start_day={start_day}"
    user_agents = [
        # List of user agents to rotate
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 OPR/73.0.3856.344',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) Safari/537.36 Edge/18.18363',
        # Add more user agents if needed
    ]
    headers = {
        'User-Agent': random.choice(user_agents),
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            logging.error(f"Failed to fetch data: Status code {response.status_code}")
            return None
        soup = BeautifulSoup(response.content, 'html.parser')
        script_tag = soup.find('script', id='__NEXT_DATA__', type='application/json')
        if not script_tag:
            logging.error("Failed to find the JSON data script tag.")
            return None
        json_data = json.loads(script_tag.string)
        return json_data
    except requests.exceptions.RequestException as e:
        logging.error(f"Request exception: {e}")
        return None
    except json.JSONDecodeError as e:
        logging.error(f"JSON decode error: {e}")
        return None
