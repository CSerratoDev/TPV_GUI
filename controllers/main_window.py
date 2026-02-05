from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

#Importando la base de datos
from models.database import Database

#Ventana principal de tpv
class MainRoot(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = Database() #Creamos la instancia de la base de datos para evitar errores

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

    def agregar_producto_nombre(self, productName):
        if not productName:
            print("El Nombre está vacío")
            return
        
        #Repito, sin el self en el parametro, python lo detectara solo xd
        self.db.get_productoName(productName)

    #Panel de control
    def agregar_producto(self, productId):
        if not productId:
            print("El ID está vacío")
            return
        
        #Sin el self, python lo detectara solo algo curioso xd
        self.db.get_productId(productId)
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