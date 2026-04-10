import csv
import matplotlib.pyplot as plt

file = "cleaned_data.csv"

category_count = {}

with open(file, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        cat = row["category"]
        if cat in category_count:
            category_count[cat] += 1
        else:
            category_count[cat] = 1

# Prepare data
categories = list(category_count.keys())
values = list(category_count.values())

# Plot
plt.bar(categories, values)
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Trending Stories by Category")

plt.show()
