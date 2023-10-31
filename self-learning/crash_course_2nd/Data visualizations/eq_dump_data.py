import json

# Explore the structure of the data
filename = 'data/eq_data_30_day.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_30_day_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)