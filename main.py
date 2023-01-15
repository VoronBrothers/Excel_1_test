from openpyxl import Workbook
import datetime
import os


work = Workbook()

sheet = work.active

sheet["A1"] = "VoronBrothers"
sheet["A2"] = "Название операционной системы: " + os.name
sheet["a3"] = os.getlogin()

#Дата изменения файла + сохранение в файл
sheet["A20"] = datetime.datetime.now()
work.save("vbexcel.xlsx")

print(os.listdir("."))