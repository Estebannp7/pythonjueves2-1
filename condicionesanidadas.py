#CONDICIONES ANIDADAS ELIF

sensorNivelAgua = int(input("Digite el nivel de agua actual:"))

if(sensorNivelAgua>=0 and sensorNivelAgua<20):
    print(f' Peligro el nivel de agua en  {sensorNivelAgua} es peligroso')
elif(sensorNivelAgua>=20 and sensorNivelAgua<400):
    print(f' Hidroituango te cuida  {sensorNivelAgua}')
elif(sensorNivelAgua>=400):
    print(f'Peligro el nivel de agua en {sensorNivelAgua} es peligroso')
else:
    print("El nivel del agua no es valido")
