import openpyxl
 #reading 
file_path = "Excel_Files/employees.xlsx"

wb = openpyxl.load_workbook(file_path)
sheet = wb.active
#print all rows
for row in sheet.iter_rows(values_only = True):
    print(row)


