Cemento = 40
Yeso = 30
Camion = 3254

CantC = input("Cuántos costales de cemento se entregarán? ")
CantY = input("Cuántos costales de yeso se entregarán? ")

TotalC = int(CantC) * int(Cemento)
TotalY = int(CantY) * int(Yeso)

TotalCY = TotalC + TotalY

if TotalCY < Camion:
    print("El viaje si se puede realizar")
else:
    print("El viaje no se puede realizar")
    
print("El total del peso es de " + str(TotalCY))