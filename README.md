# Dragon Shield MTG App Exported CSV Parser

Dragon Shield MTG app is a mobile app used for managing a collectible card game collection. While I primarily use this app to scan Magic: The Gathering (MTG) cards, I also maintain my collection on archidekt.com. However, the Dragon Shield template provided by Archidekt did not work properly with the exported CSV files.

## Objective

This simple script parses the CSV files exported from the Dragon Shield app into a format suitable for Archidekt. Additionally, it manages the processed files by moving them to a separate "Parsed" folder to avoid duplication.

## Features

- Parses .csv files from the Dragon Shield app.
- Creates a single output file with the parsed data.
- Manages processed files by moving them to a "Parsed" folder.

## Usage

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Place the CSV files exported from the Dragon Shield app in the "Input" folder.
4. Run the script using the command `python csv_parser.py`.
5. The parsed output file will be generated in the "Output" folder, and processed files will be moved to the "Parsed" folder.

## Folder Structure

- Input
  - Destination for CSV files exported from the Dragon Shield app.
- Output
  - Contains the parsed output file.
- Parsed
  - Contains processed files moved from the "Input" folder.
 
## Example

- You can find files that I've run the script on in Parsed folder and the result in Output folder
