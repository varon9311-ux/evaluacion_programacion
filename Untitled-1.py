def calcular_descuento_base(monto):
    """Calcula el descuento inicial según el rango de precio."""
    if monto < 50:
        return 0.0
    elif 50 <= monto <= 100:
        return 0.10  # 10%
    else:
        return 0.20  # 20%

def aplicar_descuento_vip(subtotal, es_vip):
    """Aplica un 5% adicional si el usuario es VIP."""
    if es_vip:
        return subtotal * 0.95
    return subtotal

def procesar_compra():
    """Función principal para interactuar con el usuario y mostrar resultados."""
    # 1. Entrada de datos
    try:
        monto_inicial = float(input("Ingrese el valor de la compra: "))
    except ValueError:
        print("Error: Por favor ingrese un número válido.")
        return

    respuesta_vip = input("¿Es cliente VIP? (si/no): ").lower().strip()
    es_vip = respuesta_vip == "si"

    # 2. Lógica de cálculos
    porcentaje_base = calcular_descuento_base(monto_inicial)
    subtotal = monto_inicial * (1 - porcentaje_base)
    total_final = aplicar_descuento_vip(subtotal, es_vip)

    # 3. Salida de resultados
    print("-" * 30)
    print(f"Monto original: ${monto_inicial:.2f}")
    print(f"Descuento base aplicado: {porcentaje_base * 100:.0f}%")
    print(f"Subtotal: ${subtotal:.2f}")
    
    if es_vip:
        print("Se aplicó un 5% adicional por ser miembro VIP.")
        
    print(f"TOTAL A PAGAR: ${total_final:.2f}")
    print("-" * 30)

# Ejecución del programa
if __name__ == "__main__":
    procesar_compra()