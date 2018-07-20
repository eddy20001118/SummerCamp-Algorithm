import xlrd

def writePoint(point = (),number = 0):
    f= open("/home/dji/SummerCamp-Algorithm/save/"+"solver"+str(number)+".txt",mode="w")
    for d in range(0,len(point)):
        f.write(point[d])
        f.write("\n")
    

data = xlrd.open_workbook('map.xlsx')
sheet = data.sheets()[2]
point1 = []                                        
pointPosition = []
R = []
Y = []
G = []
B = []
comb = ((0, 1), (0, 2), (0, 3))
comborder = ['0000', '0001', '0002', '0010', '0011', '0012', '0020', '0021', '0022', '0100', '0101', '0102', '0110', '0111','0112', '0120', '0121', '0122', '0200', '0201', '0202', '0210', '0211', '0212', '0220', '0221', '0222', '1000', '1001', '1002', '1010', '1011', '1012', '1020', '1021', '1022', '1100', '1101', '1102', '1110', '1111', '1112', '1120', '1121', '1122', '1200', '1201', '1202', '1210', '1211', '1212', '1220', '1221', '1222', '2000', '2001', '2002', '2010', '2011', '2012', '2020', '2021', '2022', '2100', '2101', '2102', '2110', '2111', '2112', '2120', '2121', '2122', '2200', '2201', '2202', '2210', '2211', '2212', '2220', '2221', '2222']
for i in range(0,8):
    row = []
    for h in range(0,8):
        val = str(sheet.cell(i,h))[7]
        if val!=".":
            pointPosition.append(val)
            pointPosition.append(i)
            pointPosition.append(h)

        row.append(val)
        
    #rowStr = "".join(row)
    point1.append(row)
pointPosition = tuple(pointPosition)
#print(pointPosition)
for a in range(0,len(pointPosition)):
    b = pointPosition[a]
    if b == "R":
        R.append(a)
    elif b == "Y":
        Y.append(a)
    elif b == "G":
        G.append(a)
    elif b == "B":
        B.append(a)

def conv(iterr = (),itery = (),iterg = (),iterb = ()):
    ps1 = list(pointPosition)
    ps1[R[iterr[0]]] = "r"
    ps1[R[iterr[1]]] = "r"
    ps1[Y[itery[0]]] = "y"
    ps1[Y[itery[1]]] = "y"
    ps1[G[iterg[0]]] = "g"
    ps1[G[iterg[1]]] = "g"
    ps1[B[iterb[0]]] = "b"
    ps1[B[iterb[1]]] = "b"   
    return tuple(ps1)


sthTowrite = []
for m in range(0,len(comborder)):
    iterr = comb[int(comborder[m][0])]
    itery = comb[int(comborder[m][1])]
    iterg = comb[int(comborder[m][2])]
    iterb = comb[int(comborder[m][3])]
    sthTowrite.append(conv(iterr,itery,iterg,iterb))

point3 = []
#####
for l in range(0,len(comborder)):
    sthw = sthTowrite[l]
    for ll in range (0,16):
        vvv = sthw[ll*3]
        pppx = sthw[ll*3+1]
        pppy = sthw[ll*3+2]
        point1[pppx][pppy] = vvv
        point1 = tuple(point1)
        
    point2 = []
    for ts in range(0,len(point1)):
        point2.append("".join(point1[ts]))
    point2 = tuple(point2)
    point3.append(point2)

for fff in range(0,len(comborder)):
    writePoint(point3[fff],fff)



#print(point2)
#print(len(sthTowrite[0]))
#writePoint(point1)


