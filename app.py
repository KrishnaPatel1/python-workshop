# library which helps to read excel spreadsheets
import xlrd

# Find and store excel file
excelFile = xlrd.open_workbook('cover_letters.xlsx', on_demand = True)
# Choose which sheet to use inside your excel file
worksheet = excelFile.sheet_by_name('Sheet1')

# Set total amount of rows and columns
rows = worksheet.nrows
columns = worksheet.ncols

# Define start, end for the range 
for row in range(1, rows):
  for column in range(columns):
    # print values
    print(worksheet.cell(row, column).value)