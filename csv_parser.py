import csv
import sys

def parse_csv(input_file, output_file):
    # Step 1: Read the CSV File and Skip First Row
    with open(input_file, 'r', newline='') as input_csv:
        reader = csv.reader(input_csv)
        next(reader)  # Skip the first row with "sep=,"

        # Step 2: Process the Input Data
        mapped_data = []
        for row in reader:
            # Step 3: Map Data to Template (Selecting and Renaming Columns)
            mapped_row = {
                'Quantity': row[1],
                'Card Name': row[3],
                'Set Name': row[5],
                'Printing': row[8],
                'Collector Number': row[6]  # Renamed from 'Card Number'
            }
            mapped_data.append(mapped_row)

    # Step 4: Write to Output CSV
    with open(output_file, 'w', newline='') as output_csv:
        fieldnames = ['Quantity', 'Card Name', 'Set Name', 'Printing', 'Collector Number']
        writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(mapped_data)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python csv_parser.py <input_file> <output_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    parse_csv(input_file, output_file)


# # Example usage:
# python csv_parser.py input_data.csv output.csv
