import random
from models.database import Database

class seed:
    def run_seed():
        print("--- Iniciando poblado de datos (Seed) ---")
        
        # 1. Conectar a la DB
        db = Database()
        conn = db.get_connection()
        cursor = conn.cursor()

        # --- Limpiar datos viejos (Opcional, ten cuidado en prod) ---
        # cursor.execute("DELETE FROM sale_details")
        # cursor.execute("DELETE FROM sales")
        # cursor.execute("DELETE FROM products")
        # cursor.execute("DELETE FROM users")

        # 2. Crear Usuarios (Ej: Admin y Cajeros)
        users_data = [
            ("admin", "admin123", "Administrador"),
            ("cajero1", "1234", "Cajero"),
            ("cajero2", "1234", "Cajero")
        ]
        
        print(f"Insertando {len(users_data)} usuarios...")
        cursor.executemany("INSERT OR IGNORE INTO users (userName, password, role) VALUES (?, ?, ?)", users_data)

        # 3. Crear Productos Random
        nombres_productos = [
            "Coca Cola 600ml", "Pepsi 600ml", "Agua Ciel 1L", "Galletas Marias", 
            "Sabritas Sal", "Doritos Nacho", "Gansito", "Leche Lala 1L", 
            "Huevo Kilo", "Tortillas Kilo", "Jabón Zote", "Shampoo Caprice"
        ]

        print("Generando productos aleatorios...")
        for nombre in nombres_productos:
            stock = random.randint(10, 100) # Stock entre 10 y 100
            price = round(random.uniform(10.0, 50.0), 2) # Precio entre 10 y 50
            
            cursor.execute('''
                INSERT INTO products (productName, stock, price) 
                VALUES (?, ?, ?)
            ''', (nombre, stock, price))

        conn.commit()
        conn.close()
        print("--- Datos insertados con éxito en data/tpv.db ---")
