import sqlite3
import csv
import os

def cargar_datos_iniciales():
    db_path = "data/tpv_abarrotes.db"
    csv_path = "data/seed_products.csv"
    
    if not os.path.exists(db_path):
        print("Error: La base de datos no existe. Ejecuta db_init.py primero.")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Ejemplo de datos manuales por si no tienes el CSV listo aún
    datos_manuales = [
        ('7501055300075', 'Coca Cola 600ml', 18.50, 14.00, 50),
        ('7501000611218', 'Gansito 50g', 15.00, 11.50, 30),
        ('7501030497233', 'Sabritas Sal 42g', 17.00, 13.00, 20)
    ]

    # Insertar datos manuales
    cursor.executemany("INSERT OR IGNORE INTO productos VALUES (?, ?, ?, ?, ?)", datos_manuales)
    
    # Lógica para cargar desde CSV si el archivo existe
    if os.path.exists(csv_path):
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader) # Saltar cabecera
            for fila in reader:
                cursor.execute("INSERT OR IGNORE INTO productos VALUES (?, ?, ?, ?, ?)", fila)
        print("✓ Datos del CSV cargados.")

    conn.commit()
    conn.close()
    print(f"Seed completado exitosamente.")

if __name__ == "__main__":
    cargar_datos_iniciales()