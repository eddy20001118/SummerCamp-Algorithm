import xlrd

def writePoint(point = []):
    f= open("solver.txt",mode="w")
    for d in range(0,len(point)):
        f.write(point[d])
        f.write("\n")


data = xlrd.open_workbook('map.xlsx')
sheet = data.sheets()[0]
point1 = []
val = sheet.cell(0,0)
for i in range(0,8):
    row = []
    for h in range(0,8):
        val = str(sheet.cell(i,h))[7]
        row.append(val)
        
    rowStr = "".join(row)
    point1.append(rowStr)


writePoint(point1)