import os
from db_init import inicializar_db
import kivy
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, ListProperty
from db_manager import buscar_producto_db  # Importamos la lógica de DB

Builder.load_file('main.kv')

class TPVRoot(BoxLayout):
    carrito = ListProperty([])  # Lista dinámica de productos en la venta actual
    
    def agregar_producto_por_codigo(self, codigo):
        """ Se activa cuando el escáner lee un código """
        producto = buscar_producto_db(codigo)
        
        if producto:
            # Lógica para sumar cantidad si ya existe en el carrito
            encontrado = False
            for item in self.carrito:
                if item['codigo'] == codigo:
                    item['cantidad'] += 1
                    encontrado = True
                    break
            
            if not encontrado:
                self.carrito.append({
                    'codigo': producto['codigo'],
                    'nombre': producto['nombre'],
                    'precio': producto['precio'],
                    'cantidad': 1
                })
            print(f"Producto añadido: {producto['nombre']}")
        else:
            print("Producto no encontrado en el sistema.")

    def eliminar_del_carrito(self, index):
        if self.carrito:
            self.carrito.pop(index)

    def calcular_total(self):
        return sum(item['precio'] * item['cantidad'] for item in self.carrito)

    def finalizar_venta(self):
        total = self.calcular_total()
        if total > 0:
            # Aquí llamarías a la función para guardar en DB e imprimir ticket
            print(f"Venta finalizada por: ${total}")
            self.carrito = [] # Limpiar carrito

class TPVApp(App):
    def build(self):
        return TPVRoot()

if __name__ == '__main__':
    # Si no existe la base de datos, la creamos antes de lanzar la App
    if not os.path.exists("data/tpv_abarrotes.db"):
        print("Primera ejecución detectada. Configurando...")
        inicializar_db()
    
    TPVApp().run()