"""Datetime module for ensuring fresh temp values are stored"""
from datetime import datetime, timedelta, timezone

import os

import httpx

from fastapi import FastAPI

VERSION = "v0.1.0"

SENSEBOX_IDS = ["5eba5fbad46fb8001b799786", "5c21ff8f919bf8001adf2488", "5ade1acf223bd80019a1011c"]

SENSEBOX_ENV_IDS = os.getenv("SENSEBOX_ENV_IDS")

if SENSEBOX_ENV_IDS:
    SENSEBOX_IDS = SENSEBOX_ENV_IDS.split(",")

def box_temps():
    """Query opensensemap for temps and calculate average of values taken within the hour"""
    cutoff = datetime.now(timezone.utc) - timedelta(hours=1)
    temps = []
    for box_id in SENSEBOX_IDS:
        # setting variable using box_id in url, timeout 15 to avoid failures from slow api calls
        response = httpx.get(f"https://api.opensensemap.org/boxes/{box_id}?format=json", timeout=15)
        # parse json response into a dictionary
        data = response.json()
        for sensor in data["sensors"]:
            # conditional statement to isolate only temperature sensors via title match
            if sensor["title"] == "Temperatur":
                measured_at = datetime.fromisoformat(sensor["lastMeasurement"]["createdAt"])
                # if temp reading was taken later than an hour ago add it to the list
                if measured_at > cutoff:
                    temps.append(float(sensor["lastMeasurement"]["value"]))
    # last conditional statement ensuring list is not empty
    if temps:
        # if list is not empty calculate avg with sum and len functions
        temp_avg = sum(temps) / len(temps)
        # return the value of the average
        return temp_avg
    # avoids linting errors for inconsistent return statements
    return None

app = FastAPI()

@app.get("/version")
async def app_version():
    """Return app version"""
    return {"version": VERSION}

@app.get("/temperature")
def app_temperature():
    """Return average temperature from all senseboxes"""
    return {"temperature": box_temps()}
