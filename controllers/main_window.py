from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MainRoot(BoxLayout):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    #Sesiones
    def admin(self):
        print("Admin presionado")

    def salir(self):    
        print("Salir presionado")

    #Operador
    def nueva_compra(self):
        print("Reset al sistema...")

    def buscar_producto(self):
        print("Click buscar producto")

    def agregar_producto_nombre(self, nombre):
        print("Buscando: " , nombre)

    #Panel de control
    def agregar_producto(self):
        print("Click en agregar")

    def editar_producto(self):
        print("Click editar producto")

    def eliminar_producto(self):
        print("Click eliminar producto")

    def verificar_precio(self):
        print("Click verificar producto")

    #Compra y Cancelación
    def finalizar_venta(self):
        print("Click en finalizar compra")
    
    def carrito(self):
        print('Click en cancelar')
    
class TPVApp(App):
    def build(self):
        return MainRoot()