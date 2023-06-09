import csv
import serial
import time
import numpy as np
import matplotlib.pyplot as plt

# Establecer la comunicación serial con Arduino
arduino = serial.Serial('COM3', 9600)

# Configurar la ventana de gráficos
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(12, 7)) # La figura se crea con subplots, y muestra 3 filas, 1 columna, anch0 12 pulg, altura 7 pulg
plt.subplots_adjust(hspace=0.5)

# Inicializar las variables para almacenar los datos
Acel_X = []
Acel_Y = []
Acel_Z = []
Gyro_X = []
Gyro_Y = []
Gyro_Z = []
Altitud = []
Temperatura = []

# Función para actualizar los datos y graficarlos en tiempo real
def update():
    # Leer los datos desde Arduino
    data = arduino.readline().decode('utf-8').strip().split(',')
    # Convertir los datos a valores numéricos
    X_Acel = float(data[0])
    Y_Acel = float(data[1])
    Z_Acel = float(data[2])
    X_Gyro = float(data[3])
    Y_Gyro = float(data[4])
    Z_Gyro= float(data[5])
    Altit = float(data[6])
    Temp = float(data[7])
    # Almacenar los datos
    Acel_X.append(X_Acel)
    Acel_Y.append(Y_Acel)
    Acel_Z.append(Z_Acel)
    Gyro_X.append(X_Gyro)
    Gyro_Y.append(Y_Gyro)
    Gyro_Z.append(Z_Gyro)
    Altitud.append(Altit)
    Temperatura.append(Temp)
    # Actualizar las gráficas
    ax1.clear()
    ax1.plot(Acel_X, label='X')
    ax1.plot(Acel_Y, label='Y')
    ax1.plot(Acel_Z, label='Z')
    ax1.set_title('Acelerómetro')
    ax1.legend()
    ax2.clear()
    ax2.plot(Gyro_X, label='X')
    ax2.plot(Gyro_Y, label='Y')
    ax2.plot(Gyro_Z, label='Z')
    ax2.set_title('Giroscopio')
    ax3.legend()
    ax3.clear()
    ax3.plot(Altitud, label= 'Alti')
    ax3.set_title('Altitud')
    ax3.legend()
    ax4.clear()
    ax4.plot(Temperatura, label= 'Temp')
    ax4.set_title('Temperatura')
    ax4.legend()
    with open('datos.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Accel X', 'Accel Y', 'Accel Z', 'Gyro X', 'Gyro Y', 'Gyro Z', 'Altitud', 'Temperatura'])
            for i in range(len(Gyro_X)):
                writer.writerow([Acel_X[i], Acel_Y[i], Acel_Z[i], Gyro_X[i], Gyro_Y[i], Gyro_Z[i], Altitud[i], Temperatura[i]])
# Bucle principal
while True:
    update()
    plt.pause(0.001)
