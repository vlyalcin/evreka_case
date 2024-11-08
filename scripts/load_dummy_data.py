import requests
import random
import datetime
import json
import sys

"""
This script performs a load test by sending a specified number of HTTP POST requests (default: 1000).
Each request sends randomly generated device data in JSON format to a given URL.
The script outputs status information every 100 requests and displays a final summary after all requests are completed.

Functions:
- generate_random_data(): Generates random device data (device_id, timestamp, location, and speed).
- run_load_dummy_data(): Sends a specified number of HTTP POST requests with random data generated by generate_random_data.

Usage:
    python load_dummy_data.py <REQUEST_COUNT>

Parameters:
- REQUEST_COUNT (optional): The total number of requests to send. Defaults to 1000 requests.
  For example, `python load_dummy_data.py 500` sends 500 requests.

Output:
- Prints a status message every 100 requests.
- Displays the total number of completed requests and the status code of the last request upon completion.
"""

REQUEST_COUNT = int(sys.argv[1]) if len(sys.argv) > 1 else 1000  # Default: 1000 requests
URL = "http://localhost:8000/data/"

def generate_random_timestamp():
    """Generate a random timestamp within the last day."""
    now = datetime.datetime.now(datetime.timezone.utc)
    one_day_in_seconds = 24 * 60 * 60  # 1 day in seconds
    random_seconds = random.randint(0, one_day_in_seconds)
    random_timestamp = now - datetime.timedelta(seconds=random_seconds)
    return random_timestamp.isoformat()

def generate_random_data():
    """Generate random device data, including a timestamp within the last day."""
    device_id = f"device{random.randint(0, 100)}"
    timestamp = generate_random_timestamp()
    lat = round(40.5 + random.uniform(0, 0.1), 6)
    lon = round(-74.0 - random.uniform(0, 0.1), 6)
    speed = round(50 + random.uniform(0, 30), 2)

    return {
        "device_id": device_id,
        "timestamp": timestamp,
        "location": {"lat": lat, "lon": lon},
        "speed": speed
    }

def run_load_dummy_data():
    for i in range(REQUEST_COUNT):
        data = generate_random_data()
        headers = {"Content-Type": "application/json"}
        response = requests.post(URL, headers=headers, data=json.dumps(data))

        if (i + 1) % 100 == 0 or i == REQUEST_COUNT - 1:
            print(f"{i+1}/{REQUEST_COUNT} requests completed - Last Status Code: {response.status_code}")

if __name__ == "__main__":
    run_load_dummy_data()