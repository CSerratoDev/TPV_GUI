from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from models.database import Database

class MessagePopup(Popup):
    message = StringProperty("")

class MainRoot(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = Database()

    def reset(self):
        print("Reset al sistema...")

    def admin(self):
        print("Admin presionado")

    def exit(self):    
        print("Salir presionado")

    def show_popup(self, text):
        pop = MessagePopup(message=text)
        pop.open()
    
    def add_product(self, productId, productName):
        if not productId.strip() and not productName.strip():
            self.show_popup("Error: Debes ingresar al menos un criterio de búsqueda.")
            return

        results = self.db.get_product(productId, productName)

        if results:
            if len(results) == 1:
                self.insert_into_cart(results[0])
            else:
                self.show_selection_modal(results)
        else:
            self.show_popup("Producto no encontrado.")

    def insert_into_cart(self, product):
        product_name, price = product
        print(f"Producto agregado al carrito: {product_name} - Precio: ${price}")

        container = self.ids.cart_container

        row = BoxLayout(size_hint_y=None, height=36, spacing=3)

        row.add_widget(Label(text="1", size_hint_x=0.1, color=(0,0,0,1))) # ID temporal
        row.add_widget(Label(text=product_name, size_hint_x=0.5, color=(0,0,0,1)))
        row.add_widget(Label(text="1", size_hint_x=0.1, color=(0,0,0,1))) # Cantidad inicial
        row.add_widget(Label(text=f"{price:.2f}", size_hint_x=0.15, color=(0,0,0,1)))
        row.add_widget(Label(text=f"{price:.2f}", size_hint_x=0.15, color=(0,0,0,1)))
    
        container.add_widget(row)

        print(f"Producto visual agregado: {product_name}")
    def put_product(self, product_id, new_price, quantity_sold):
        if not product_id or not new_price or not quantity_sold:
            print("Faltan datos para editar")
            return
    
    def delete_product(self):
        print("Click eliminar producto")

    def sell(self):
        print("Click en finalizar compra")
    
class TPVApp(App):
    def build(self):
        return MainRoot()