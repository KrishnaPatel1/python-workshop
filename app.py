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

def find_value_in_dictionaries_and_replace(template_dict, information_dict, name_of_file):
  for firstKey in template_dict:
    for secondKey in information_dict:
      if firstKey == secondKey:
        find_and_replace_text(template_dict[firstKey], information_dict[secondKey], name_of_file)

def find_values_and_replace(dict_string, string, name_of_file):
  find_and_replace_text(dict_string, string, name_of_file)

# Find and store excel file
excel_file = xlrd.open_workbook('cover_letters.xlsx', on_demand = True)
# Choose which sheet to use inside your excel file
worksheet = excel_file.sheet_by_name('Sheet1')

# Set total amount of rows and columns
rows = worksheet.nrows
columns = worksheet.ncols

user_wants_pfd = int(input("Press 1 for PDF, or 0 for Word docx"))

boiler_plate_text_to_replace = {
  "my_name": "YourName",
  "my_address": "YourAddress",
  "current_date": "CurrentDate",
  "company_name": "CompanyName",
  "first_name": "ContactFirstName",
  "last_name": "ContactLastName",
  "gender": "Gender",
  "position_name": "PositionName",
  "company_address": "CompanyAddress"
}

# Define your personal details
name = "Tony Stark"
address = "10880 Malibu Point, 90265"
# Retrieve month name rather than number
current_month = date.today().strftime("%B")
current_date = current_month + " " + str(date.today().day) + ", " + str(date.today().year)

cover_letter_information_to_add = {
  "my_name": name,
  "my_address": address,
  "current_date": current_date
}

key_to_add = None
string_to_replace_with = None
file_name = None

# Define start, end for the range 
for row in range(1, rows):
  for column in range(columns):
    # Company name
    if column == 0:
      file_name = None
      key_to_add = "company_name"
      string_to_replace_with = worksheet.cell(row, column).value
      # Copy from template text file and name it based on company name
      file_name = os.getcwd() + "/exports/" + worksheet.cell(row, column).value + ".txt" 
      shutil.copyfile("cover-letter-template.txt", file_name)
      find_value_in_dictionaries_and_replace(
        boiler_plate_text_to_replace, 
        cover_letter_information_to_add, 
        file_name)
      
    # First name
    elif column == 1:
      key_to_add = "first_name"
      string_to_replace_with = worksheet.cell(row, column).value
    # Last name
    elif column == 2:
      key_to_add = "last_name"
      string_to_replace_with = worksheet.cell(row, column).value
    # Gender 
    elif column == 3:
      key_to_add = "gender"
      if worksheet.cell(row, column).value == "Male":
        string_to_replace_with = "Mr."
      else:
        string_to_replace_with = "Ms."
    # Position Name  
    elif column == 4:
      key_to_add = "position_name"
      string_to_replace_with = worksheet.cell(row, column).value
    # Company Address
    elif column == 5:
      key_to_add = "company_address"
      string_to_replace_with = worksheet.cell(row, column).value
    
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
        os.remove("exports/" + name_of_file + ".txt")
    else:
        document = Document()
        my_file = open(path_to_file).read()
        my_file = re.sub(r'[^\x00-\x7F]+|\x0c',' ', my_file) # remove all non-XML-compatible characters
        p = document.add_paragraph(my_file)
        document.save("exports/" + name_of_file + '.docx')
        os.remove("exports/" + name_of_file + ".txt")


