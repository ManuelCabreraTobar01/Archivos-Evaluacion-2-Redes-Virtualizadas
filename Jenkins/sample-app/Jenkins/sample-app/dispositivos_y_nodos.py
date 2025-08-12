#!/usr/bin/env python3
import re
import json

# ====== Parte A: Clase DispositivoRed con validación de IP ======
class DispositivoRed:
    """
    Clase que representa un dispositivo de red con nombre e IP.
    Método validar_ip() verifica si la IP es una IPv4 válida usando regex.
    """
    def __init__(self, nombre: str, ip: str):
        self.nombre = nombre
        self.ip = ip.strip()

    def validar_ip(self) -> bool:
        """
        Retorna True si la IP es válida (IPv4 0-255 en cada octeto), False en caso contrario.
        Regex usado: (25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)
        """
        patron = re.compile(r'^((25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}'
                            r'(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)$')
        return bool(patron.match(self.ip))

# ====== Parte B: Lista de nodos y exportación a JSON ======
def exportar_nodos():
    # Lista de diccionarios (mínimo 3 nodos)
    nodos = [
        {"nombre": "Router1", "pais": "Chile", "tipo": "Router"},
        {"nombre": "Switch1", "pais": "Peru", "tipo": "Switch"},
        {"nombre": "Firewall1", "pais": "Argentina", "tipo": "Firewall"}
    ]
    with open("nodos.json", "w") as f:
        json.dump(nodos, f, indent=4)
    print("✅ Archivo 'nodos.json' creado correctamente.")

# ====== Ejecución principal ======
if __name__ == "__main__":
    print("=== VALIDACIÓN DE IP ===")
    try:
        cantidad = int(input("¿Cuántos dispositivos deseas validar?: ").strip())
    except ValueError:
        cantidad = 1

    for i in range(1, cantidad + 1):
        nombre = input(f"Nombre del dispositivo {i}: ").strip()
        ip = input(f"IP del dispositivo {i}: ").strip()
        disp = DispositivoRed(nombre, ip)
        if disp.validar_ip():
            print(f"[OK] {nombre} -> IP válida")
        else:
            print(f"[ERROR] {nombre} -> IP inválida")

    print("\n=== EXPORTANDO NODOS A JSON ===")
    exportar_nodos()
