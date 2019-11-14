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

def findValueInDictionariesAndReplace(templateDict, informationDict, nameOfFile):
  for firstKey in templateDict:
    for secondKey in informationDict:
      if firstKey == secondKey:
        findAndReplaceText(templateDict[firstKey], informationDict[secondKey], nameOfFile)

def findValuesAndReplace(dictString, string, nameOfFile):
  findAndReplaceText(dictString, string, nameOfFile)

# Find and store excel file
excelFile = xlrd.open_workbook('cover_letters.xlsx', on_demand = True)
# Choose which sheet to use inside your excel file
worksheet = excelFile.sheet_by_name('Sheet1')

# Set total amount of rows and columns
rows = worksheet.nrows
columns = worksheet.ncols

user_wants_pfd = int(input("Press 1 for PDF, or 0 for Word docx"))

boilerPlateTextToReplace = {
  "myName": "YourName",
  "myAddress": "YourAddress",
  "currentDate": "CurrentDate",
  "companyName": "CompanyName",
  "firstName": "ContactFirstName",
  "lastName": "ContactLastName",
  "gender": "Gender",
  "positionName": "PositionName",
  "companyAddress": "CompanyAddress"
}

# Define your personal details
name = "Tony Stark"
address = "10880 Malibu Point, 90265"
# Retrieve month name rather than number
currentMonth = date.today().strftime("%B")
currentDate = currentMonth + " " + str(date.today().day) + ", " + str(date.today().year)

coverLetterInformationToAdd = {
  "myName": name,
  "myAddress": address,
  "currentDate": currentDate
}

keyToAdd = None
stringToReplaceWith = None
fileName = None

# Define start, end for the range 
for row in range(1, rows):
  for column in range(columns):
    # Company name
    if column == 0:
      fileName = None
      keyToAdd = "companyName"
      stringToReplaceWith = worksheet.cell(row, column).value
      # Copy from template text file and name it based on company name
      fileName = os.getcwd() + "/exports/" + worksheet.cell(row, column).value + ".txt" 
      shutil.copyfile("cover-letter-template.txt", fileName)
      findValueInDictionariesAndReplace(
        boilerPlateTextToReplace, 
        coverLetterInformationToAdd, 
        fileName)
      
    # First name
    elif column == 1:
      keyToAdd = "firstName"
      stringToReplaceWith = worksheet.cell(row, column).value
    # Last name
    elif column == 2:
      keyToAdd = "lastName"
      stringToReplaceWith = worksheet.cell(row, column).value
    # Gender 
    elif column == 3:
      keyToAdd = "gender"
      if worksheet.cell(row, column).value == "Male":
        stringToReplaceWith = "Mr."
      else:
        stringToReplaceWith = "Ms."
    # Position Name  
    elif column == 4:
      keyToAdd = "positionName"
      stringToReplaceWith = worksheet.cell(row, column).value
    # Company Address
    elif column == 5:
      keyToAdd = "companyAddress"
      stringToReplaceWith = worksheet.cell(row, column).value
    
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
        os.remove("exports/" + name_of_file + ".txt")
    else:
        document = Document()
        myfile = open(path_to_file).read()
        myfile = re.sub(r'[^\x00-\x7F]+|\x0c',' ', myfile) # remove all non-XML-compatible characters
        p = document.add_paragraph(myfile)
        document.save("exports/" + name_of_file + '.docx')
        os.remove("exports/" + name_of_file + ".txt")


