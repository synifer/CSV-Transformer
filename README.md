**CSV-Transformer**

This Python script performs data conversion from an input CSV file and saves the result to a new CSV file and an Excel file in the same directory as the input file. 
The main task of the code is to take two lines from the input CSV file, where the first line contains the variable names and the second line contains the corresponding 
values, and convert them into a list of pairs (variable, value). This list is then written to new output files with appropriate formatting.

**Code Task**

1. **Reading and Validating the File:** The code checks whether the specified input file exists. If the file does not exist, an error message is displayed to the user.
2. **Processing the Input:**
   
- Reads all lines from the input CSV file.
- Checks whether the file contains at least two lines: one for the headers (variables) and one for the values.
- Creates a list of pairs (variable, value) from the lines read.
  
3. **Recording the results:** The obtained data is written to two output files:
   
- CSV file: Saved in the same format with two columns: "Variable" and "Value".
- Excel file: An Excel file with the same data format is created.
  
4. **Saving the files:** The output files are saved in the same directory as the input file, with names starting with the prefix "Output".

**How to run the script**

1. **Make sure Python is installed:** You must have Python installed on your computer. Download and install Python from the official Python website https:/www.python.org if you haven't already.
2. Install the required libraries: You will need the `openpyxl` library to work with Excel files. It can be installed by running the command:
   
pip install openpyxl

4. **Run the script:**
   
- Place the input CSV file in the specified directory or change the file path in the `input_file_path` variable.
- Run the script via the command line (CLI) or an integrated development environment (IDE), for example:
  
python csv_transformer.py

4. **Result:** After running the script, two new files will appear in the same directory:
- `Output_<input_file_name>.csv`
- `Output_<input_file_name>.xlsx`
- 
By following these instructions, you will be able to successfully use the script to process CSV files and save the results in the desired format.
