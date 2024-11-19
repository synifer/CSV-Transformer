import csv
from openpyxl import Workbook
import os

# Function to read and transform incoming CSV
def transform_csv(input_file_path):
    try:
        # Check for file existence
        if not os.path.exists(input_file_path):
            raise FileNotFoundError(f"File '{input_file_path}' not found.")

        with open(input_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            rows = list(reader)  # Read all the lines

            if len(rows) < 2:  # Check if there are two lines exist
                raise ValueError("The file must contain at least two lines: headers and values.")

            variables = rows[0]  # First line
            values = rows[1]     # Second line

            # Convert to a list of pairs (variable, value)
            result = list(zip(variables, values))
            return result

    except FileNotFoundError as e:
        print(f"Error: {e}")
        return []
    except ValueError as e:
        print(f"Error: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

# Function to write data to a new CSV file
def write_to_csv(data, output_file_path):
    try:
        with open(output_file_path, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Variable', 'Value'])  # Column headings
            writer.writerows(data)  # Write pairs to a file
    except Exception as e:
        print(f"Error while writing to CSV: {e}")

# Function to write data to a new Excel file
def write_to_excel(data, output_file_path):
    try:
        workbook = Workbook()
        sheet = workbook.active

        # Adding column headings
        sheet.append(['Variable', 'Value'])

        # Write pairs to a file
        for variable, value in data:
            sheet.append([variable, value])

        # Save the file
        workbook.save(output_file_path)
    except Exception as e:
        print(f"Error while writing to Excel: {e}")

# Main code for handling files
if __name__ == "__main__":
    input_file_path = r'C:\Users\user-name\Documents\CSV\Simple-Template.csv'

    # Checking if the input file exists
    if not os.path.isfile(input_file_path):
        print(f"File '{input_file_path}' does not exist. Check the file path.")
    else:
        # Generate the name of the output file in the same directory
        input_directory = os.path.dirname(input_file_path)  # Input file directory
        input_filename = os.path.basename(input_file_path)  # Output file directory
        output_csv_path = os.path.join(input_directory, f"Output_{input_filename}")
        #output_excel_path = os.path.splitext(output_csv_path)[0] + '.xlsx'  # Change the extension to на .xlsx

        # Processing the input file
        transformed_data = transform_csv(input_file_path)

        if transformed_data:
            # Write data to output files if transformation is successful
            write_to_csv(transformed_data, output_csv_path)
            #write_to_excel(transformed_data, output_excel_path)
            print(f"Data successfully written to file: {output_csv_path}")
            #print(f"Data successfully written to files: {output_csv_path} та {output_excel_path}")
        else:
            print("Processing failed due to errors.")
