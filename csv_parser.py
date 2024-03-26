import csv
import sys

def parse_csv(input_file, output_file):
    # Step 1: Reading the CSV File and Skip First Row
    with open(input_file, 'r', newline='') as input_csv:
        reader = csv.reader(input_csv)
        next(reader)  # Skiping the first row with redundant "sep=,"

        # Step 2: Processing the Input Data
        mapped_data = []
        for row in reader:
            # Step 3: Mapping Data to Template (Selecting and Renaming Columns)
            mapped_row = {
                'Quantity': row[1],
                'Card Name': row[3],
                'Set Name': row[5],
                'Foil/Variant': row[8],     # Renamed from 'Printing' to 'Foil/Variant'
                'Card Number': row[6]       # Renamed from 'Collector Number'
            }
            mapped_data.append(mapped_row)

    # Removing the header row from mapped_data
    mapped_data.pop(0)

    # Step 4: Writing to Output CSV
    with open(output_file, 'w', newline='') as output_csv:
        fieldnames = ['Quantity', 'Card Name', 'Set Name', 'Foil/Variant', 'Card Number']  # Updated fieldnames
        writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
        
        # Writing the header with updated column names
        writer.writeheader()
        
        # Writing the data
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
