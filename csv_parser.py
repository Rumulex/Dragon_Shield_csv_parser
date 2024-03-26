import csv
import os
from datetime import datetime

def parse_csv_files(input_dir, output_dir):
    # Initialize an empty list to store combined data
    combined_data = []

    # Step 1: Process each CSV file in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".csv"):
            input_file = os.path.join(input_dir, filename)
            with open(input_file, 'r', newline='') as input_csv:
                reader = csv.reader(input_csv)
                # Skip the first two rows (one with "sep=," and one with headers)
                next(reader)
                next(reader)
                
                # Step 2: Process the Input Data
                for row in reader:
                    # Step 3: Map Data to Template (Selecting and Renaming Columns)
                    mapped_row = {
                        'Quantity': row[1],        # Adjusted index from 0 to 1
                        'Card Name': row[2],       # Adjusted index from 1 to 2
                        'Set Name': row[3],        # Adjusted index from 2 to 3
                        'Foil/Variant': row[4],    # Adjusted index from 7 to 4
                        'Card Number': row[5]      # Adjusted index from 6 to 5
                    }
                    combined_data.append(mapped_row)

    # Step 4: Write to Output CSV
    output_file = os.path.join(output_dir, f"output_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv")
    with open(output_file, 'w', newline='') as output_csv:
        fieldnames = ['Quantity', 'Card Name', 'Set Name', 'Foil/Variant', 'Card Number']  # Updated fieldnames
        writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
        
        # Write the header with updated column names
        writer.writeheader()
        
        # Write the combined data
        writer.writerows(combined_data)

if __name__ == "__main__":
    input_dir = "Input"    # Default input directory
    output_dir = "Output"  # Output directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Create the output directory if it doesn't exist
    parse_csv_files(input_dir, output_dir)
