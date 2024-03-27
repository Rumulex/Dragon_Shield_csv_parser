import csv
import os
from datetime import datetime
import shutil

def parse_csv_files(input_dir, output_dir):
    # Initialize an empty list to store data
    combined_data = []

    # Step 1: Processing each CSV file from the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".csv"):
            input_file = os.path.join(input_dir, filename)
            with open(input_file, 'r', newline='') as input_csv:
                reader = csv.reader(input_csv)
                # Skipping the first two rows of the files (one with "sep=," and one with headers)
                next(reader)
                next(reader)
                
                # Step 2: Processing the Input Data
                for row in reader:
                    # Step 3: Mapping Data to Template (Selecting and Renaming Columns)
                    mapped_row = {
                        'Quantity': row[1],           # Quantity column
                        'Card Name': row[3],          # Card Name column
                        'Set Name': row[5],           # Set Name column
                        'Foil/Variant': row[8],           # Print type column
                        'Card Number': row[6]         # Card Number column
                    }
                    combined_data.append(mapped_row)

    # Step 4: Writing to Output CSV
    output_file = os.path.join(output_dir, f"output_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv")
    with open(output_file, 'w', newline='') as output_csv:
        fieldnames = ['Quantity', 'Card Name', 'Set Name', 'Foil/Variant', 'Card Number']  # Updated fieldnames
        writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
        
        # Writing the header with updated column names
        writer.writeheader()
        
        # Writing the combined data
        writer.writerows(combined_data)

    # Step 5: Creating a timestamped folder and moving processed files
    parsed_dir = os.path.join(os.getcwd(), "Parsed")
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    timestamped_folder = os.path.join(parsed_dir, f"Executed_{timestamp}")
    if not os.path.exists(timestamped_folder):
        os.makedirs(timestamped_folder)  # Creating the timestamped folder if it doesn't exist
    for filename in os.listdir(input_dir):
        if filename.endswith(".csv"):
            file_to_move = os.path.join(input_dir, filename)
            shutil.move(file_to_move, timestamped_folder)

if __name__ == "__main__":
    input_dir = "Input"    # Default input directory
    output_dir = "Output"  # Output directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Creating the output directory if it doesn't exist
    parse_csv_files(input_dir, output_dir)
