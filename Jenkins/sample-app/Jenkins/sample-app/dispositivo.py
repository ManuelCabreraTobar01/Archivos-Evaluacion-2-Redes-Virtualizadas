#!/usr/bin/env python3
import re

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

if __name__ == "__main__":
    print("=== Validación de IP para DispositivoRed ===")
    try:
        cantidad = int(input("¿Cuántos dispositivos deseas validar? (ej: 1 ó 3): ").strip())
    except Exception:
        cantidad = 1

    for i in range(1, cantidad + 1):
        nombre = input(f"Nombre del dispositivo {i}: ").strip()
        ip = input(f"IP del dispositivo {i}: ").strip()
        disp = DispositivoRed(nombre, ip)
        if disp.validar_ip():
            print(f"[OK] La IP '{disp.ip}' del dispositivo '{disp.nombre}' es válida.")
        else:
            print(f"[ERROR] La IP '{disp.ip}' del dispositivo '{disp.nombre}' NO es válida.")
