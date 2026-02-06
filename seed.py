import random
from models.database import Database

class seed:
    def run_seed():
        print("--- Iniciando poblado de datos (Seed) ---")
        db = Database()
        conn = db.get_connection()
        cursor = conn.cursor()
        users_data = [
            ("admin", "admin123", "Administrador"),
            ("cajero1", "1234", "Cajero"),
            ("cajero2", "1234", "Cajero")
        ]
        print(f"Insertando {len(users_data)} usuarios...")
        cursor.executemany("INSERT OR IGNORE INTO users (userName, password, role) VALUES (?, ?, ?)", users_data)
        
        nombres_productos = [
            "Coca Cola", "Pepsi", "Agua Ciel", "Galletas Marias", 
            "Sabritas Sal", "Doritos Nacho", "Gansito", "Leche Lala", 
            "Huevo", "Tortillas", "Jabón Zote", "Shampoo Caprice"
        ]
        print("Generando productos aleatorios...")
        for nombre in nombres_productos:
            stock = random.randint(10, 100)
            price = round(random.uniform(10.0, 50.0), 2)
            
            cursor.execute('''
                INSERT INTO products (productName, stock, price) 
                VALUES (?, ?, ?)
            ''', (nombre, stock, price))
        conn.commit()
        conn.close()
        print("--- Datos insertados con éxito en data/tpv.db ---")
