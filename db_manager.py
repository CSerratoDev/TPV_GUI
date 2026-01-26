import sqlite3

def buscar_producto_db(codigo):
    conn = sqlite3.connect("data/tpv.db")
    cursor = conn.cursor()
    cursor.execute("SELECT codigo_barras, nombre, precio_venta FROM productos WHERE codigo_barras = ?", (codigo,))
    resultado = cursor.fetchone()
    conn.close()
    
    if resultado:
        return {
            'codigo': resultado[0],
            'nombre': resultado[1],
            'precio': resultado[2]
        }
    return None