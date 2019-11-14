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
def findAndReplaceText(stringInFile, stringToReplaceWith, nameOfFile):
  with fileinput.FileInput(nameOfFile, inplace=True) as file:
    for line in file:
      print(line.replace(stringInFile, stringToReplaceWith), end='')

# Function to find values inside the dictionary provided, and replace
def findValueInDictionariesAndReplace(templateDict, informationDict, nameOfFile):
  for firstKey in templateDict:
    for secondKey in informationDict:
      if firstKey == secondKey:
        findAndReplaceText(templateDict[firstKey], informationDict[secondKey], nameOfFile)

# Function to find values, and replace
def findValuesAndReplace(dictString, string, nameOfFile):
  findAndReplaceText(dictString, string, nameOfFile)

# Find and store excel file
excelFile = xlrd.open_workbook('cover_letters.xlsx', on_demand = True)
# Choose which sheet to use inside your excel file
worksheet = excelFile.sheet_by_name('Sheet1')

# Set total amount of rows and columns
rows = worksheet.nrows
columns = worksheet.ncols

# User input for PDF or Word document
user_wants_pfd = input("Press 1 for PDF, or 0 for Word docx")

# Step 1
# Create a dictionary linking your keys, to the values inside the template file
boilerPlateTextToReplace = {
  
}

# Step 2  
# Set personal details to add to cover letter
# Retrieve month name rather than number
currentMonth = date.today().strftime("%B")
currentDate = currentMonth + " " + str(date.today().day) + ", " + str(date.today().year)

# Set information in a dictionary with above information
coverLetterInformationToAdd = {
  
}

# Values with no variables to use in loops
keyToAdd = None
stringToReplaceWith = None
fileName = None

# Define start, end for the range 
# First for loop with range of data based on rows
# Second for loop with range of data based on columns

  # Traverse through all the columns of data in a single row of the excel sheet
  # Note: Use if and elif statements
    # Company name 
      fileName = None
      # Set keyToAdd with key from object you want to add

      # Set stringToReplaceWith from worksheet cell value

      # Copy from template text file and name it based on company name
      fileName = os.getcwd() + "/exports/" + worksheet.cell(row, column).value + ".txt" 
      shutil.copyfile("cover-letter-template.txt", fileName)
      
      # Pass variables in function to find the value and replace with new value
      findValueInDictionariesAndReplace(
        boilerPlateTextToReplace, 
        coverLetterInformationToAdd, 
        fileName)
      
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
    if keyToAdd != None:
      findValuesAndReplace(
        boilerPlateTextToReplace[keyToAdd], 
        stringToReplaceWith, 
        fileName)

    # Reset variables
    keyToAdd = None
    stringToReplaceWith = None

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
        myfile = open(path_to_file).read()
        myfile = re.sub(r'[^\x00-\x7F]+|\x0c',' ', myfile) # remove all non-XML-compatible characters
        p = document.add_paragraph(myfile)
        document.save("exports/" + name_of_file + '.docx')


