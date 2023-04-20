import openpyxl

pd = openpyxl.load_workbook("cor_hw.xlsx")
ws = pd["身長と体重の相関"]

for row in ws.rows:
    for colum in ws.columns:
        print()