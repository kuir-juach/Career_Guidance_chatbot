import json
import csv

def convert_json_to_csv():
    # Read JSON file
    with open('career_dataset.json', 'r') as f:
        data = json.load(f)
    
    # Write to CSV
    with open('career_dataset.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['input', 'output'])  # Header
        
        for item in data:
            writer.writerow([item['input'], item['output']])
    
    print(f"Converted {len(data)} records from JSON to CSV")

if __name__ == "__main__":
    convert_json_to_csv()