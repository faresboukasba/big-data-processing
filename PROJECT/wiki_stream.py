import json
import requests
import time
from collections import defaultdict

URL = "https://stream.wikimedia.org/v2/stream/recentchange"

ENTITIES = {
    "Inception": ["inception"],
    "The Dark Knight": ["dark knight"],
    "Christopher Nolan": ["christopher nolan", "nolan"],
    "Leonardo DiCaprio": ["leonardo dicaprio", "dicaprio"],
    "Comedy (genre)": ["comedy"]
}

EVENTS_FILE = "wiki_events.jsonl"
ALERTS_FILE = "wiki_alerts.jsonl"

ALERT_THRESHOLD = 3 
event_counts = defaultdict(int)

headers = {
    "User-Agent": "WikiStreamBot/1.0 (Educational Project)"
}

print("Starting Wikimedia stream listener...")

with requests.get(URL, stream=True, headers=headers) as response:
    print("Connected to Wikimedia stream.")

    for line in response.iter_lines():
        if not line or not line.startswith(b"data:"):
            continue

        event = json.loads(line.decode("utf-8")[5:])
        title = event.get("title", "").lower()

        for entity, keywords in ENTITIES.items():
            if any(keyword in title for keyword in keywords):
                event_counts[entity] += 1

                log_entry = {
                    "entity": entity,
                    "page_title": event.get("title"),
                    "timestamp": event.get("timestamp"),
                    "user": event.get("user"),
                    "event_type": event.get("type"),
                    "total_events_for_entity": event_counts[entity]
                }

                # Store metric event
                with open(EVENTS_FILE, "a", encoding="utf-8") as f:
                    f.write(json.dumps(log_entry) + "\n")

                print(f"Event for {entity} (count={event_counts[entity]})")

                # ALERT logic
                if event_counts[entity] == ALERT_THRESHOLD:
                    alert = {
                        "entity": entity,
                        "alert_type": "EDIT_THRESHOLD_REACHED",
                        "threshold": ALERT_THRESHOLD,
                        "timestamp": time.time()
                    }

                    with open(ALERTS_FILE, "a", encoding="utf-8") as a:
                        a.write(json.dumps(alert) + "\n")

                    print(f"ALERT triggered for {entity}")
