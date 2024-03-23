from openpyxl import Workbook
import time


wb=Workbook("C:\PYTHON PROGRAM\datasamp.xlsx")
sheet=wb.active

sheet [ 'a1' ] = 44
sheet['a2']="mani"
sheet['a3']=64
sheet['a4']=67

now = time.strftime("%x")
sheet [ 'A5' ] = now

wb.save("C:\PYTHON PROGRAM\datasamp.xlsx")