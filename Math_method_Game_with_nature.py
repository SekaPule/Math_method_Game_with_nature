def print_array(arr):
    for row in arr:
        for item in row:
            print(item, end='\t')
        print()


"""
Example:
10	80	40	-20
50	90	35	0
-40	150	55	-15
20	25	35	15
"""

row = int(input("Set number of Rows: "))
col = int(input("Set number of Columns: "))
kefl, kefs, kefm, kefv, kefg = 0, 0, 0, 0, 0
flag = True

mat = [[int(input("Input nums from keyboard:")) for x in range(col)] for y in range(row)]
koef_optimizm = float(input("Input the coefficient of optimism: "))
arrMaxInCol = []
arrMinInRow = []
arrMaxInRow = []
riskMaxInRow = []
#riskMat = []#t0d0

print("Payoff matrix")
print_array(mat)

for i in range(row):
    min = mat[i][0]
    maxr = mat[i][0]
    for j in range(col):
        if(min > mat[i][j]):
            min = mat[i][j]
        if (maxr < mat[i][j]):
            maxr = mat[i][j]
    arrMinInRow.append(min)#Запись наименьших элементов по строкам
    arrMaxInRow.append(maxr)#Запись наибольших элементов по строкам
for i in range(col):
    max = mat[0][i]
    for j in range(row):
        if (max < mat[j][i]):
            max = mat[j][i]
    arrMaxInCol.append(max)#Запись наибольших элементов по столбцам

#LAPLAS
cr_laplasa = 0
for i in range(row):
    sum = 0
    for j in range(col):
        sum += (mat[i][j]/col)
    if(cr_laplasa < sum):
        cr_laplasa = sum
        kefl = i+1

#Изменение платежной матрицы в матрицу рисков

for i in range(col):
    for j in range(row):
        mat[j][i] = arrMaxInCol[i]-mat[j][i]

for i in range(row):
    max = mat[i][0]
    for j in range(col):
        if(max < mat[i][j]):
            max = mat[i][j]
    riskMaxInRow.append(max)

cr_valda = arrMinInRow[0]
cr_sevidja = arrMaxInRow[0]
cr_gurvica = 0
cr_maximaxa = 0

#Нахождение критериев

for j in range(len(arrMinInRow)):
    if(cr_valda < arrMinInRow[j]):
        cr_valda = arrMinInRow[j]
        kefv = j+1
for j in range(len(riskMaxInRow)):
    if(cr_sevidja > riskMaxInRow[j]):
        cr_sevidja = riskMaxInRow[j]
        kefs = j+1
for j in range(len(arrMaxInRow)):
    max = ((koef_optimizm*arrMinInRow[j])+((1-koef_optimizm)*arrMaxInRow[j]))
    if(cr_gurvica < max):
        cr_gurvica = max
        kefg = j+1
for j in range(len(arrMaxInRow)):
    if(cr_maximaxa < arrMaxInRow[j]):
        cr_maximaxa = arrMaxInRow[j]
        kefm = j+1

print("\nRisk matrix:")
print_array(mat)

while(flag):
    choice = int(input("Choose criterion: 1-Valda, 2-Maximaxa, 3-Laplasa, 4-Gurvica, 5-Sevidja: "))
    if(choice == 1):
        print(cr_valda, end=" - Критерий Вальда(Выбираем стратегию № %.d)\n" % kefv)
    elif(choice == 2):
        print(cr_maximaxa, end=" - Критерий максимакса(Выбираем стратегию № %.d)\n" % kefm)
    elif(choice == 3):
        print(cr_laplasa, end=" - Критерий Лапласа(Выбираем стратегию № %.d)\n" % kefl)
    elif(choice == 4):
        print(cr_gurvica, end=" - Критерий Гурвица(Выбираем стратегию № %.d)\n" % kefg)
    elif(choice == 5):
        print(cr_sevidja, end=" -  Критерий Севиджа(Выбираем стратегию № %.d)\n" % kefs)
    if(input("s - stop! | n - next!") == 's'):
        flag = False
    elif(input() == 'n'):
        flag = True
