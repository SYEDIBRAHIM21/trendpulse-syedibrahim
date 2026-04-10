import requests
import time
import json
from datetime import datetime
import os

# API URLs
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

headers = {"User-Agent": "TrendPulse/1.0"}

# Categories
categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

def get_category(title):
    title = title.lower()
    for category, keywords in categories.items():
        for word in keywords:
            if word in title:
                return category
    return "other"

def fetch_data():
    try:
        res = requests.get(TOP_STORIES_URL, headers=headers)
        story_ids = res.json()[:100]  # first 100 stories
    except:
        print("Error fetching story IDs")
        return []

    stories = []

    for story_id in story_ids:
        try:
            res = requests.get(ITEM_URL.format(story_id), headers=headers)
            item = res.json()

            if item and "title" in item:
                story = {
                    "post_id": item.get("id"),
                    "title": item.get("title"),
                    "category": get_category(item.get("title")),
                    "score": item.get("score", 0),
                    "num_comments": item.get("descendants", 0),
                    "author": item.get("by"),
                    "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                stories.append(story)

        except:
            continue

    return stories

def save_json(data):
    if not os.path.exists("data"):
        os.makedirs("data")

    filename = "data/trends_" + datetime.now().strftime("%Y%m%d") + ".json"

    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Collected {len(data)} stories. Saved to {filename}")

# Run
data = fetch_data()
save_json(data)
