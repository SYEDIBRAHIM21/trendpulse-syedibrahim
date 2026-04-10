import json
import csv
import os

# Find latest JSON file
folder = "data"
files = [f for f in os.listdir(folder) if f.endswith(".json")]
files.sort()

latest_file = os.path.join(folder, files[-1])

# Read JSON
with open(latest_file, "r") as f:
    data = json.load(f)

# Clean + write CSV
csv_file = "cleaned_data.csv"

with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    
    # Header
    writer.writerow(["post_id", "title", "category", "score", "num_comments", "author", "collected_at"])
    
    for item in data:
        writer.writerow([
            item.get("post_id"),
            item.get("title"),
            item.get("category"),
            item.get("score"),
            item.get("num_comments"),
            item.get("author"),
            item.get("collected_at")
        ])

print("CSV file created:", csv_file)
