# Library which helps to read excel spreadsheets
import xlrd
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
  file.close()

def findValueInDictionariesAndReplace(templateDict, informationDict, nameOfFile):
  for firstKey in templateDict:
    for secondKey in informationDict:
      if firstKey == secondKey:
        findAndReplaceText(templateDict[firstKey], informationDict[secondKey], nameOfFile)

def findValuesAndReplace(templateDict, string, nameOfFile):
  for firstKey in templateDict:
    if firstKey == string:
      findAndReplaceText(templateDict[firstKey], string, nameOfFile)

# Find and store excel file
excelFile = xlrd.open_workbook('cover_letters.xlsx', on_demand = True)
# Choose which sheet to use inside your excel file
worksheet = excelFile.sheet_by_name('Sheet1')

# Set total amount of rows and columns
rows = worksheet.nrows
columns = worksheet.ncols

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

boilerPlateTextToReplace = {
  "myName": "YourName",
  "myAddress": "YourAddress",
  "currentDate": "CurrentDate",
  "firstName": "ContactFirstName",
  "lastName": "ContactLastName",
  "companyName": "CompanyName",
  "companyAddress": "CompanyAddress",
  "gender": "Gender"
}

# Define start, end for the range 
for row in range(1, rows):
  for column in range(columns):
    # Stop when we reach company name
    if column == 0:
      # Copy from template text file and name it based on company name
      shutil.copyfile("cover-letter-template.txt", worksheet.cell(row, column).value)
      findValueInDictionariesAndReplace(
        boilerPlateTextToReplace, 
        coverLetterInformationToAdd, 
        worksheet.cell(row, column).value)
      
    print(worksheet.cell(row, column).value)