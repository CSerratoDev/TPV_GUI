import sqlite3
import os

class Database:
    def __init__(self, db_name="data/tpv.db"):
        self.db_name = db_name
        self.ensure_directory()
        self.create_tables()

    def ensure_directory(self):
        directory = os.path.dirname(self.db_name)
        if not os.path.exists(directory):
            os.makedirs(directory)

    def get_connection(self):
        return sqlite3.connect(self.db_name)

    def create_tables(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()

            # 1. Tabla Usuarios
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    userId INTEGER PRIMARY KEY AUTOINCREMENT,
                    userName TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    role TEXT NOT NULL
                )
            ''')

            # 2. Tabla Productos
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    productId INTEGER PRIMARY KEY AUTOINCREMENT,
                    productName TEXT NOT NULL,
                    stock INTEGER NOT NULL,
                    price REAL NOT NULL
                )
            ''')

            # 3. Tabla Ventas (Cabecera del ticket/carrito)
            # Guarda quién vendió, cuándo y el total global
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS sales (
                    saleId INTEGER PRIMARY KEY AUTOINCREMENT,
                    userId INTEGER,
                    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    totalAmount REAL,
                    FOREIGN KEY(userId) REFERENCES users(userId)
                )
            ''')

            # 4. Tabla Detalles de Venta (Los items del carrito)
            # Aquí es donde ocurre la magia del escaneo
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS sale_details (
                    detailId INTEGER PRIMARY KEY AUTOINCREMENT,
                    saleId INTEGER,
                    productId INTEGER,
                    amount INTEGER NOT NULL,      -- Cantidad escaneada
                    unitPrice REAL NOT NULL,      -- Precio en el momento de la venta
                    priceFinal REAL NOT NULL,     -- Subtotal (amount * unitPrice)
                    FOREIGN KEY(saleId) REFERENCES sales(saleId),
                    FOREIGN KEY(productId) REFERENCES products(productId)
                )
            ''')
            
            conn.commit()
            print("Base de datos inicializada correctamente.")

# Instancia global para ser importada (opcional, pero útil en Singleton)
# db = Database()