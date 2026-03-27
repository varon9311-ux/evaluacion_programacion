# 1. Pedir al usuario el valor de la compra
monto_inicial = float(input("Ingrese el valor de la compra: "))

# 2. Preguntar si el cliente es VIP
es_vip = input("¿Es cliente VIP? (si/no): ").lower().strip() == "si"

# 3. Calcular el descuento por monto
if monto_inicial < 50:
    descuento_base = 0
elif 50 <= monto_inicial <= 100:
    descuento_base = 0.10  # 10%
else:
    descuento_base = 0.20  # 20%

# Aplicamos el primer descuento
subtotal = monto_inicial * (1 - descuento_base)

# Aplicar el 5% adicional si es VIP sobre el subtotal
if es_vip:
    total_final = subtotal * 0.95  # Se resta el 5%
else:
    total_final = subtotal

# 4. Mostrar el total a pagar
print("-" * 30)
print(f"Monto original: ${monto_inicial:.2f}")
print(f"Subtotal con descuento inicial: ${subtotal:.2f}")
if es_vip:
    print("Se aplicó un 5% adicional por ser miembro VIP.")
print(f"TOTAL A PAGAR: ${total_final:.2f}")
print("-" * 30)