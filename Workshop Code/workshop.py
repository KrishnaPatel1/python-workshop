# Library which helps to read excel spreadsheets
import xlrd
# Library which allows writing to docx format
from docx import Document
# Library to help find current folder
import os
# Library to help search for specific words within files
import re
# Library to retrieve current date
from datetime import date
# Library to read and modify contents
import fileinput
# Library to copy file contents
import shutil


# Function to find text and replace
def find_and_replace_text(stringInFile, string_to_replace_with, name_of_file):
  with fileinput.FileInput(name_of_file, inplace=True) as file:
    for line in file:
      print(line.replace(stringInFile, string_to_replace_with), end='')

# Function to find values inside the dictionary provided, and replace
def find_value_in_dictionaries_and_replace(template_dict, information_dict, name_of_file):
  for first_key in template_dict:
    for second_key in information_dict:
      if first_key == second_key:
        find_and_replace_text(template_dict[first_key], information_dict[second_key], name_of_file)

# Function to find values, and replace
def find_values_and_replace(dict_string, string, name_of_file):
  find_and_replace_text(dict_string, string, name_of_file)

# Find and store excel file
excel_file = xlrd.open_workbook('cover_letters.xlsx', on_demand = True)
# Choose which sheet to use inside your excel file
worksheet = excel_file.sheet_by_name('Sheet1')

# Set total amount of rows and columns
rows = worksheet.nrows
columns = worksheet.ncols

# User input for PDF or Word document
user_wants_pfd = input("Press 1 for PDF, or 0 for Word docx")

# Step 1
# Create a dictionary linking your keys, to the values inside the template file
boiler_plate_text_to_replace = {
  
}

# Step 2  
# Set personal details to add to cover letter
current_month = date.today().strftime("%B")
current_date = current_month + " " + str(date.today().day) + ", " + str(date.today().year)

# Set information in a dictionary with above information
cover_letter_information_to_add = {
  
}

# Values with no variables to use in loops
key_to_add = None
string_to_replace_with = None
file_name = None

# Define start, end for the range 
# First for loop with range of data based on rows
# Second for loop with range of data based on columns

  # Traverse through all the columns of data in a single row of the excel sheet
  # Note: Use if and elif statements
    # Company name 
      file_name = None
      # Set keyToAdd with key from object you want to add

      # Set stringToReplaceWith from worksheet cell value

      # Copy from template text file and name it based on company name
      file_name = os.getcwd() + "/exports/" + worksheet.cell(row, column).value + ".txt" 
      shutil.copyfile("cover-letter-template.txt", file_name)
      
      # Pass variables in function to find the value and replace with new value
      find_value_in_dictionaries_and_replace(
        boiler_plate_text_to_replace, 
        cover_letter_information_to_add, 
        file_name)
      
    # First name
      # Set keyToAdd with key from object you want to add

      # Set stringToReplaceWith from worksheet cell value

    # Last name
      # Set keyToAdd with key from object you want to add

      # Set stringToReplaceWith from worksheet cell value

    # Gender 
      # Set keyToAdd with key from object you want to add

      if worksheet.cell(row, column).value == "Male":
        # Set stringToReplaceWith from worksheet cell value

      else:
        # Set stringToReplaceWith from worksheet cell value

    # Position Name  
      # Set keyToAdd with key from object you want to add

      # Set stringToReplaceWith from worksheet cell value

    # Company Address
      # Set keyToAdd with key from object you want to add

      # Set stringToReplaceWith from worksheet cell value

    
    # Replace remaining template values with excel sheet values
    if key_to_add != None:
      find_values_and_replace(
        boiler_plate_text_to_replace[key_to_add], 
        string_to_replace_with, 
        file_name)

    # Reset variables
    key_to_add = None
    string_to_replace_with = None

# Convert to PDF or Word format
direct = os.listdir(os.getcwd() + "/exports/")
path_to_pdf_script = "convert-pdf/txt2pdf.py"

for i in direct:
    if not i.endswith(".txt"):
        continue

    name_of_file = i[:-4]
    path_to_file = "exports/" + i

    if user_wants_pfd:
        save_file_as = "exports/" + name_of_file + ".pdf"
        os.system("python " + path_to_pdf_script + " -o " + save_file_as + " -f Tahoma.ttf " + path_to_file)
    else:
        document = Document()
        my_file = open(path_to_file).read()
        my_file = re.sub(r'[^\x00-\x7F]+|\x0c',' ', my_file) # remove all non-XML-compatible characters
        p = document.add_paragraph(my_file)
        document.save("exports/" + name_of_file + '.docx')


