import pandas as pd
import glob
for excel_filename in glob.glob("*.xlsx"):
    print(f"ファイル名:{excel_filename}")
    datefile = pd.read_excel(excel_filename,engine="openpyxl")
    print(datefile)
    