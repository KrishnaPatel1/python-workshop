import xlrd

excelFile = xlrd.open_workbook('cover_letters.xlsx', on_demand = True)
worksheet = excelFile.sheet_by_name('Sheet1')

print(worksheet.cell(0, 0).value)
