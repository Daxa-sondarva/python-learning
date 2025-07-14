import openpyxl
 #append 
file_path = "Excel_Files\employees.xlsx"
wb = openpyxl.load_workbook(file_path)
sheet = wb.active
#append a new employee
sheet.append([4,"sam",29,"Marketing"])
#save changes
wb.save(file_path)
print("Data appended successfully!")
#print all rows
for row in sheet.iter_rows(values_only = True):
    print(row)

