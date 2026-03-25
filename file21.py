# Excel

import openpyxl as xl

path = ("./others/transactions.xlsx")

workbook = xl.load_workbook(path)

sheet = workbook['Sheet1']


