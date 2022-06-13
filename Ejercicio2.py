cont = 0
municipio = [1,2,3],[1,2,3],[1,2,3]

while cont < 3:
    municipio[0][cont] = input("Ingrese un estado ")
    municipio[1][cont] = input("Ingrese los habitantes ")
    cont = cont+1

habitantestotales = int(municipio[1][0]) + int(municipio[1][1]) + int(municipio[1][2])

promediahabitantes = habitantestotales/3

print("El numero de habitantes totales " + str(habitantestotales))
print("El promedio de habitantes es de " + str(promediahabitantes))