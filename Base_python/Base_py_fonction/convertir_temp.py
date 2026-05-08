# 5. Écrivez une fonction convertir_temperature() qui prend une température en degrés Celsius et la convertit en degrés
# Fahrenheit.
	
# (0 °C × 9/5) + 32 = 32 °F

def convertir_temperature():
    temp = int(input("Entrer une température en Celsius à convertir en Fahrenheit: "))
    return (temp * 9/5) + 32

