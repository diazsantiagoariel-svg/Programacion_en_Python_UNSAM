#coso.py
print(5*5)
print(5**5)

for    i in range(5):
        print(i)


#Una mañana ponés un billete en la vereda al lado del obelisco porteño. A partir de ahí, cada día vas y duplicás la cantidad de billetes, apilándolos prolijamente. ¿Cuánto tiempo pasa antes de que la pila de billetes sea más alta que el obelisco?
#Acá va una solución:

grosor_billete = 0.11 * 0.001  # grosor de un billete en metros
altura_obelisco = 6700.5         # altura en metros
num_billetes = 1
dia = 1

while num_billetes*grosor_billete <= altura_obelisco:
    num_billetes= num_billetes * 2
    dia= dia +1
    print(dia, num_billetes, num_billetes * grosor_billete)

print('Cantidad de días', dia)
print('Cantidad de billetes', num_billetes)
print('Altura final', num_billetes * grosor_billete)
