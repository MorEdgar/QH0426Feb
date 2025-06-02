
# exporter.py
import json
import csv
from datetime import datetime
from process import prepare_export_data

class Exporter:
    # Class for exporting data in different formats

    def __init__(self, reviews):
        self.reviews = reviews
        self.export_data = prepare_export_data(reviews)
        # Create timestamp for unique filenames
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    def to_txt(self):
        # Export to text file
        filename = f"disneyland_analysis_{self.timestamp}.txt"

        with open(filename, 'w', encoding='utf-8') as f:
            f.write("DISNEYLAND PARKS ANALYSIS REPORT\n")
            f.write("=" * 50 + "\n")
            f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total records analyzed: {len(self.reviews)}\n\n")

            for park_data in self.export_data:
                f.write(f"Park: {park_data['Park']}\n")
                f.write(f"  Total Reviews: {park_data['Total_Reviews']}\n")
                f.write(f"  Positive Reviews (4-5 stars): {park_data['Positive_Reviews']}\n")
                f.write(f"  Average Rating: {park_data['Average_Rating']}/5\n")
                f.write(f"  Countries Reviewed From: {park_data['Unique_Countries']}\n")
                f.write("-" * 30 + "\n")

        return filename

    def to_csv(self):
        # Export to CSV file
        filename = f"disneyland_analysis_{self.timestamp}.csv"

        with open(filename, 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['Park', 'Total_Reviews', 'Positive_Reviews',
                         'Average_Rating', 'Unique_Countries']
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()
            for park_data in self.export_data:
                writer.writerow(park_data)

        return filename

    def to_json(self):
        # Export to JSON file
        filename = f"disneyland_analysis_{self.timestamp}.json"

        export_structure = {
            "metadata": {
                "generated_on": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "total_records": len(self.reviews),
                "parks_analyzed": len(self.export_data)
            },
            "park_analysis": self.export_data
        }

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(export_structure, f, indent=2, ensure_ascii=False)

        return filename