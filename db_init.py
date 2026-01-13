import sqlite3
import os

def inicializar_db():
    # Aseguramos que la carpeta data exista
    if not os.path.exists('data'):
        os.makedirs('data')
        
    conn = sqlite3.connect("data/tpv_abarrotes.db")
    cursor = conn.cursor()

    # Activar llaves foráneas para integridad
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Tabla Productos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            codigo_barras TEXT PRIMARY KEY,
            nombre TEXT NOT NULL,
            precio_venta REAL NOT NULL,
            precio_costo REAL NOT NULL,
            stock INTEGER DEFAULT 0
        )
    ''')

    # Tabla Ventas Cabecera
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ventas_cabecera (
            id_venta INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
            total REAL NOT NULL,
            metodo_pago TEXT
        )
    ''')

    # Tabla Ventas Detalle
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ventas_detalle (
            id_detalle INTEGER PRIMARY KEY AUTOINCREMENT,
            id_venta INTEGER,
            codigo_barras TEXT,
            cantidad INTEGER,
            precio_unitario REAL,
            subtotal REAL,
            FOREIGN KEY (id_venta) REFERENCES ventas_cabecera (id_venta),
            FOREIGN KEY (codigo_barras) REFERENCES productos (codigo_barras)
        )
    ''')

    conn.commit()
    conn.close()
    print("Base de datos inicializada correctamente.")

if __name__ == "__main__":
    inicializar_db()