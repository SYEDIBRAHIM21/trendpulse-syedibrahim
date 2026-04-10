import csv

file = "cleaned_data.csv"

total = 0
category_count = {}

with open(file, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        total += 1
        
        cat = row["category"]
        if cat in category_count:
            category_count[cat] += 1
        else:
            category_count[cat] = 1

print("Total stories:", total)
print("Stories per category:")

for k, v in category_count.items():
    print(k, ":", v)
