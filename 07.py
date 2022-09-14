"""
Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
A formula de conversão é: C = (F - 32) * (5 / 9) , sendo C a temperatura em Celsius e 
F a temperatura em Fahrenheit
"""
F = float(input("Digite o valor em Fahrenheit:  "))
C = (F - 32) * (5 / 9)

print(f'Valor em Celsius: {C}°C')